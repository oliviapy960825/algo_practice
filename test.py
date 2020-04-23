#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 16:38:08 2020

@author: wangpeiyu
"""
"""
a1='11000000 10101000 00000001 00000001'
b='11111111 11111111 11111111 11110000'
a2='11000000 10101000 00000001 00000000'

"""
"""
def BFS(length, matrix,row,col,count):
    while row<length-1 and col<length-1:
        if matrix[row][col+1]==1 and matrix[row+1][col]==1 and matrix[row+1][col+1]==1:
            count+=1
            return BFS(length,matrix,row+1,col+1,count)
        
def max_area(length, matrix):
    count=1
    for i in range(length):
        for j in range(length):
            if matrix[i][j]==1:
                count=max(count,BFS(length,matrix,0,0,1))
    return (count**2)
    
length=3
matrix=[[1,1,0],[1,1,1],[1,1,0]]

print(max_area(length,matrix))

print("{0:b}".format(192))
print("192.68".split("."))
a1='11000000 10101000 00000001 00000001'
b='11111111 11111111 11111111 11110000'
print(1 & 2)
"""

import random
def find_alter(string): 
    stack=[]#using stack to record/memorize the index of '{' and '}'
    index=0 #starting from index 0
    def helper(string,start_index,end_index): #helper function to help decide on the alternative text between '{' and '}'
        middle_string=string[start_index+1:end_index] # we extract the substring between the start and end index
        middle_string=middle_string.split('|') #we split the alternative texts by '|' because each is a viable solution
        rand=random.randint(0,len(middle_string)-1) #generate a random number representing the index of the chosen alternative text
        return middle_string[rand] #we now have chosen the alternative text, and we return it
    while index<len(string):#set stop condition
        if string[index]=='{':
            stack.append(index) #record the index of "{" in stack, and later on when we meet "}" we pop it from stack
            index+=1
        elif string[index]=="}":
            start_index=stack.pop() 
            """
            we meet the first matching "}" for "{", thus we pop the index on top of the stack and extract the substring
            between the start_index and end_index and generate alternative text within it--I use random generator
            """
            end_index=index
            before_string=string[:start_index] #we keep track of the substring before the substring we want to modify
            after_string=string[end_idex+1:]#we keep track of the substring after the substring we want to modify
            middle_string=helper(string,start_index,end_index)#we use the helper function to help modify and decide on the alternative text we want to input in the text
            string=before_string+middle_string+after_string
            index=len(before_string_middle_string)
        else: # we keep increasing the index pointer
            index+=1
    return string
                                
            
string="{I am|I'm} {working on|starting} this {online |}interview. I hope Cortx thinks I am {{very|extremely} qualified|great|awesome}{!|.}"

print(find_alter(string))