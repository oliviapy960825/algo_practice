#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 11:51:57 2020

@author: wangpeiyu
"""

"""
#148 Medium

This problem was asked by Apple.

Gray code is a binary code where each successive value differ in only one bit,
 as well as when wrapping around. Gray code is common in hardware so that we don't
 see temporary spurious values during transitions.

Given a number of bits n, generate a possible gray code for it.

For example, for n = 2, one gray code would be [00, 01, 11, 10].

"""
class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n==0:
            return [0]
        if n==1:
            return [0,1]
        
        num=0
        lst=[0]
        for i in range(1, 1<<n):
            for j in range(0, 32):
                if (1<<j) & i:
                    num=num^(1<<j)
                    lst.append(num)
                    break
                    
        return lst
                