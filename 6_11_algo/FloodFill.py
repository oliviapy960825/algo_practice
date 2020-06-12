#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:52:48 2020

@author: wangpeiyu
"""

"""
#151 Medium

Given a 2-D matrix representing an image, a location of a pixel in the screen and a color C, replace the color of the given pixel and all adjacent same colored pixels with C.

For example, given the following matrix, and location pixel of (2, 2), and 'G' for green:

B B W
W W W
W W W
B B B

Becomes

B B G
G G G
G G G
B B B


"""
#bfs
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image or len(image)==0 or len(image[0])==0:
            return image
        if image[sr][sc]==newColor:
            return image
        oldColor=image[sr][sc]
        stack=[(sr,sc)]
        new_matrix=self.dfs(image, oldColor, newColor, stack)
        return new_matrix
    
    def dfs(self, image, oldColor, newColor, stack):
        if not stack:
            return
        while stack:
            (r,c)=stack.pop()
            if image[r][c]==oldColor:
                image[r][c]=newColor
                if r-1>=0:
                    stack.append((r-1, c))
                if r+1<len(image):
                    stack.append((r+1, c))
                if c-1>=0:
                    stack.append((r,c-1))
                if c+1<len(image[0]):
                    stack.append((r, c+1))
        return image
    
    
#dfs
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image or len(image)==0 or len(image[0])==0:
            return image
        if image[sr][sc]==newColor:
            return image
        oldColor=image[sr][sc]
        stack=[(sr,sc)]
        new_matrix=self.dfs(image, sr, sc, oldColor, newColor)
        return new_matrix
    
    def dfs(self, image, r, c, oldColor, newColor):
        if image[r][c]==oldColor:
            image[r][c]=newColor
            if r-1>=0:
                self.dfs(image, r-1, c, oldColor, newColor)
            if r+1<len(image):
                self.dfs(image, r+1, c, oldColor, newColor)
            if c-1>=0:
                self.dfs(image, r, c-1, oldColor, newColor)
            if c+1<len(image[0]):
                self.dfs(image, r, c+1, oldColor, newColor)
        return image    
                
        
        