#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 17:41:36 2020

@author: wangpeiyu
"""

"""
1329. Sequence maintenance

There is a sequencea of length n, and there are q operations on the sequence.
Each operation has a queried number bi, subtracting one from all numbers that greater than or equal to bi in the sequence.
Returns how many numbers are subtracted by one after each operation.

1 \leq n, q \leq 10000, 1 \leq a_i, x \leq n1≤n,q≤10000,1≤a
​i
​​ ,x≤n

Have you met this question in a real interview?  
Example
Example1

Input
4
3
[1,2,3,4]
[4,3,1]
Output
[1,2,4]
Example2

Input
3
2
[1,2,3]
[3,3]
Output
[1,0]
"""

#brute force
class Solution:
    """
    @param n: length of sequence
    @param q: Operating frequency
    @param a: the sequence
    @param b: the standard of each operation
    @return: How many numbers are subtracted by one after each operation
    """
    def sequenceMaintenance(self, n, q, a, b):
        # write your code here
        if n==0 or not a:
            return []
        lst=[]
        for o in b:
            count=0
            for num in range(len(a)):
                if a[num]>=o:
                    count+=1
                    a[num]-=1
            lst.append(count)
            
        return lst


#brute force 2:

class Solution:
    """
    @param n: length of sequence
    @param q: Operating frequency
    @param a: the sequence
    @param b: the standard of each operation
    @return: How many numbers are subtracted by one after each operation
    """
    def sequenceMaintenance(self, n, q, a, b):
        # write your code here
        if n==0 or not a:
            return []
        lst=[]
        a.sort(reverse=True)
        for i in b:
            if i>a[0]:
                lst.append(0)
                
            elif i<=a[-1]:
                lst.append(n)
                a=[x-1 for x in a]
                
            else:
                index=0
                while a[index]>=i:
                    a[index]-=1
                    index+=1
                lst.append(index)
        return lst
    
#BS:
class Solution:
    """
    @param n: length of sequence
    @param q: Operating frequency
    @param a: the sequence
    @param b: the standard of each operation
    @return: How many numbers are subtracted by one after each operation
    """
    def sequenceMaintenance(self, n, q, a, b):
        # write your code here
        if n==0 or not a:
            return []
        lst=[]
        a.sort(reverse=True)
        for i in b:
            if i>a[0]:
                lst.append(0)
                
            elif i<=a[-1]:
                lst.append(n)
                a=[x-1 for x in a]
                
            else:
                l=0
                r=len(a)-1
                while l+1<r:
                    mid=l+(r-l)//2
                    if a[mid]<i:
                        r=mid
                    else:
                        l=mid
                if a[r]<i:
                    lst.append(r)
                    for j in range(r):
                        a[j]-=1
                else:
                    lst.append(r+1)
                    for j in range(r+1):
                        a[j]-=1
        return lst
                    
