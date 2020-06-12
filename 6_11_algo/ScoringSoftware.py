#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 17:40:26 2020

@author: wangpeiyu
"""

"""
1331. English Software

Xiao Lin is a representative of the English class in the class. He wants to develop a software to handle the grades of classmates.
Xiao LIn ’s software has a magical feature that can reflect the position of your grades in the class through a percentage. "Classmates with grades exceeding…%".
Suppose this percentage is p, and s score is tested, then p can be calculated by the following formula:
p = (number of people whose score does not exceed s-1) / total number of students in the class * 100%
Please design this software

The score array is given to represent the i-th person to take score[i] points
Give the ask array to represent the score of the i-th individual
Each query will output the corresponding score percentage, no need to output a percent sign
The answer is rounded down（To avoid loss of precision, please calculate multiplication first）

Have you met this question in a real interview?  
Example
Example 1:

Input: score= [100,98,87], ask=[1,2,3]
Output: [66,33,0] 
Explanation:
The first person scored 100 points, more than 66% of students
"""
class Solution:
    """
    @param score: Each student's grades
    @param ask: A series of inquiries
    @return: Find the percentage of each question asked
    """
    def englishSoftware(self, score, ask):
        # write your code here
        if not score or len(score)==0 or not ask or len(ask)==0:
            return []
        vec=dict()
        sortedVec=[]
        for i in range(len(score)):
            vec[i+1]=score[i]
            sortedVec.append({'ind':i,'sco':score[i]})
        sortedVec.sort(key= lambda obj:obj.get('sco'), reverse=False)
        um=dict()
        for i in range(len(sortedVec)):
            um[sortedVec[i]['sco']]=float(i)*100/len(sortedVec)
            
        ans=[]
        for k in ask:
            ans.append(math.floor(um[vec[k]]))
            
        return ans
        