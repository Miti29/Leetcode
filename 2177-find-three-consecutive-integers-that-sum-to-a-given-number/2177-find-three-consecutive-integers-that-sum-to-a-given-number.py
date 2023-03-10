class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        li =[]

        n = (num//3)

        n -= 1

        if 3*n + 3 == num:
            li.append(n)
            li.append(n+1)
            li.append(n+2)
            return li