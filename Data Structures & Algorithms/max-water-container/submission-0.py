
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        i = 0
        j = len(height) - 1
        while i != j:
            min_height = min(height[i], height[j])
            out = min_height * (j - i)
            max_area = max(out, max_area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area
        