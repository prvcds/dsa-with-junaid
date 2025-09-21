# https://leetcode.com/problems/missing-number/description/


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        expected_sum = N * (N+1)//2
        current_sum = 0
       
        for i in nums:
            current_sum += i

        return round(expected_sum - current_sum)

