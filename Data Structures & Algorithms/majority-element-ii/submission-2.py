class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        arr=[]
        map={}
        if len(nums) <= 2:
            return list(nums)
        for num in nums:
            map[num]= map.get(num, 0) + 1
        for key, value in map.items():
            if value > len(nums) // 3:
                arr.append(key)
        return arr
        


        