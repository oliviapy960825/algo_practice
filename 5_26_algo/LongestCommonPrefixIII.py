#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 22:09:42 2020

@author: wangpeiyu
"""

"""
Lintcode
1159. Longest Common Prefix III

You are given a string array arrarr consisting of nn strings, and a binary query array qq with size k. Each query consists of 2 integers x,y, and answer for the query is the length of the Longest Common Prefix of arr[x]arr[x] and arr[y]arr[y]. You are expected to return a array of size k.

1 \leq n \leq 50001≤n≤5000
1 \leq K \leq 1000001≤K≤100000
length of all stringsLL 1 \leq L \leq 1000001≤L≤100000
string only have lower character

Have you met this question in a real interview?  
Example
input:["aab","aac","aacd"]
[[0,1],[0,2],[1,2]]
output:[2,2,3]
explation:
arr[0] and arr[1] LCP="aa" length=2
arr[0] and arr[2] LCP="aa" length=2
arr[1] and arr[2] LCP="aac" length=3
"""
class TrieNode:
    def __init__(self):
        self.children={}
        self.isEnd=False
    
    def put(self, char):
        self.children[char]=TrieNode()
        
    def getSize(self):
        return len(self.children)
        
class Trie:
    def __init__(self):
        self.root=TrieNode()
        
    def insert(self,word):
        node=self.root
        for i in range(len(word)):
            char=word[i]
            if char in node.children:
                node=node.children[char]
                continue
            else:
                node.children[char]=TrieNode()
                node=node.children[char]
        node.isEnd=True
        
    def searchLCA(self,word):
        node=self.root
        prefix=''
        for i in range(len(word)):
            char=word[i]
            if char in node.children and node.getSize()==1 and not node.isEnd:
                prefix+=char
                node=node.children[char]
            else:
                return prefix
                
        return prefix
    
        
class Solution:
    """
    @param arr: string array
    @param query: query array
    @return: return  LCP ans array
    """
    def queryLCP(self, arr, query):
        # write your code here
        if not arr or not query or len(arr)==0 or len(query)==0:
            return []
        lst=[]
        for pair in query:
            trie=Trie()
            trie.insert(arr[pair[0]])
            lst.append(len(trie.searchLCA(arr[pair[1]])))
            
        return lst
            