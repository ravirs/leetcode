# Problem 3:
# longest substring without repeating characters
# input "abcabcbb"
# output =3

class Solution:
    def lengthoflongesrSubstring(self,s):
        charset = set()
        l =0

        for r in range (len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l=l+1
            charset.add(s[r])
            res = max(res, r-l+1)
        return res



