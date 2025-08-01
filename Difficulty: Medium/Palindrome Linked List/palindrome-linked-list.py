'''
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
class Solution:
    def isPalindrome(self, head):
        #code here
        l = []
        if not head:
            return True
        curr = head
        while curr:
            l.append(curr.data)
            curr = curr.next
        return l==l[::-1]