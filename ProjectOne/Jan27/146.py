#https://leetcode.com/problems/lru-cache/
class Node:
    def __init__(self, key,val):
        self.prev=None
        self.next=None
        self.val=val
        self.key=key
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache=dict()
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head

    def remove(self,node):
        node.prev.next,node.next.prev=node.next,node.prev
    def add(self,n):
        self.tail.prev.next,n.prev,n.next,self.tail.prev=n,self.tail.prev,self.tail,n
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        n=self.cache[key]
        self.remove(n)
        self.add(n)
        return n.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node=Node(key,value)
        self.add(node)
        self.cache[key]=node
        if len(self.cache)>self.capacity:
            #notice dont del node first
            del self.cache[self.head.next.key]
            self.remove(self.head.next)




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)