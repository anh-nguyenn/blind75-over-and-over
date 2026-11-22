class Solution:
    def findMin(self, nums: List[int]) -> int:
        # at every position, find which side is sorted of the array
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left+right) // 2
            if nums[mid] > nums[right]: # left side is sorted
                left = mid + 1
            else:
                right = mid
        return nums[left]