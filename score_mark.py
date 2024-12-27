class Solution(object):
    def findScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        indexed_nums = [(num, idx) for idx, num in enumerate(nums)]
        indexed_nums.sort()
        
        score = 0
        marked = set()
        
        for val, idx in indexed_nums:
            if idx in marked:
                continue
            
            score += val
            marked.add(idx)
            marked.add(idx-1)
            marked.add(idx+1)
        
        return score
    
s = Solution()
print(s.findScore([2,1,3,4,5,2]))

