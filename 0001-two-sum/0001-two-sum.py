class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # arr=[]
        # for idx1, i in enumerate(nums):
        #     for idx2, j in enumerate(nums):
        #         if not idx1 == idx2:
        #             if target == i + j:
        #                 arr.append(idx1)
        #                 arr.append(idx2)
        #                 return arr
            
        arr = {}  #value:index
        
        for idx, i in enumerate(nums):
            diff = target - i
            if diff in arr:
                return arr[diff],idx

            arr[i] = idx

                    
                
        
