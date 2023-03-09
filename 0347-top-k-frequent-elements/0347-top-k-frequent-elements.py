class Solution(object):
    
    from heapq import nlargest

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        temp_dict = {}

        for i in nums:
            if i in temp_dict.keys():
                temp_dict[i] = temp_dict[i] + 1
            else:
                temp_dict[i] = 1
        

        res = nlargest(k, temp_dict, key = temp_dict.get)

        return res


        







            

            
