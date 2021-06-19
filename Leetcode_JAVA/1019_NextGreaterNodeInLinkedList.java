/*
Medium
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
    public int[] nextLargerNodes(ListNode head) {
        List<Integer> list = new ArrayList<>();
        ListNode node = head;
        while(node != null){
            list.add(node.val);
            node = node.next;
        }
        int[] res = new int[list.size()];
        Stack<Integer> stack = new Stack<>();
        for(int i = 0; i < list.size(); i++){
            int num = list.get(i);
            while(!stack.isEmpty() && num > list.get(stack.peek())){
                int index = stack.pop();
                res[index] = num;
            }
            stack.push(i);    
        }
        while(!stack.isEmpty()){
            int i = stack.pop();
            res[i] = 0;
        }
        
        return res;
    }
}