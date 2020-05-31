#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 13:55:17 2020

@author: wangpeiyu
"""

"""
Lintcode 1145. Associated query

Given an employee table datalist1, store the employee ID and the employee name.

Given an employee hours table datalist2, store the employee ID, month, and hour.

Calculate the monthly working hours and total working hours of each employee from January to march.

Input description:

[[employee ID, employee name],[employee ID, employee name],...]

[[employee ID, month, hour, month, hour, month, hour],[employee ID, month, hour, month, hour, month, hour],...]

Output description:

[[employee name, January hours, February hours, march hours, total hours],[employee name, January hours, February hours, march hours, total hours],...]

The relevant data are presented in the two tables from small to large according to the employee ID, and the data in the returned table should also be arranged from small to large according to the employee ID.

Have you met this question in a real interview?  
Example
Input: 
[["1","zhangwei01"]]
[["1","01","200","02","150","03","196"]]
Output: 
[["zhangwei01","200","150","196","546"]]
"""
class Solution:
    """
    @param datalist1: a list represents the employee table
    @param datalist2: a list represents the employee hours table
    @return: Returns a list of strings represents the datalist3
    """
    def getList(self, datalist1, datalist2):
        # write your code here
        datalist3=[]
        n=len(datalist1)
        for i in range(n):
            datalist3.append([datalist1[i][1]])
            sum=0
            for j in range(2,7,2):
                datalist3[i].append(datalist2[i][j])
                sum+=int(datalist2[i][j])
                
            datalist3[i].append(str(sum))
            
        return datalist3