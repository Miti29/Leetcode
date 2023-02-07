class Solution {
    boolean ans;
    public boolean isPalindrome(int x) {
        
        String str = Integer.toString(x);
        int n = str.length();
        char c1[] = str.toCharArray();
        for (int i=0; i<str.length();i++){
            if (c1[i]==c1[n-1-i]){ans= true;}
            else
            {ans=false;
            break;}
        }
      return ans;  
    }
}