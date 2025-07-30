'''    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
class Solution:
    def insertAtEnd(self, head, x):
        #code here 
        new_data = Node(x)
        if not head:
            return new_data
        curr = head
        while curr.next:
            curr = curr.next
        curr.next = new_data
        return head