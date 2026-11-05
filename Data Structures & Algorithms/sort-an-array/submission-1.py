class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n - 1):
            minin = i

            for j in range(i + 1, n):
                if nums[j] < nums[minin]:
                    minin = j

            temp = nums[i]
            nums[i] = nums[minin]
            nums[minin] = temp

        return nums
        