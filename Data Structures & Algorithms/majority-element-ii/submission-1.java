class Solution {
    public List<Integer> majorityElement(int[] nums) {
        List<Integer> arr= new ArrayList<>();
        HashMap<Integer,Integer> map =new HashMap<>();
        if (nums.length <= 2){
            for (int num : nums){
                arr.add(num);
            }
            return arr;
        }
        for (Integer i:nums){
            map.put(i,map.getOrDefault(i,0)+1);
        }
        int n= nums.length/3;
        for (Integer key:map.keySet()){
            if(map.get(key)>n){
                arr.add(key);

            }
        }
        return arr;
        
    }
}