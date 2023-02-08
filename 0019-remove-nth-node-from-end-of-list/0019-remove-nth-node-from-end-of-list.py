# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count1 = 0
        count2 = 0
        n1 = head
        while (n1):
            n1= n1.next
            count1+=1
        
        if count1==1:
            return None
        
#Take 2 pointers, n3,temp
#assign n3 to second node and temp to first node, now make n3(second node) as head
        n3=head
        if count1==n:
            temp=head
            n3 = n3.next
            head = n3         #making second node as head 
        
        n2=head
        while (n2):
            count2 +=1  
            if count2 == count1-n:
                n2.next = n2.next.next
            else:
                n2 = n2.next
        return head 
            
               
      
        