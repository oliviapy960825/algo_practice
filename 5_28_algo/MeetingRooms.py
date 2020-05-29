#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 10:40:28 2020

@author: wangpeiyu
"""

"""
920. Meeting Rooms

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

(0,8),(8,10) is not conflict at 8

Have you met this question in a real interview?  
Example
Example1

Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation: 
(0,30), (5,10) and (0,30),(15,20) will conflict
Example2

Input: intervals = [(5,8),(9,15)]
Output: true
Explanation: 
Two times will not conflict 
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
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        if not intervals or len(intervals)==0:
            return True
        # Write your code here
        intervals.sort(key=lambda x:x.end)
        end=intervals[0].end
        for i in range(1,len(intervals)):
            if intervals[i].start<end:
                return False
            end=max(end, intervals[i].end)
            
                    
        return True