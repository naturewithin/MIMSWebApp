#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Parse.py parses data from a .lvm file

__author__ = "Sarah Shinn"
__email__ = "sashinn@ucsd.edu"
__status__ = "Prototype"


# the Parse class opens a .lvm file and creates a 2-dimensional array of values
class Parse:

    # TODO: fetch .lvm file by "Last Modified" and initialize filename
    def __init__(self, filename):
        self.filename = filename
        # TODO: pass instance variable filename into constructor

    def get_date(self):
        return "2019-06-19"

    # TODO: research how to add a try catch block and how to control errors here
    def _read_file(self):
        with open(self.filename, "r") as f:
            data = f.read()
        return data

    def get_data(self):
        data = self._read_file()
        return data

    # parse() takes .lvm input as a string and returns a clean 2-D array of data
    def parse(self):
        data = self.get_data()
        word = 'Comment'
        start_index = data.find(word) + len(word)
        if start_index != -1:
            data_block = data[start_index:]
            grid = data_block.split('\n')  # create grid rows
            grid.pop(0)  # remove first blank value
            grid.pop(len(grid) - 1)  # remove last blank value
            col = 0
            for row in grid:
                grid[col] = row.split('\t')  # create grid columns
                grid[col].pop(0)  # remove leading blank values
                col += 1
        return grid
