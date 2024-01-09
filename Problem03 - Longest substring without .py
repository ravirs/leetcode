#Problem 03 - Longest substring without repeating characers


class Solution:
    def longestsubstring(self, s):
        charset = set()
        left =0
        right =0
        result =0
        for right in range(len(s)):
            while s[right] in charset:
                charset.remove[s[left]]
                left = left +1
            charset.add(s[right])
            result =max(result , right- left +1)
        return result 

