import heapq

class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        def gain(passes, total):
            return (passes + 1)/(total + 1) - passes/total
        
        heap = []
        for passes, total in classes:
            g = -gain(passes, total)
            heapq.heappush(heap, (g, passes, total))
        
        for _ in range(extraStudents):
            g, passes, total = heapq.heappop(heap)
            passes += 1
            total += 1
            g = -gain(passes, total)
            heapq.heappush(heap, (g, passes, total))
        
        total_ratio = 0
        for _, passes, total in heap:
            total_ratio += passes/total
        
        return total_ratio

s = Solution()

print(s.maxAverageRatio([[1,2],[3,5],[2,2]], 2))  # Output: 0.78333
print(s.maxAverageRatio([[2,4],[3,9],[4,5],[2,10]], 4))  # Output: 0.53485