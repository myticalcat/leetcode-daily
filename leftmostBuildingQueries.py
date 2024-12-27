from typing import List
import bisect

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)

        normalized_queries = []
        for i, (a, b) in enumerate(queries):
            if a == b:
                normalized_queries.append((a, a, i, True))
            else:
                if a > b:
                    a, b = b, a
                normalized_queries.append((a, b, i, False))
        normalized_queries.sort(
            key=lambda x: max(heights[x[0]], heights[x[1]]), 
            reverse=True
        )
        
        buildings_sorted = sorted([(h, i) for i, h in enumerate(heights)], 
                                  key=lambda x: x[0],
                                  reverse=True)

        res = [-1] * len(queries)

        active_indices = []
        
        bld_idx = 0
        total_buildings = len(buildings_sorted)

        for (a, b, query_idx, same) in normalized_queries:
            if same:
                res[query_idx] = a
                continue

            X = max(heights[a], heights[b])

            while bld_idx < total_buildings and buildings_sorted[bld_idx][0] > X:
                _, idx = buildings_sorted[bld_idx]
                bisect.insort(active_indices, idx)
                bld_idx += 1

            if heights[b] > heights[a]:
                res[query_idx] = b
                continue

            pos = bisect.bisect_left(active_indices, b+1)
            if pos < len(active_indices):
                res[query_idx] = active_indices[pos]
            else:
                res[query_idx] = -1
        
        return res


s = Solution()
print(s.leftmostBuildingQueries([6,4,8,5,2,7], [[0,1],[0,3],[2,4],[3,4],[2,2]]))
print(s.leftmostBuildingQueries([5,3,8,2,6,1,4,6], [[0,7],[3,5],[5,2],[3,0],[1,6]]))
