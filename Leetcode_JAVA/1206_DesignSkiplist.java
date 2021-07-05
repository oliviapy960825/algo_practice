/*
Hard
*/

class Skiplist {
    class Node{
        int val;
        Node next;
        Node down;
        public Node(){};
        public Node(int val){
            this.val = val;
        }
        public Node(int val, Node next, Node down){
            this.val = val;
            this.next = next;
            this.down = down;
        }
    }
    
    Node head = new Node(-1);
    Random rand = new Random();
    
    public Skiplist() {
        
    }
    
    public boolean search(int target) {
        Node curr = head;
        while(curr != null){
            while(curr.next != null && curr.next.val < target){
                curr = curr.next;
            }
            if(curr.next != null && curr.next.val == target)
                return true;
            curr = curr.down;
        }
        
        return false;
    }
    
    public void add(int num) {
        Stack<Node> stack = new Stack<>();
        Node curr = head;
        while(curr != null){
            while(curr.next != null && curr.next.val < num){
                curr = curr.next;
            }
            stack.push(curr);
            curr = curr.down;
        }
        
        boolean insert = true;
        Node down = null;
        while(insert && !stack.isEmpty()){
            curr = stack.pop();
            curr.next = new Node(num, curr.next, down);
            down = curr.next;
            insert = rand.nextDouble() < 0.5;
        }
        if(insert)
            head = new Node(-1, null, head);
    }
    
    public boolean erase(int num) {
        Node curr = head;
        while(curr != null){
            while(curr.next != null && curr.next.val < num){
                curr = curr.next;
            }
            if(curr.next != null && curr.next.val == num){
                curr.next = curr.next.next;
                return true;
            }
            curr = curr.down;
        }
        
        return false;
    }
}

/**
 * Your Skiplist object will be instantiated and called as such:
 * Skiplist obj = new Skiplist();
 * boolean param_1 = obj.search(target);
 * obj.add(num);
 * boolean param_3 = obj.erase(num);
 */