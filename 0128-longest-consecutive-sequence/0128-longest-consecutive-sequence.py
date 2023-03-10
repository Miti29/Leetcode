class Solution(object):
    import heapq
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        stack,temp_list= [],[]
        
        if len(nums) == 0:
            return 0
        
        

        heapq.heapify((nums))
        new_list = []
        while nums:
            new_list.append(heapq.heappop(nums))
            

        print(new_list)


        lo = 1
        used,maxBounds = [],[]
        maxBounds.append(new_list[0])
        used.append(new_list[0])

        while lo < len(new_list):
            if new_list[lo - 1] != new_list[lo]:
                if new_list[lo - 1] + 1 == new_list[lo]:
                    maxBounds.append(new_list[lo])
                    if len(maxBounds) > len(used):
                        used = maxBounds                
                else:
                    maxBounds = []
                    maxBounds.append(new_list[lo])
            lo += 1
        print(used)
        return len(used)
        