"""
problem 23 :  merge K  sorted Lists
Given a arry of K linked list of lists 
each in ascending order , merge thme 
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val =val
        self.next = next

class Soultion:
    def mergeKLists(self, lists):
        if not lists: return None
        if len(lists)==1: return lists[0]

        output = lists[0]
        for l in lists[1:]:
            output = merge2LL(output,l)
        return output 
    
    def merge2LL(l1,l2):
        dummy = curr = ListNode(0)
        while l1 and l2:
            if l1.val <l2.val:
                curr.next = ListNode(l1.val)
                l1 = l1.next
            else:
                curr.next = ListNode(l2.val)
                l2=l2.next
            curr = curr.next
            

