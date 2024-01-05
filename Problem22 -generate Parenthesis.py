# problem 22 : generate Parenthesis 
# S is buffer .n is count 
# dfs approach
def generateParenthesis(n):
    def backtrackdfs(S='', left=0, right=0):
        #final condition. when to stop adding 
        if len(S) == 2 * n:
            result.append(S)
            return
        
        #dfs/backtrack call 
        if left < n:
            backtrackdfs(S+'(', left+1, right)
        if right < left:
            backtrackdfs(S+')', left, right+1)

    result = []
    backtrackdfs()
    return result

# Example usage 
n = 3
print(generateParenthesis(n))

"""
In this function, generateParenthesis starts the process, and the backtrack function is used for the recursive generation of parentheses. 
It takes the current string S, and the counts of left and right parentheses used so far.
If the length of S is 2 * n, it means a valid combination is formed and it's added to the result list.
The function then explores further by adding either a '(' or ')' as long as the count of left parentheses 
is less than n and the count of right parentheses is less than the count of left parentheses (to ensure well-formedness).
====
Understanding the Approach
The goal is to generate strings of well-formed parentheses. A well-formed string of parentheses is one where every opening parenthesis '(' has a corresponding closing parenthesis ')', and no closing parenthesis appears before its matching opening parenthesis.

For example, for n = 3, one valid combination is "((()))", where each opening parenthesis is properly matched with a closing one.

Recursive Backtracking
The function uses a technique called recursive backtracking. This is a common approach for generating all possible combinations of a set of choices. In this case, the choices are where to place opening and closing parentheses.

Function Breakdown
Base Function generateParenthesis(n):

n: The number of pairs of parentheses.
It initializes an empty list result, which will store all valid combinations.
It calls the backtrack function to start the process.
Nested Function backtrack(S, left, right):

S: The current state of the string being formed.
left: The number of opening parentheses used so far.
right: The number of closing parentheses used so far.
This function is where the recursive magic happens.
How Backtracking Works
Base Case: If the current string S reaches a length of 2 * n (since each pair has two characters), it means a valid combination is complete. This combination is added to result.

Recursive Calls:

Adding an Opening Parenthesis: If the number of opening parentheses (left) is less than n, it means we can still add an opening parenthesis. We make a recursive call with S+'(', incrementing left by 1.
Adding a Closing Parenthesis: If the number of closing parentheses (right) is less than the number of opening parentheses (left), it means we can add a closing parenthesis (to maintain well-formedness). We make a recursive call with S+')', incrementing right by 1.
Example:
For n = 2, the function works like this:

Start with an empty string S.
Add an opening parenthesis: S = "(".
Since left < n, add another opening parenthesis: S = "((".
Now, right < left, so add a closing parenthesis: S = "(()".
Again, right < left, add another closing parenthesis: S = "(())".
Now S is of length 2 * n, add "(())" to result.
Backtrack and try different combinations.
Through this process, the function explores all valid ways to arrange n
"""