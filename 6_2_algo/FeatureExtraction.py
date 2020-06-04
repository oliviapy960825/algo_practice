#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 16:51:27 2020

@author: wangpeiyu
"""

"""
Lintcode 1135. Feature extraction

Xiao Ming wants to dig up some cat movement information from the cat video. In order to extract motion information, he needs to extract "cat features" from each frame of the video.
The characteristic of a cat is a two-dimensional vector <x, y>. If x_1 = x_2 and y_1 = y_2, then these two are the same feature.
If the characteristics of the kitty are consistent, it can be considered that the kitty is in motion. That is, if features <a, b> appear in continuous frames, then it will constitute feature motion. For example, feature <a, b> appears in the 2/3/4/7/8 frame, then the feature will form two feature motions 2-3-4 and 7-8.
Now, given the features of each frame, the number of features may be different. Xiaoming expects to find the longest characteristic movement.

Each line represents a frame. Among them, the first number is the number of features of the frame, and the next two numbers are a pair of <x, y>
The total number of features does not exceed 10^5

Have you met this question in a real interview?  
Example
Example 1:

Input: 
features:
[[2,1,1,2,2],
[2,1,1,1,4],
[2,1,1,2,2],
[2,2,2,1,4],
[0],
[0],
[1,1,1],
[1,1,1]]
Output: 3
Explanation:Feature <1,1> appears three times in a row in consecutive frames. Compared with other features, the 
"""
class Solution:
    """
    @param frames: A series of frames
    @return: Find the longest feature movement
    """
    def FeatureExtraction(self, frames):
        # write your code here
        if not frames or len(frames)==0 or len(frames[0])==0:
            return 0
        preTime={}
        curTime={}
        count=0
        for i in range(len(frames)):
            for j in range(frames[i][0]):
                k=(frames[i][j*2+1], frames[i][j*2+2])
                if k in preTime:
                    curTime[k]=preTime[k]+1
                    
                else:
                    curTime[k]=1
                    
                count=max(count, curTime[k])
                
            preTime.clear()
            preTime=curTime.copy()
            curTime.clear()
            
        return count
            