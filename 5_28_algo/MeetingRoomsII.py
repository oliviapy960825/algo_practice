#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 23:05:15 2020

@author: wangpeiyu
"""

"""
919. Meeting Rooms II

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Have you met this question in a real interview?  
Example
Example1

Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)
Example2

Input: intervals = [(2,7)]
Output: 1
Explanation: 
Only need one meeting room
"""

"""
Definition of Interval.
"""

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        if not intervals or len(intervals)==0:
            return 0
        if len(intervals)==1:
            return 1
        points=[]
        for m in intervals:
            points.append((m.start,1))
            points.append((m.end,-1))
            
        meeting=0
        room=0
        
        for time,flag in sorted(points):
            meeting+=flag
            room=max(room,meeting)
            
        return room