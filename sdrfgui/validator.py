from sdrf_pipelines.zooma import ols
from sdrf_pipelines.sdrf import sdrf, sdrf_schema
from utilities import load_sdrf
import pandas as pd


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

    # Check Syntax of the sdrf_struct!
    default_errs = sdrf_df.validate(sdrf_schema.DEFAULT_TEMPLATE)
    mass_errs = sdrf_df.validate(sdrf_schema.MASS_SPECTROMETRY)
    orgs_errs = [] # TODO DL!
    # TODO we need to validate depending on the scheemas and organism used in SDRF (e.g. Human/Vertibrates/etc..)
    # TODO DL the order of columns probably matters?

    # return the errors obtained by validation
    return default_errs, mass_errs, orgs_errs