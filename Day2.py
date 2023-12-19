import numpy as np
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list1 = list(np.arange(0,len(nums)))
        list2 = list(np.arange(0,len(nums)))
        for i in list1 :
            for j in list2 :
                if i == j:
                    break
                else :
                    if nums[i] + nums[j] == target:
                       return (i,j)