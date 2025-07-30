#Your task is to complete this function
#Your function should print the data in one line only

'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    # Function to display the elements of a linked list in same line
    def printList(self, head):
        #code here
        if not head:
            return
        curr = head
        while curr:
            print(curr.data,end =" ")
            curr = curr.next