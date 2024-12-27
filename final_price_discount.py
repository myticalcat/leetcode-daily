class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        return [p - list(filter(lambda x: x <= p, prices[i+1:]))[:1][0] if list(filter(lambda x: x <= p, prices[i+1:])) else p for i, p in enumerate(prices)]
    
s = Solution()
print(s.finalPrices([8,4,6,2,3]))
print(s.finalPrices([1,2,3,4,5]))
print(s.finalPrices([10,1,1,6]))