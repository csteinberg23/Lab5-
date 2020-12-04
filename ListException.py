#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 08:33:07 2020

@author: christina

Christina Steinberg 
Lab 05 - Section 2 
FileName: ArratList.py 
Professor Dancy 
9/30/20

"""


class ListException(BaseException): #raise exception 
    def __init__(self, message):
        print(message)