class Solution(object):
    def check(self, i, sol):
        if len(i) == 0:
            sol.append(True)
            return sol
        current = i[0] % 2 == 1
        for j in i[1:]:
            if current == True and j % 2 == 0:
                current = False
            elif current == False and j % 2 == 1:
                current = True
            else:
                sol.append(False)
                return sol
        sol.append(True)
        return

    def isArraySpecial(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        sol = []
        for q in queries:
            i = nums[q[0]:q[1]+1]
            self.check(i, sol)
        return sol
                
                    

c = Solution()
print(c.isArraySpecial([4,3,1,6], [[0,2],[2,3]]))