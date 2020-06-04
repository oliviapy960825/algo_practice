#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 20:28:40 2020

@author: wangpeiyu
"""

"""
Lintcode 104. Merge K Sorted List

Merge k sorted linked lists and return it as one sorted list.

Analyze and describe its complexity.

Have you met this question in a real interview?  
Example
Example 1:
	Input:   [2->4->null,null,-1->null]
	Output:  -1->2->4->null

Example 2:
	Input: [2->6->null,5->null,7->null]
	Output:  2->5->6->7->null
	
"""

import heapq
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
ListNode.__lt__ = lambda x, y: (x.val < y.val)
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        if not lists:
            return None
            
        if len(lists)==1:
            return lists[0]
            
        dummy=ListNode(0)
        tail=dummy
        heap=[]
        for head in lists:
            if head:
                heapq.heappush(heap, head)
                
        while heap:
            head=heapq.heappop(heap)
            tail.next=head
            tail=head
            if head.next:
                heapq.heappush(heap, head.next)
                
        return dummy.next
            
            

