#User function Template for python3

'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
def displayList(head):
    #code here
    l = []
    if not head:
        return l
    
    curr = head
    while curr:
        l.append(curr.data)
        curr = curr.next
    return l
        
        
        