#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 14:36:36 2020

@author: wangpeiyu
"""

"""
102. Linked List Cycle

Given a linked list, determine if it has a cycle in it.



Have you met this question in a real interview?  
Example
	Example 1:
		Input: 21->10->4->5,  then tail connects to node index 1(value 10).
		Output: true
		
	Example 2:
		Input: 21->10->4->5->null
		Output: false
	
	```
Challenge
Follow up:
Can you solve it without using extra space?
"""

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here
        if not head:
            return False
        if not head.next:
            return False
        p1=head
        p2=head
        while p2.next:
            p2=p2.next.next
            p1=p1.next
            if not p1 or not p2:
                return False
            elif p1==p2:
                return True
        return False