#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 18:19:11 2020

@author: wangpeiyu
"""

"""
#150 Hard

This problem was asked by LinkedIn.

Given a list of points, a central point, and an integer k, find the nearest k points 
from the central point.

For example, given the list of points [(0, 0), (5, 4), (3, 1)], the central point (1, 2),
and k = 2, return [(0, 0), (3, 1)].
"""
import heapq
def KNP(lst, cp, k):
    if not lst or len(lst)==0 or k==0:
        return []
    if k>=len(lst):
        return lst
    dist= lambda x, y: (x-cp[0])**2+(y-cp[1])**2
    stack=[]
    for point in lst[:k]:
        stack.append((-dist(*point), point))
    heapq.heapify(stack)
    for point in lst[k:]:
        heapq.heappushpop(stack, (-dist(*point), point))
        
    return [point for _, point in stack]
    