class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # at every position, anser: what is min and max product ending at this index

        ans = nums[0]
        min_product, max_product = nums[0], nums[0]
        for val in nums[1:]:
            curr_max = max(val, min_product*val, max_product*val)
            curr_min = min(val, min_product*val, max_product*val)
            max_product = curr_max
            min_product = curr_min
            ans = max(ans, max_product)
        return ans