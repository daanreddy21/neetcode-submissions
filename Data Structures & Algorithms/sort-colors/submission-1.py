class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)

        for i in range(n - 1):
            minin = i

            for j in range(i + 1, n):
                if nums[j] < nums[minin]:
                    minin = j

            temp = nums[i]
            nums[i] = nums[minin]
            nums[minin] = temp

        
        """
        Do not return anything, modify nums in-place instead.
        """
        