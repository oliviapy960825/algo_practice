/*
Hard
*//**
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
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists == null || lists.length == 0)
            return null;
        
        ListNode prev = new ListNode();
        ListNode dummy = prev;
        PriorityQueue<ListNode> pq = new PriorityQueue<>((a, b) -> a.val - b.val);
        for(ListNode n : lists){
            if(n != null)
                pq.offer(n);
        }
        while(!pq.isEmpty()){
            ListNode node = pq.poll();
            dummy.next = node;
            dummy = dummy.next;
            if(node.next != null)
                pq.offer(node.next);
        }
        
        return prev.next;
    }
}