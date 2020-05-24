#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 14:34:17 2020

@author: wangpeiyu
"""

"""
This question was asked by Riot Games.

Design and implement a HitCounter class that keeps track of requests (or hits). It should support the following 
operations:

    record(timestamp): records a hit that happened at timestamp
    total(): returns the total number of hits recorded
    range(lower, upper): returns the number of hits that occurred between timestamps lower and upper (inclusive)

Follow-up: What if our system has limited memory?

"""
class HintCounter:
    def __init__(self):
        self.hits={}
        self.counts=0
        
    def record(self,timestamp):
        if timestamp not in self.hits:
            self.hits[timestamp]=1
        else:
            self.hits[timestamp]+=1
        self.counts+=1
        
    def total(self):
        return self.counts
    
    def range(self,lower,upper):
        count=0
        for time in self.hits.keys():
            if time>=lower and time<=upper:
                count+=self.hits[time]
        return count
    