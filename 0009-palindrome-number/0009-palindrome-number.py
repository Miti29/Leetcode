class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        y = str(x)
        
        for i in range(len(y)/2):
            if y[i] != y[-1-i]:
                return False
            
        return True
        
                
            
        