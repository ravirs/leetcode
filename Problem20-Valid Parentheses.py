# Problem 20 Valid Parentheses 
class Solution:
    def isValid(self,inputs):
        stack=[]  # python list
        #hashMap in form of dictionary O(n)
        closetoopen ={")":"(","]":"[","}":"{"}

        for charactr in inputs:
            if charactr in closetoopen:
                if stack and stack[-1] == closetoopen[charactr]:
                    stack.pop()
                else:
                    return False
            else:
                # we got open paranethis 
                stack.append(charactr)
        return True if not stack else False
        
                        
        
