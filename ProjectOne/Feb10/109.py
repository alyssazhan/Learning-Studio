# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getSize(node):
            size=0
            while node:
                size+=1
                node=node.next
            return size
        def dfs(l,r):
            nonlocal head
            if l>r:
                return 
            m=(l+r)//2
            left=dfs(l,m-1)        
            node=TreeNode(head.val)
            node.left=left
            head=head.next
            
            node.right=dfs(m+1,r)
            return node
        
        size=getSize(head)
        return dfs(0,size-1)
        