#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 14:34:54 2020

@author: wangpeiyu
"""

"""
#131 Medium

This question was asked by Snapchat.

Given the head to a singly linked list, where each node also has a “random” pointer that points to anywhere 
in the linked list, deep clone the list.
"""

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        # Dictionary which holds old nodes as keys and new nodes as its values.
        self.visitedHash = {}

    def copyRandomList(self, head):

        if head == None:
            return None

        # If we have already processed the current node, then we simply return the cloned version of it.
        if head in self.visitedHash:
            return self.visitedHash[head]

        # create a new node
        # with the value same as old node.
        node = Node(head.val, None, None)

        # Save this value in the hash map. This is needed since there might be
        # loops during traversal due to randomness of random pointers and this would help us avoid them.
        self.visitedHash[head] = node

        # Recursively copy the remaining linked list starting once from the next pointer and then from the random pointer.
        # Thus we have two independent recursive calls.
        # Finally we update the next and random pointers for the new node created.
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node
    
    

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        new_head=Node(head.val,None,None)
        curr_head=new_head
        nxt=head.next
        
        l={head:new_head}
        while nxt:
            new_nxt=Node(nxt.val,None,None)
            new_head.next=new_nxt
            l[nxt]=new_nxt
            nxt=nxt.next
            new_head=new_nxt
            
        curr=head
        while curr:
            if curr.random:
                l[curr].random=l[curr.random]
                
            curr=curr.next
            
        return curr_head
            