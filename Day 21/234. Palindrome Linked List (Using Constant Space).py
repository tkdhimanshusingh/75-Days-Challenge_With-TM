# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        p1=p2=head
        while(p2 and p2.next):
            p1=p1.next
            p2=p2.next.next
        prev=None
        while(p1):
            nxt=p1.next
            p1.next=prev
            prev=p1
            p1=nxt
        
        left,right=head,prev
        while(right):
            if right.val!=left.val:
                return False
            left=left.next
            right=right.next
        return True