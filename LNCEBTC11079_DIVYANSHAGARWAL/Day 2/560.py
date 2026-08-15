class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr_sum = 0
        mp = {0: 1}

        for i in range(len(nums)):
            curr_sum += nums[i]

            if curr_sum - k in mp:
                count += mp[curr_sum - k]

            if curr_sum in mp:
                mp[curr_sum] += 1
            else:
                mp[curr_sum] = 1

        return count