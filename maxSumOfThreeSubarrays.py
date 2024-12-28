from typing import List
from pprint import pprint

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        sum_of_k = {}
        curr = sum(nums[0:k])
        sum_of_k[0] = curr

        for i in range(1, len(nums)-k+1):
            curr = curr - nums[i-1] + nums[i+k-1]
            sum_of_k[i] = curr

        dp1 = {}
        idx = {}

        curr_max = sum_of_k[0]
        curr_idx = 0

        for i in range(len(nums)-k+1):
            if sum_of_k[i] > curr_max:
                curr_max = sum_of_k[i]
                curr_idx = i
            dp1[i] = curr_max
            idx[i] = curr_idx
        
        dp2 = {}
        id2 = {}
        for i in range(k, len(nums)-k+1):
            curr_max = dp1[i-k] + sum_of_k[i]
            curr_idx = (idx[i-k], i)
            
            if i > k and curr_max < dp2[i-1]:
                curr_max = dp2[i-1]
                curr_idx = id2[i-1]

            dp2[i] = curr_max
            id2[i] = curr_idx

        dp3 = {}
        id3 = {}

        res = []
        max_sum = 0

        for i in range(k + k, len (nums)-k+1):
            curr_max = dp2[i - k] + sum_of_k[i]
            curr_idx = id2[i-k] + (i,)

            if i > (k+k) and curr_max < dp3[i-1]:
                curr_max = dp2[i-1]
                curr_idx = id2[i-1]

            dp3[i] = curr_max
            id3[i] = curr_idx
            
            if max_sum < curr_max:
                max_sum = curr_max
                res = list(curr_idx)
        
        return res





s = Solution()
print(s.maxSumOfThreeSubarrays(nums = [1,2,1,2,6,7,5,1], k = 2))
print(s.maxSumOfThreeSubarrays(nums = [1,2,1,2,1,2,1,2,1], k = 2))
