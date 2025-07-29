#Your task is to complete this function
#Your function should return the new head pointer
'''
class node:
    def __init__(self,x):
        self.data = x
        self.next = None
'''

class Solution:
    def deleteK(self, head, k):
        #code here  
        if not head:
            return 
        c = 1
        prev = head
        curr = head.next
        
        while curr:
            c+=1
            if c%k==0:
                prev.next = curr.next
    
            prev = curr
            curr = curr.next
            
        return head
                