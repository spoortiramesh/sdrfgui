class Model():

    def __init__(self):
        self.sdrf_struct = []  # The data which we display on the preview (and modify)
        self.marked_entry = None  # The marked entry from the preview below (needed e.g. to delete or modify it)
        self.last_added_entry = None  # The last entry which was added to the sdrf_struct
        self.selected_section = None  # The template which was selected (--> in order to display mandatory and optional fields)


    def get_sdrf_struct(self):
        return self.sdrf_struct


    def set_sdrf_struct(self, sdrf_struct):
        self.sdrf_struct = sdrf_struct

    # Test

