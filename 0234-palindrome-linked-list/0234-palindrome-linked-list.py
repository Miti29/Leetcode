# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        l = []
        while head:
            l.append(head.val)
            head = head.next
        
        print(l)

        for i in range(0, len(l)-1):
            if l[i] != l[len(l)-1-i]:
                return False
        return True

        