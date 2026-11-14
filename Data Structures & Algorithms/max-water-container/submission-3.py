class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        ans = 0
        while left < right:
            curr_height = min(heights[left], heights[right])
            area = curr_height*(right-left)
            ans = max(area, ans)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return ans