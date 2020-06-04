#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 18:21:28 2020

@author: wangpeiyu
"""

"""
#141 Hard 
This problem was asked by Microsoft.

Implement 3 stacks using a single list:

class Stack:
    def __init__(self):
        self.list = []

    def pop(self, stack_number):
        pass

    def push(self, item, stack_number):
        pass

"""

class Stack:
    def __init__(self,size):
        self.lst = [None]*3*size
        self.size=size
        self.top=[0,0,0]

    def pop(self, stack_number):
        if stack_number>=0 and stack_number<3:
            temp=self.lst[self.top[stack_number]]
            self.lst[self.top[stack_number]]=None
            self.top[stack_number]-=1
            return temp
    def push(self, item, stack_number):
        if stack_number>=0 and stack_number<3:
            self.lst[self.top[stack_number]]=item
            self.top[stack_number]+=1
            
