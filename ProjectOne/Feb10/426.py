"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        first,last=None,None
        def dfs(root):
            nonlocal last, first
            if root:
                dfs(root.left)
                if last:
                    last.right=root
                    root.left=last
                    
                    
                else:
                    first=root
                last=root
                
                dfs(root.right)
        
        dfs(root)
        first.left=last
        last.right=first
        return first
        