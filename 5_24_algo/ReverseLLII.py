#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 15:06:34 2020

@author: wangpeiyu
"""

"""
92. Reverse Linked List II

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return head
        cur,prev=head,None
        while m>1:
            prev=cur
            cur=cur.next
            m, n=m-1, n-1
            
        tail, con=cur, prev
        
        while n:
            third=cur.next
            cur.next=prev
            prev=cur
            cur=third
            n-=1
            
        if con:
            con.next=prev
            
        else:
            head=prev
            
        tail.next=cur
        return head
            
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return head
        left=head
        right=head
        stop=False
        def recursion(right,m,n):
            nonlocal left,stop
            if n==1:
                return
            right=right.next
            if m>1:
                left=left.next
                
            recursion(right,m-1,n-1)
            
            if left==right or right.next==left:
                stop=True
                
            if not stop:
                left.val,right.val=right.val,left.val
                
                left=left.next
                
        recursion(right,m,n)
        return head
