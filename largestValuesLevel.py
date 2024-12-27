from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        return [max(node.val for node in self.dfs_level(root))]
    
    def dfs_level(self, root): 
        return ([level for level in (([node.left for node in queue if node.left] + [node.right for node in queue if node.right]) for queue in [[root]]) if level] for _ in iter(int, 1))

