#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Data.py contains default variables for data points

import Parse as from_Parse

__author__ = "Sarah Shinn"
__email__ = "sashinn@ucsd.edu"
__status__ = "Prototype"

class Data:

    def __init__(self):
        self.grid = self.get_data()

    def get_date(self):
        return "2019-06-19"

    def get_data(self):
        lvm_data = from_Parse.Parse("2019613_.lvm")
        grid = lvm_data.parse()
        return grid

Test = Data()
print(Test.get_data())