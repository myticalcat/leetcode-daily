
from typing import List
from pprint import pprint

class Solution:
    def findTargetSumWays(self, nums, target):
        from collections import defaultdict
        table = defaultdict(lambda: 0)
        table[0] = 1
        for i in  nums:
            new_table = defaultdict(lambda: 0)
            for j in table:
                new_table[j + i] += table[j]
                new_table[j - i] += table[j]
            table = new_table
        return table[target]

    

s = Solution()
print(s.findTargetSumWays(nums = [1,1,1,1,1], target = 3))
print(s.findTargetSumWays(nums = [1], target = 1))
                
