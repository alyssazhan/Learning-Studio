"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.visited={}
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        def getCopyNode(node):
            if not node:
                return 
            if node in self.visited:
                return self.visited[node]
            copy=Node(node.val,None,None)
            self.visited[node]=copy
            return copy
        
        if not head:
            return None
        old=head
        new=Node(old.val,None,None)
        self.visited[old]=new
        
        while old:
            new.next=getCopyNode(old.next)
            new.random=getCopyNode(old.random)
            old=old.next
            new=new.next
            
        
        return self.visited[head]
        