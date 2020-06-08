#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 14:31:24 2020

@author: wangpeiyu
"""

"""
#147 Hard

Given a list, sort it using this method: reverse(lst, i, j), which reverses lst from i 
to j.
"""
def reverse(lst, i, j):
    lst=lst[:i]+lst[j:(i-1):-1]+lst[j:]
    print(lst)
    return lst
#print(reverse([1,2,3],0,2))
    
def ReverseSort(reverse, lst):
    target=sorted(lst)
    length=len(lst)
    for i in range(length):
        if target[i]==lst[i]:
            continue
        else:
            target_num=target[i]
            index=i
            while index<len(lst) and lst[index]!=target_num:
                index+=1
            if index!=len(lst):
                lst=reverse(lst, i, index)
            print(lst)
    return lst


print(ReverseSort(reverse, [5,7,9,6,3,2]))