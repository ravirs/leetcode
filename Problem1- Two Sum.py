#Problem1- Two Sum
#nums =[2,5,7,10]   target =9
class Solution:
    def twoSum(self, nums, target):
        prevmap ={}
        for index, num in enumerate(nums):
            difference = target - num
            if difference in prevmap:
                return [prevmap[difference], index]
            prevmap[num] = index
        return 

