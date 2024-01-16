# Problem 704 Binary Search 
# Number and target number , return index 
# nums  =[-1,0,3,5,9] target =9 return =4
class Solution:
    def binarysearch(self, nums, target):
        left  = 0
        right = len(nums)

        while left<=right:
            middle = left +(right-left)/2
            if nums[middle] == target :
                return middle
            elif nums[middle]< target :
                left =middle+1
            elif nums[middle]> target :
                right =middle-1
        return -1
