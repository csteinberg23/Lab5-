#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 08:35:53 2020

@author: christina
"""

"""
This program tests various functionality of an array list
implemented in the arraylist.py.

Assume the student has completed the array list implementation.

Xiannong Meng
2019-11-14
"""

from arraylist import *      # import the array list implementation
from ListException import *  # import the ListException class

def test_constructor():
    '''Test the list constructor. Create and return an empty list.'''

    my_list = List()  # create a new list
    print('A new list is created, its length should be 0 (zero), it is --> ', len(my_list))
    return my_list


def test_insert( my_list ):
    '''Test the insert method that insert a new item into the list.
       Note that the list insert() method defined takes the form
       of insert(self, item, index), i.e., an index must be given.
       the method should handle the invalid index itself, not this
       test program.'''

    items = ['hello', 'how', 'are', 'you', '?'] # some data
    for i in range(len(items)):
        my_list.insert(items[i], i)

    # test insertion at a particular location, other elements should shift
    my_list.insert('world', 1)  

    print('Length of the list should be 6, it is --> ',len(my_list))

    # print the list using the __str__() method
    print("The list content should be ['hello', 'world', 'how', 'are', 'you', '?']")
    print("It is --> ", end = '')
    print(my_list)

    return my_list   # we return the list so other functions can use it.

def test_peek( my_list ):
    '''Test the peek() method on the given list.
       Assume my_list contains proper information and is generated
       by the test_insert() method.'''

    print("The items in the list should be ['hello', 'world', 'how', 'are', 'you', '?'], it is --> [", end = '')
    for i in range(len(my_list)):
        print(my_list.peek(i), ' ', end = '');
    print(']')


def test_delete(my_list):
    '''Test the delete() method. The delete() method takes an index
       as the parameter and removes the item at the index'''

    # delete at normal positions
    my_list.delete(0)
    my_list.delete(1)
    n = len(my_list)
    my_list.delete(n-1)
    
    # print the content of the list
    print("The items in the list should be ['world', 'are', 'you'], it is --> [", end = '')
    for i in range(len(my_list)):
        print(my_list.peek(i), ' ', end = '');
    print(']')

    return my_list

def test_exception( my_list ):
    '''Test various exceptions of the list'''

    # peek exception, testing non-existing index
    try:
        print('Peek at a non-existing location should raise an exception')
        print(my_list.peek(len(my_list) + 2))
    except ListException:
        print("Caught peek error at a wrong index.")
    except:
        print("Other errors not caught by ListException when peek.")

    # delete exception, testing -1
    try:
        print('Deleting at index -1, should cause exception')
        my_list.delete(-1)
    except ListException:
        print("Caught delete error at index -1")
    except:
        print("Other errors not caught by ListException when deleting")

    # delete exception, testing n
    n = len(my_list)   # get an updated list length
    try:
        print('Deleting at index n, should cause exception')
        my_list.delete(n + 2)
    except ListException:
        print("Caught delete error at index n")
    except:
        print("Other errors not caught by ListException when deleting")

def test_arraylist():
    '''Test various operations of the list ADT in array.'''
    print('--- Test the list constructor ---')
    my_list = test_constructor()
    print('--- Passed constructor test ---\n')

    print('--- Test the insert() method ---')
    my_list = test_insert( my_list )
    print('--- Passed insert() test ---\n')

    print('--- Test the peek() method ---')
    test_peek( my_list )
    print('--- Passed peek() test ---\n')

    print('--- Test the delete() method ---')
    my_list = test_delete( my_list )
    print('--- Passed delete() test ---\n')

    print('--- Test the exceptions ---')
    test_exception( my_list )
    print('--- Passed exceptions test ---\n')

# run the tests
test_arraylist()