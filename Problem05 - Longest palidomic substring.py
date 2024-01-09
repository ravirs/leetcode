#Problem05 - Longest palidomic substring 
# def expandAroundCenter(left: int, right: int) -> str:
#     while left >= 0 and right < len(s) and s[left] == s[right]:
#         left = left -1
#         right = right +1
#     return s[left + 1:right]

# if not s:
#     return ""

def longestPalindrome(s: str) -> str:
    longest = ""
    for i in range(len(s)):
        # Odd length palindrome
        temp = expandAroundCenter(i, i)
        if len(temp) > len(longest):
            longest = temp
        
        # Even length palindrome   need to pass +1 right pointer
        temp = expandAroundCenter(i, i + 1) 
        if len(temp) > len(longest):
            longest = temp

    return longest

