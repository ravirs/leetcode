# Problem 22: Balanced binary tree
class TreeNode(object):
    def __init__(self, val=0, left=None , right= None):
        self.val = val
        self.right = right 
        self.left = left

class Solution(object):
    def isBalanced(self, root):
        return (self.Height(root)>=0)
    
    def Height(self, root):
        if root is None: 
            return 0
        leftheight= self.Height(root.left)
        rightheight= self.Height(root.right)
        if leftheight ==-1 or rightheight ==-1 or abs(leftheight- rightheight)>1:
            return -1 
        return max(leftheight, rightheight) +1
    
