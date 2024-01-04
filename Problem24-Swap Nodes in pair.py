# Problem 24 : Swap Nodes in pair
# given 'a LL , swap adjacent nodes
# input = [1,2,3,4]
# output = [2,1,4,3]
# Solution can be done iterative or recursive 
# Definition for single LL
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None 

class Solution:
    def swapPairs(self, head):
        """
        input type : ListNode 
        output type : ListNode
        """
        #DummyNode acts as previous Node for head node
        dummy = ListNode(-1)
        dummy.next = head
        prevNode = dummy

        while head and head.next:
            # find Nodes to be swapped 
            first_node = head
            second_node =head.next 

            # Swap them ++ prevnode
            # Draw diagram before and after .Easier to do assignement
            prevNode.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            #Reinitliaised head and prevnode . New virtual list start
            prevNode = first_node
            head = first_node.next

        return dummy.next
    



