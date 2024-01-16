# Problem101 : Sysmmetric tree 
# ignore root , trhe lefrt and right are equal 
# recursion
# not identical , but mirror image 

class Solution :
    def symmetrictree(self, root):
        def dfs(left , right):
            if not left and not right:
                return True
            if not left or not right:
                return False
        
            value = (left.val == right.val and 
                 dfs(left.left , right.right) and 
                 dfs(left.right, right.left))
            return value
        
        return dfs(root.left, root.right)
            
