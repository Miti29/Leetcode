class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        l=0
        u=length-1
        

        while l<=u:
            mid = (l+u)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                u=mid-1
            else:
                l=mid+1
        return -1
        