from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        best = values[0]
        sol = float('-inf')
        
        for j in range(1, len(values)):
            c = best + (values[j] - j)
            sol = max(sol, c)
            best = max(best, values[j] + j)
        
        return sol
    
s = Solution()
print(s.maxScoreSightseeingPair([8,1,5,2,6]))
print(s.maxScoreSightseeingPair([1,2]))

        