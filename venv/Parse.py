#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Parse.py parses data from a .lvm file

import csv
from io import StringIO

__author__ = "Sarah Shinn"
__email__ = "sashinn@ucsd.edu"
__status__ = "Prototype"


class Parse:
    def __init__(self, filename):
        self.filename = filename

    def get_date(self):
        return "2019-06-19"

    def _read_file(self):
        with open(self.filename, "r") as f:
            data = f.read()
        return data

    def get_data(self):
        data = self._read_file()
        return data
    def print_var(self):
        print(self.filename)

    def parse(self):
        data = self.get_data()
        word = 'Comment'
        start_index = data.find(word) + len(word)

        if start_index != -1:
            print(start_index)
            data_block = data[start_index:]
            # print(data_block)

            grid = data_block.split('\n')
            grid.pop(0)
            grid.pop(len(grid) - 1)
            col = 0
            for row in grid:
                grid[col] = row.split('\t')
                grid[col].pop(0)
                col += 1
            print(grid)

# next step: create constants for measurement types and sort data
# prep data to be ready for Data.py

obj = Parse("2019613_.lvm")
# obj.print_var()
# print(obj.get_date())
# print(obj.get_data())
obj.parse()
