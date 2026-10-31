class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map={}
        for word in strs:
            templist=list(word)
            templist.sort()
            s=''.join(templist)
            if s not in map:
                arr=[]
                map[s]=arr
            group=map[s]
            group.append(word)
        return list(map.values())
        