# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        
        def calculate(l):
            x=0
            while l:
                x=x*10+l.val
                l=l.next
            return x

        x1=calculate(l1)
        x2=calculate(l2)
        x=x1+x2
        head=ListNode(0)
        if not x:
            return head
        while x:
            x,digit=x//10,x%10
            head.next,head.next.next=ListNode(digit),head.next
        return head.next
        