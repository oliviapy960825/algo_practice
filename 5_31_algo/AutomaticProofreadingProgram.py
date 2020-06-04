#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 22:23:02 2020

@author: wangpeiyu
"""

"""
Lintcode 1531. Automatic Proofreading Program

There are some words spelt wrong. Please write a program to proofread the spell, and return the right spell.
The rules is listed below:

If three same charactors connected together, it's a wrong spell, delete one of the charators, e.g, ooops -> oopsooops−>oops.
If two pairs of same charactors (AABB) connected together, it's a wrong spell, delete one charactor of the second pair, e.g. helloo -> hellohelloo−>hello.
The rules follow the priority from left to right, e.g. the aabbaabb and bbccbbcc are both wrong spell in aabbccaabbcc, you should fix aabbaabb firstly, so the final result is aabccaabcc.
The length of input string is nn, 1 <= n <= 10^51<=n<=10
​5
​​ .
字符串均由小写字符组成。

Have you met this question in a real interview?  
Example
Sample Input 1:
str = "helloo"

Sample Output 1:
“hello”

"lloo" is a wrong spell, delete 'o'.

Sample Input 2:
str = ”woooow“

Sample Output 2:
“woow”

"oooo" is a wrong spell, delete an 'o' firstly, "ooo" is still wrong, delete an 'o'.
"""

class Solution:
    """
    @param str: The string before proofreading.
    @return: Return the string after proofreading.
    """
    def automaticProofreadingProgram(self, str):
        # Write your code here.
        if not str or len(str)<=2:
            return str
            
        new_str=[]
        for i in str:
            new_str.append(i)
            if len(new_str)>=3:
                if new_str[-1]==new_str[-2] and new_str[-1]==new_str[-3]:
                    new_str.pop()
            if len(new_str)>=4:
                if new_str[-1]==new_str[-2] and new_str[-3]==new_str[-4]:
                    new_str.pop()
                
        return "".join(new_str)
            
        