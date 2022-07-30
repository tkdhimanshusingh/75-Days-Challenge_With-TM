class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l=[]
        while(head):
            l.append(head.val)
            head=head.next
        return True if l==l[::-1] else False