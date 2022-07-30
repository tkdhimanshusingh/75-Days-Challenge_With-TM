class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev1=None
        while(l1):
            nxt=l1.next
            l1.next=prev1
            prev1=l1
            l1=nxt
        prev2=None
        while(l2):
            nxt=l2.next
            l2.next=prev2
            prev2=l2
            l2=nxt
        dummy=head=ListNode()
        carry=0
        while(prev1 or prev2 or carry):
            if prev1 and prev2:
                s=prev1.val+prev2.val+carry
                rem=s%10
                dummy.next=ListNode(rem)
                dummy=dummy.next
                carry=s//10
                prev1=prev1.next
                prev2=prev2.next
            elif prev1:
                s=prev1.val+carry
                rem=s%10
                dummy.next=ListNode(rem)
                dummy=dummy.next
                carry=s//10
                prev1=prev1.next
            elif prev2:
                s=prev2.val+carry
                rem=s%10
                dummy.next=ListNode(rem)
                dummy=dummy.next
                carry=s//10
                prev2=prev2.next
            else:
                dummy.next=ListNode(carry)
                dummy=dummy.next
                carry=0
        head=head.next
        prev3=None
        while(head):
            nxt=head.next
            head.next=prev3
            prev3=head
            head=nxt
        return prev3