# problem 35 :  Search insert position in sorted 
# return the index if exists 
# if not exist return index it may exist in order 
# rerturn left pointer for solution if not exists 

class Solution:
    def searchInsert(self, nums, target):
        left =0
        right = len(nums)-1

        while left<= right:
            middle = left +(right-left)/2
            if target ==nums[middle]:
                return middle 
            if target > nums[middle]:
                left = left +1
            elif target < nums[middle]:
                right = right -1
        return left
    # left since if you look when while look is not satisfied the left index 
    # is the right place of increment