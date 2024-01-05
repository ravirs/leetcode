#Problem19- Remove Nth Node from End of list
# head =[1,2,3,4,5]  n=2
# output =[1,2,3,5]
# two pointer problem 
class ListNode:
    def __init__(self,val=0, next=None)
        self.val = val
        self.next = next

class Solution:
    def removeNthfromend(self, head, n):
        dummy = ListNode(0)
        left = dummy
        right = head

        # push right pointer ahead by n 
        #then iterate next till null
        while n > 0 and right:
            right = right.next
            n = n-1
        while right:
            left = left.next
            right = right.next
        
        #delete 
        left.next = left.next.next 
        return dummy.next
        
        

        
    
