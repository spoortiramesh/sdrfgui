import csv
from collections import defaultdict


def _get_header_list(keyword, key_amount):
    """ Captures and repeats a partial sdrf header """
    part_header = []
    for key, value in key_amount.items():
        if key.startswith(keyword):
            part_header.extend([key]*value)
    return part_header

def _get_remaining_header_list(keyword_list, key_amount):
    """ Captures and repeats a partial sdrf header """
    part_header = []
    for key, value in key_amount.items():
        _found = False
        for keyword in keyword_list:
            if key.startswith(keyword):
                _found = True
        if not _found:
            part_header.extend([key]*value)
    return part_header

def save_sdrf(sdrf_struct, output_file):
    """
    Saves the sdrf_struct into the corresponding output file
    """

    # First unpack the list columns and count how often we need to repeat one
    # TODO own function, since it might also be needed by the gui itself?
    key_amount_map = defaultdict(lambda: 0)
    for entry in sdrf_struct:
        for key, value in entry.items():
            if type(value) is list:
                key_amount_map[key] = max(key_amount_map[key], len(value))
            else:
                key_amount_map[key] = max(key_amount_map[key], 1)
    
    # Generate header
    # The order matters!
    header_order = ["characteristics","material type","factor value","assay name","comment","technology type","factor value"]
    headers_ordered = [sorted(_get_header_list(x, key_amount_map)) for x in header_order]
    remaining_headers = sorted(_get_remaining_header_list(header_order, key_amount_map))
    sdrf_header =  [*[y for x in headers_ordered for y in x], *remaining_headers]

    # Get all rows to write (including header)
    rows = [sdrf_header]
    for entry in sdrf_struct:
        index = 0
        row = []
        for h in sdrf_header:
            if h in entry:
                if type(entry[h]) == list:
                    if len(entry[h]) < index:
                        row.append("not available (SDRFGUI)") # TODO Can this case happen and if so what to add?
                    else:
                        row.append(entry[h][index])
                        index +=1
                else:
                    row.append(entry[h])
            else:
                row.append("not available SDRFGUI)") # TODO Can this case happen and if so what to add?
        rows.append(row)

    #  TODO Maybe up to this point a list of lists is returned which may be usefull for the GUI itself!
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
                if h not in d:
                    d[h] = j
                else:
                    if type(d[h]) == list:
                        d[h].append(j)
                    else:
                        d[h] = [d[h], j]
            sdrf_struct.append(d)
    
    return sdrf_struct


def get_entries_by_value(sdrf_struct, key, value, _compare_func=lambda x,y: x==y):
    """
    Returns idcs of matching values by a specified key in sdrf
    """
    match_idcs = []
    for idx, entry in enumerate(sdrf_struct):
        if key in entry:
            if type(entry[key]) == list:
                for e in entry[key]:
                    if _compare_func(e, value):
                        match_idcs.append(idx)
                        break
            else:
                if _compare_func(entry[key], value):
                    match_idcs.append(idx)

    return match_idcs
