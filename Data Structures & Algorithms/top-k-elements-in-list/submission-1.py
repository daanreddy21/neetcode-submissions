class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        lst = []
        for num in nums:
            map[num] = map.get(num, 0) + 1
        for key in map:
            lst.append(map.get(key))
        lst.sort()
        list2 = []
        n = len(lst) - 1
        while k != 0:
            for key, value in map.items():
                if lst[n] == value and key not in list2:
                    list2.append(key)
                    k -= 1
                    n -= 1
                    break
        return list2