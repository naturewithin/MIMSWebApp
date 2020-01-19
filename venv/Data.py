#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Data.py contains default variables for data points

import Parse as read_lvm_file
import julian

__author__ = "Sarah Shinn"
__email__ = "sashinn@ucsd.edu"
__status__ = "Prototype"


class Data:
    #### TODO: Fix constructor to use grid properly in functions. This will isolate errors!!

    JULIAN_DATE_IDX = 0
    TEMP_IDX = 1
    WATER_IDX = 2
    N2_IDX = 3
    O2_IDX = 4
    Ar_IDX = 5
    O2_Ar_IDX = 6
    N2_Ar_IDX = 7
    TOTAL_IDX = 8
    DMS_62_IDX = 9
    DMS_47_IDX = 10
    BROMOFORM_173_IDX = 11
    BROMOFORM_171_IDX = 12
    BROMOFORM_175_IDX = 13
    ISOPRENE_67_IDX = 14
    ISOPRENE_68_IDX = 15
    ISOPRENE_53_IDX = 16

    def __init__(self):
        self.grid = self.get_data()

    # check for errors
    def get_data(self):
        lvm_data = read_lvm_file.Parse("2019618_.lvm")
        grid = lvm_data.parse()
        return grid

    def _get_array(self, key):
        grid = self.get_data()
        array = []
        for index in range(len(grid)):
            array.append(self.grid[index][key])
        return array

    def get_julian_date(self):
        return self._get_array(self.JULIAN_DATE_IDX)

    #### TODO: fix julian get_time and get_date (do this manually)
    #    def get_date(self, key):
    #        mjd = self.get_julian_date(key)
    #        dt = julian.from_jd(mjd, fmt='mjd')
    #        print(dt)
    #
    #    def get_time(self, key):
    #        mjd = self.get_julian_date(key)
    #        dt = julian.from_jd(mjd, fmt='mjd')
    #        print(dt)
    #### fix ^^^^^

    def get_temperature(self):
        return self._get_array(self.TEMP_IDX)

    def get_water(self):
        return self._get_array(self.WATER_IDX)

    def get_N2(self):
        return self._get_array(self.N2_IDX)

    def get_O2(self):
        return self._get_array(self.O2_IDX)

    def get_Ar(self):
        return self._get_array(self.Ar_IDX)

    def get_O2_Ar(self):
        return self._get_array(self.O2_Ar_IDX)

    def get_N2_Ar(self):
        return self._get_array( self.N2_Ar_IDX)

    def get_total(self):
        return self._get_array(self.TOTAL_IDX)

    def get_DMS_62(self):
        return self._get_array(self.DMS_62_IDX)

    def get_DMS_47(self):
        return self._get_array(self.DMS_47_IDX)

    def get_bromoform_173(self):
        return self._get_array(self.BROMOFORM_173_IDX)

    def get_bromoform_171(self):
        return self._get_array(self.BROMOFORM_171_IDX)

    def get_bromoform_175(self):
        return self._get_array(self.BROMOFORM_175_IDX)

    def get_isoprene_67(self):
        return self._get_array(self.ISOPRENE_67_IDX)

    def get_isoprene_68(self):
        return self._get_array(self.ISOPRENE_68_IDX)

    def get_isoprene_53(self):
        return self._get_array(self.ISOPRENE_53_IDX)

    Julian_Date = "Julian Date"
    Temperature = "Temperature"
    Water = "Water"
    N2 = "N2"
    O2 = "O2"
    Ar = "Ar"
    O2_Ar = "O2/Ar"
    N2_Ar = "N2/Ar"
    Total = "Total"
    DMS_62 = "DMS 62"
    DMS_47 = "DMS 47"
    Bromoform_173 = "Bromoform 173"
    Bromoform_171 = "Bromoform 171"
    Bromoform_175 = "Bromoform 175"
    Isoprene_67 = "Isoprene 67"
    Isoprene_68 = "Isoprene 68"
    Isoprene_53 = "Isoprene 53"

#### Testing Only
# Test = Data()
# print("1. Temp:", Test.get_temperature(10))
# print("2. Water:", Test.get_water(10))
# print("3. N2:", Test.get_N2(10))
# print("4. O2:", Test.get_O2(10))
# print("5. Ar:", Test.get_Ar(10))
# print("6. O2/Ar:", Test.get_O2_Ar(10))
# print("7. N2/Ar:", Test.get_N2_Ar(10))
# print("8. Total:", Test.get_total(10))
# print("9. DMS_62:", Test.get_DMS_62(10))
# print("10. DMS_47:", Test.get_DMS_47(10))
# print("11. Bromoform_173:", Test.get_bromoform_173(10))
# print("12. Bromoform_171:", Test.get_bromoform_171(10))
# print("13. Bromoform_175:", Test.get_bromoform_175(10))
# print("14. Isoprene_67:", Test.get_isoprene_67(10))
# print("15. Isoprene_68:", Test.get_isoprene_68(10))
# print("16. Isoprene_53:", Test.get_isoprene_53(10))
####
