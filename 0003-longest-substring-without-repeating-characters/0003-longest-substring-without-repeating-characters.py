class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) == 0: return 0

        #maxbounds will store the lower and upper bounds of a string
        lo, up, maxBounds = 0, 1, (0,1)
        
        #define a set to store values for substring
        used = {s[lo]}

        while up < len(s):
            if s[up] in used:
                #Remove the character at low for a new substring to be formed
                used.remove(s[lo])
                lo += 1
            else:
                used.add(s[up])
                up += 1
            
            #if the lower and bounds are different from the maxbounds, update them each time
            if up - lo > maxBounds[1] - maxBounds[0]:
                maxBounds = (lo, up)

        return maxBounds[1] -  maxBounds[0]
                #s[maxBounds[0]:maxBounds[1]]....if asked to return the longest substring

    