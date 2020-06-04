#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 19:53:15 2020

@author: wangpeiyu
"""

"""
Leetcode 451. Sort Characters By Frequency

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

"""

class Solution:
    def frequencySort(self, s: str) -> str:
        if not s or len(s)==0 or len(s)<=2:
            return s
        dic={}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]]=1
            else:
                dic[s[i]]+=1
                
        dic={k: v for k, v in sorted(dic.items(), key=lambda item: item[1], reverse=True)}
        new_s=""
        for key in dic.keys():
            new_s+=key*dic[key]
            
        return new_s
    
    
#with built-in counter
        
class Solution:
    def frequencySort(self, s: str) -> str:
        if not s or len(s)==0 or len(s)<=2:
            return s
        counts=collections.Counter(s)
        
        string_builder=[]
        
        for letter, freq in counts.most_common():
            string_builder.append(letter*freq)
            
        return "".join(string_builder)