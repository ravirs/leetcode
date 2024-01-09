#Problem 2 : Add two Numbers 
#445+333 = 778]\\

class ListNode():
    def __init__(self,val, next) -> None:
        self.val= val 
        self.next= next

class Solution:
    def addtwonumbers(self, l1, l2):
        # two linked list that we need to add 
        dummy = ListNode(-1)
        curr= dummy 
        carry =0

        while l1 and l2 or carry :
            v1= l1.val if l1 else 0
            v2= l2.val if l2 else 0

            # new digit
            val = v1 + v2
            carry = val//10
            val  =val%10
            curr.next = ListNode(val)

            # update pointer
            curr = curr.next 
            l1= l1.next if l1 else 0
            l2= l2.next if l2 else 0

        return dummy.next
