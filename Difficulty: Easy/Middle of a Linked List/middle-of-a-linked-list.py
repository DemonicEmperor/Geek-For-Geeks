# your task is to complete this function

'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''
class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def getMiddle(self, head):
        # Code here
        # return the value stored in the middle node
        if not head:
            return 
        curr = head
        c = 0
        while curr:
            c+=1
            curr = curr.next
        m = 0
        curr = head
        while curr:
            m+=1
            if m==(c//2)+1:
                return curr.data
            curr = curr.next
        
            
            