#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 08:36:19 2020

@author: christina
"""
"""
This program tests the ListException class.

Assume the student has completed the implementation of ListException class.

Xiannong Meng
2019-11-15
"""
from ListException import * # import the ListException class

print("--- Test exception ---")
print("We will raise the ListException ...")
try:
    raise ListException("Raise list exception.")
except ListException:
    print("We caught the exception raised.")
except:
    print("Some unknow exception is caught.")
print("--- Passed exception test ---")
