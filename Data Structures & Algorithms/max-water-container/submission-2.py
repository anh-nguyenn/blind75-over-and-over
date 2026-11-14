class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        ans = 0
        while left < right:
            curr_height = min(heights[left], heights[right])
            curr_area = (right-left)*curr_height
            if curr_area > ans:
                ans = curr_area
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return ans