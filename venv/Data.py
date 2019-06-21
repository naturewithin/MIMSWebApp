#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Data.py contains default variables for data points

__author__ = "Sarah Shinn"
__email__ = "sashinn@ucsd.edu"
__status__ = "Prototype"

class Data:

    lvm_data = Parse("2019613_.lvm")
    grid = lvm_data.parse()
    preint(grid)