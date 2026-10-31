class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String,List<String>> map=new HashMap<>();
        for (String word:strs){
            char [] arr= word.toCharArray();
            Arrays.sort(arr);
            String s= new String(arr);
            if(!map.containsKey(s)){
                List<String> newgroup= new ArrayList<>();
                map.put(s,newgroup);
            }
            List<String> group =map.get(s);
            group.add(word);

        }
        return new ArrayList<>(map.values());
        
    }
}
