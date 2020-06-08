#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 14:33:00 2020

@author: wangpeiyu
"""

"""
#145

This problem was asked by Google.

Given the head of a singly linked list, swap every two nodes and return its head.

For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.

"""
#Recursive

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        if not head or not head.next:
            return head
        curr=head
        temp=head.next
        
        curr.next=self.swapPairs(temp.next)
        temp.next=curr
        
        
        return temp
    


#Iterative 
        
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        prev=ListNode()
        curr=head
        head=head.next
        prev.next=curr
        while curr and curr.next:
            temp=curr.next
            prev.next=temp
            curr.next=temp.next
            temp.next=curr
            prev=curr
            curr=curr.next
        
        return head