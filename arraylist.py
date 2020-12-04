#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 08:27:52 2020

@author: christina
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Christina Steinberg 
Lab 05 - Section 2 
FileName: ArratList.py 
Professor Dancy 
9/30/20
"""

"""
Created on Thu Sep 24 10:20:39 2020

@author: ces051
"""
from array204 import *

class List:
    def __init__(self): #creates an empty list 
        self.capacity = 2 
        self.length = 0 
        self._array = Array(2)
        
    def __len__(self): #returns the size of the list 
        return self.length 
    
    def __str__(self): #returns a string representation of the list 
        s = "[" 
        for i in range(self.length -1):
          s += self._array[i] + ", "
        s += self._array[self.length -1]
        return s + "]"
    
    
    def insert(self, item, index): #inserts an item at the given index 
        if self.capacity == self.length:
            self.capacity *= 2 
            temp = Array(self.capacity)
            for i in len.self._array: 
                temp[i] = self._array[i] 
            self._array = temp 
        if index >= self.length:
            self._array[self.length]= item 
            self.length += 1 
        else:
            if index < 0:
                index = 0 
            for i in range(self.length, index, -1): 
                self._array[i] = self._array[i-1]
            self._array[index] = item
            self.length += 1 
    
    
    def delete(self, index): #removes the item at the given index 
        if index < 0 or index >= self.length: 
            raise ListException("index error")  
        for i in range(index, self.length - 1):
            self._array[i] = self._array[i+1]
        self.length -= 1 
        self._array[self.length] = None
                
    
    def peek(self, index): #returns the item at the given index 
        if index < 0 or index >= self.length: 
            raise ListException("index error")  
        return self._array[index]
                