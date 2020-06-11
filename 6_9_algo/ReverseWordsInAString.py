#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 13:59:48 2020

@author: wangpeiyu
"""

"""
53. Reverse Words in a String

Given an input string, reverse the string word by word.

Have you met this question in a real interview?  
Clarification
What constitutes a word?
A sequence of non-space characters constitutes a word and some words have punctuation at the end.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.
Example
Example 1:
	Input:  "the sky is blue"
	Output:  "blue is sky the"
	
	Explanation: 
	return a reverse the string word by word.

Example 2:
	Input:  "hello world"
	Output:  "world hello"
	
	Explanation: 
	return a reverse the string word by word.

"""

class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        # write your code here
        if not s or len(s)==0:
            return ""
        if len(s)==1:
            return s
        stack=[]
        l=0
        r=len(s)-1
        while l<len(s) and s[l]==' ' :
            l+=1
        if l==len(s):
            return ''
        while s[r]==' ':
            r-=1

        string=""   
        while l<=r:
            if s[l]==' ':
                stack.append(string)
                string=""
                while s[l]==" " and l<=r:
                    l+=1
            else:
                string+=s[l]
                l+=1
        stack.append(string)        
        new_str=""
        for i in range(len(stack)-1, 0, -1):
            new_str+=stack[i]
            new_str+=" "
        new_str+=stack[0]
        
        return new_str
                    
                
#python built-in
class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        # write your code here
        return ' '.join(reversed(s.strip().split()))