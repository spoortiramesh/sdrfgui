from sdrf_pipelines.zooma import ols
from sdrf_pipelines.sdrf import sdrf, sdrf_schema
from utilities import load_sdrf
import pandas as pd

client = ols.OlsClient()


def _get_organism_schema(df):
    organism_templates = []
    
    # First check for column cell line
    if "characteristics[cell line]" in df:
        not_avail_or_app = df["characteristics[cell line]"].isin({sdrf_schema.NOT_APPLICABLE, sdrf_schema.NOT_AVAILABLE})
        if sum(~not_avail_or_app) != 0:
            # if it is set to true we add the cell line template/schema
            organism_templates.append(sdrf_schema.CELL_LINES_TEMPLATE)

    # Check remaining rows
    rem_df = df.loc[not_avail_or_app]

    if "characteristics[organism]" in rem_df:
        orgs = set(df["characteristics[organism]"])

        for o in orgs:
            # Check if it is partially machine readable
            if "NT=" in o:
                # In case, then we simply extract the "NT=" information
                o_split = o.split(";")
                for o_s in o_split:
                    if o_s.strip().startswith("NT="):
                        o = o_s[3:]
                        break
            
            # Use ontology to retrieve the name of the best hit 
            result = client.besthit(o, ontology='ncbitaxon')
            if result:
                # Check for the special case human
                if result["label"].lower() == "homo sapiens":
                    organism_templates.append(sdrf_schema.HUMAN_TEMPLATE)
                    continue

                # Check for the remaining schemas/templates by using the ancestors
                if "iri" in result:
                    ancs = client.get_ancestors("ncbitaxon", result["iri"])
                    if ancs:
                        l = [x["label"] for x in ancs]
                        if 'Gnathostomata <vertebrates>' in l:
                            organism_templates.append(sdrf_schema.VERTEBRATES_TEMPLATE)
                        elif 'Metazoa' in l:
                            organism_templates.append(sdrf_schema.NON_VERTEBRATES_TEMPLATE)
                        elif 'Viridiplantae' in l:
                            organism_templates.append(sdrf_schema.PLANTS_TEMPLATE)
                        else:
                            print("WARNING: Could not distinguish {} into the validation schemas".format(o))                            
                else:
                    print("WARNING: Could not retrieve ancestors for: {}".format(o))

    # TODO what about URLS of ontology in data-cells in sdrf?
    # see: https://github.com/bigbio/proteomics-metadata-standard/blob/master/sdrf-proteomics/README.adoc#82-sdrf-proteomics-values
    return organism_templates


def syntax_check_sdrf_from_file(input_file):
    """ Wrapper to check sdrf_struct """
    return syntax_check_sdrf_struct(load_sdrf(input_file))


def syntax_check_sdrf_struct(sdrf_struct):
    """
    Checks the sdrf format with the given validator from sdrf_pipelines

    returns 3 types of errors:
    * Errors based on the default structure (specific columns)
    * Errors based on the MassSpectromentry structure and 
    * Errors based on the species used in sdrf
    """

    # Wrap struct to the SdrfDataFrame
    df = pd.DataFrame(sdrf_struct)
    sdrf_df = sdrf.SdrfDataFrame(df)

    # Get possible schema specific checks
    organism_templates = _get_organism_schema(df)

    # Check Syntax of the sdrf_struct!
    default_errs = sdrf_df.validate(sdrf_schema.DEFAULT_TEMPLATE)
    mass_errs = sdrf_df.validate(sdrf_schema.MASS_SPECTROMETRY)
    orgs_errs = [j for i in organism_templates for j in sdrf_df.validate(i)]
    # TODO DL the order of columns probably matters?

    # return the errors obtained by validation
    return default_errs, mass_errs, orgs_errs
