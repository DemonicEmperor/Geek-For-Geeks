#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def searchLinkedList(self, head, x):
        #code here
        if not head:
            return False
        curr = head
        while curr:
            if curr.data == x:
                return True
            curr = curr.next
        return False