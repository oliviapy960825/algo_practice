/*
Hard
*/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverse(ListNode head, int k){
        ListNode prev = null;
        while(k > 0){
            ListNode temp = head.next;
            head.next = prev;
            prev = head;
            head = temp;
            k--;
        }
        return prev;
    }
    
    
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode curr = head;
        int count = k;
        while(curr != null && count > 0){
            curr = curr.next;
            count--;
        }
        if(count == 0){
            ListNode reversedHead = reverse(head, k);
            head.next = reverseKGroup(curr, k);
            return reversedHead;
        }
        
        return head;
    }
}