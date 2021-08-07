/*
Medium
*/

class RandomizedSet {
    Map<Integer, Integer> map;
    List<Integer> list;
    //int count;
    /** Initialize your data structure here. */
    public RandomizedSet() {
        this.map = new HashMap();
        this.list = new ArrayList();
        //this.count = 0;
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    public boolean insert(int val) {
        if(this.map.containsKey(val))
            return false;
        else{
            //this.count++;
            this.map.put(val, this.list.size());
            this.list.add(val);
            return true;
        }
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    public boolean remove(int val) {
        if(!this.map.containsKey(val))
            return false;
        
            int index = this.map.get(val);
            int newVal = list.get(list.size() - 1);
            
            this.map.put(newVal, index);
            this.map.remove(val);
            this.list.set(index, newVal);
            this.list.remove(list.size() - 1);
            //this.count--;
            return true;
        
    }
    
    /** Get a random element from the set. */
    public int getRandom() {
        Random rand = new Random();
        int index = rand.nextInt(list.size());
        return list.get(index);
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */