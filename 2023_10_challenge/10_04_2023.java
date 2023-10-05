class MyHashMap {
    /*
    LeetCode 706
    
    16 ms, faster than 75.56%
    */
    Map<Integer, Integer> _map = new HashMap<>();

    public MyHashMap() {
        
    }
    
    public void put(int key, int value) {
        _map.put(key, value);
    }
    
    public int get(int key) {
        return _map.getOrDefault(key, -1);
    }
    
    public void remove(int key) {
        _map.remove(key);
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */