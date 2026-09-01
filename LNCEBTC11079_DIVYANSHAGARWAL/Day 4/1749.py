class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = 0
        min_sum = 0

        curr_max = 0
        curr_min = 0

        for num in nums:
            curr_max = max(0, curr_max + num)
            curr_min = min(0, curr_min + num)

            max_sum = max(max_sum, curr_max)
            min_sum = min(min_sum, curr_min)

        return max(max_sum, abs(min_sum))