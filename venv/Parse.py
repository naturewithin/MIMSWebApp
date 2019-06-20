#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Parse.py parses data from a .txt file

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


obj = Parse("2019613_.lvm")
obj.print_var()
print(obj.get_date())
print(obj.get_data())