#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Parse.py parses data from a .txt file

__author__ = "Sarah Shinn"
__email__ = "sashinn@ucsd.edu"
__status__ = "Prototype"


class Parse:
    #filename = "2019613_.lvm"

    def __init__(self, filename):
        self.filename = filename

    def getDate(self):
        return "6/19/2019"

    def _read(filename):
        file = open(filename, "r")
        data = file.read()
        return data

    def getData(self):
        data = _read(self.filename)
        return data

    def printVar(self):
        print(self.filename)

obj = Parse("2019613_.lvm")
obj.printVar()
print(obj.getDate())
print(obj.getData())


