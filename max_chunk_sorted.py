from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        return sum(max(arr[:i+1]) == i for i in range(len(arr)))



s = Solution()
print(s.maxChunksToSorted([4,3,2,1,0]))
print(s.maxChunksToSorted([1,0,2,3,4]))
print(s.maxChunksToSorted([0,1]))