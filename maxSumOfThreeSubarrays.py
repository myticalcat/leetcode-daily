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
        pprint(sum_of_k)

s = Solution()
print(s.maxSumOfThreeSubarrays(nums = [1,2,1,2,6,7,5,1], k = 2))
print(s.maxSumOfThreeSubarrays(nums = [1,2,1,2,1,2,1,2,1], k = 2))
