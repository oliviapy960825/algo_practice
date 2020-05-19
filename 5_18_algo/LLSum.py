"""
#127
This problem was asked by Microsoft.

Let's represent an integer in a linked list format by having each node
represent a digit in the number. The nodes make up the number in 
reversed order.

For example, the following linked list:

1 -> 2 -> 3 -> 4 -> 5

is the number 54321.

Given two linked lists in this format, return their sum in the same 
linked list format.

For example, given

9 -> 9

5 -> 2

return 124 (99 + 25) as:

4 -> 2 -> 1

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, node1: ListNode, node2: ListNode) -> ListNode:
        carry=0
        prev=ListNode()
        head=prev
        while node1 or node2:
            num=(node1.val if node1 else 0) +(node2.val if node2 else 0)+carry
            carry=num//10
            num=num%10
            head.next=ListNode(num)
            head=head.next
            if node1:
                node1=node1.next
            if node2:
                node2=node2.next

        if carry==1:
            head.next=ListNode(1)

        return prev.next

#or

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        result_tail = result
        carry = 0
                
        while l1 or l2 or carry:            
            val1  = (l1.val if l1 else 0)
            val2  = (l2.val if l2 else 0)
            carry, out = divmod(val1+val2 + carry, 10)    
                      
            result_tail.next = ListNode(out)
            result_tail = result_tail.next                      
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
               
        return result.next