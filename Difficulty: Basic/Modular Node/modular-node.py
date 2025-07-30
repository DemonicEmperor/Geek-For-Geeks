'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def modularNode(self, head, k):
        # Code Here
        if not head:
            return -1
        c = 0
        m = -1
        curr = head
        while curr:
            c+=1
            if c%k==0:
                m = curr.data
            curr = curr.next
        return m
        