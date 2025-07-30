'''
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
'''
class Solution:
    def getCount(self, head):
        # code here
        c = 0
        if not head:
            return 0
        curr = head
        while curr:
            c+=1
            curr = curr.next
        return c