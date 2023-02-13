class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        l = s.split();
        a=l[-1]
        a.rsplit();
        
        return len(a)
        