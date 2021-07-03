/*
Medium
*/

class Solution {
    public ListNode reverse(ListNode head){
        if(head == null || head.next == null)
            return head;
        ListNode curr = head;
        while(head.next != null){
            ListNode p = head.next;
            head.next = p.next;
            p.next = curr;
            curr = p;   
        }
        return curr;
    }
    
    public void reorderList(ListNode head) {
        ListNode slow = head, fast = head;
        while(fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode curr2 = reverse(slow);
        ListNode curr1 = head;
        
        while(curr1 != null && curr2 != null){
            
            ListNode temp1 = curr1.next;
            ListNode temp2 = curr2.next;
            curr1.next = curr2;
            curr2.next = temp1;
            curr1 = temp1;
            curr2 = temp2;
            
            /*
            ListNode temp1 = curr1.next;
            curr1.next = curr2;
            curr1 = temp1;

            ListNode temp2 = curr2.next;
            curr2.next = curr1;
            curr2 = temp2;
            */
        }
        
        if(curr1 != null)
            curr1.next = null;
    }
}