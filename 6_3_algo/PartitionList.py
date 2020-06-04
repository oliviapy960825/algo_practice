#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 15:36:22 2020

@author: wangpeiyu
"""

"""
This problem was asked by Amazon.

Given a pivot x, and a list lst, partition the list into three parts.

    The first part contains all elements in lst that are less than x
    The second part contains all elements in lst that are equal to x
    The third part contains all elements in lst that are larger than x

Ordering within a part can be arbitrary.

For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be [9, 3, 5, 10, 10, 12, 14].

"""
from collections import deque
def PartitionList(lst, pivot):
    new_lst=deque()
    new_lst.append(pivot)
    index=0
    for i in lst:
        if i<pivot:
            new_lst.appendleft(i)
            index+=1
        elif i==pivot:
            new_lst.insert(index, i)
        elif i>pivot:
            new_lst.append(i)
            
    return new_lst


print(PartitionList([9, 12, 3, 5, 14, 10, 10],10))


"""
The following pseudocode for three-way partitioning assumes zero-based array indexing. It uses three indices i, j and k, maintaining the invariant that i ≤ j ≤ k.

    Entries from 0 up to (but not including) i are values less than mid,
    entries from i up to (but not including) j are values equal to mid,
    entries from j up to (but not including) k are values not yet sorted, and
    entries from k to the end of the array are values greater than mid.

procedure three-way-partition(A : array of values, mid : value):
    i ← 0
    j ← 0
    k ← size of A

    while j < k:
        if A[j] < mid:
            swap A[i] and A[j]
            i ← i + 1
            j ← j + 1
        else if A[j] > mid:
            k ← k - 1
            swap A[j] and A[k]
        else:
            j ← j + 1

https://en.m.wikipedia.org/wiki/Dutch_national_flag_problem
"""