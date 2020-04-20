#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Parse.py parses data from a .lvm file

__author__ = "Sarah Shinn"
__email__ = "sashinn@ucsd.edu"
__status__ = "Prototype"

import csv


# the Parse class opens a .lvm file and creates a 2-dimensional array of values
class Parse:
    # TODO: fetch .lvm file by "Last Modified" and initialize filename
    def __init__(self, filename):
        self.filename = filename
        # TODO: pass instance variable filename into constructor

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
            data_list = data_block.split('\n')  # create grid rows
            data_list.pop(0)  # remove first blank value
            data_list.pop(len(data_list) - 1)  # remove last blank value
            for row in range(len(data_list)):
                data_list[row] = data_list[row].split('\t')  # create grid cols
                data_list[row].pop(0)  # remove leading blank values
                for col in range(len(data_list[row])):
                    try:
                        data_list[row][col] = float(data_list[row][col])
                    except:
                        pass
        return data_list

