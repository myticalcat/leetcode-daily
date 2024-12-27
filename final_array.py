class Solution(object):
    def getFinalState(self, nums: list, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """

        for i in range(k):
            nums[nums.index(min(nums))] *= multiplier
        return nums

        

sol = Solution()
print(sol.getFinalState([2,1,3,5,6], k = 5, multiplier = 2))