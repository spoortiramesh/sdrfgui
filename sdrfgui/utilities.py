import csv

def save_sdrf(sdrf_struct, output_file):
    """
    Saves the sdrf_struct into the corresponding output file
    """

    # Get all headers 
    # TODO do we want to save in a specific order!
    # then we only need to adjust the headers list
    headers = set()
    for entry in sdrf_struct:
        for key in entry.keys():
            headers.add(key)
    headers = sorted(list(headers))


    # Get all rows to write (including header)
    rows = [headers]
    for entry in sdrf_struct:
        row = []
        for h in headers:
            if h in entry:
                row.append(entry[h])
            else:
                row.append()
        rows.append(row)

    with open(output_file, "w") as out_file:
        writer = csv.writer(out_file, delimiter="\t")
        writer.writerows(rows)
            

def load_sdrf(input_file):
    """
    Loads a sdrf file into the internal sdrf structure

    NOTE: It does not do any checking and can break by exotic sdrfs
    """
    sdrf_struct = []

    with open(input_file, "r") as in_file:
        reader = csv.reader(in_file, delimiter="\t")

        # Read Header
        header = next(reader)

        # Parse Information into dict structure
        for i in reader:
            d = dict()
            for h, j in zip(header, i):
                d[h] = j
            sdrf_struct.append(d)
    
    return sdrf_struct


def get_entries_by_value(sdrf_struct, key, value):
    """
    Returns idcs of matching values by a specified key in sdrf
    """

    match_idcs = []
    for idx, entry in enumerate(sdrf_struct):
        if key in entry:
            if entry[key] == value:
                match_idcs.append(idx)

    return match_idcs
