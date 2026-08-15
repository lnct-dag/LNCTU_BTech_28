class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr_sum = 0
        ans = len(nums) + 1

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum >= target:
                length = right - left + 1

                if length < ans:
                    ans = length

                curr_sum -= nums[left]
                left += 1

        if ans == len(nums) + 1:
            return 0

        return ans