class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp1=temp2=head
        length=0
        while(temp1):
            length+=1
            temp1=temp1.next
        if length==1:
            return
        elif length-n==0:
            head=head.next
            return head
        for _ in range(length-n-1):
            temp2=temp2.next
        temp2.next=temp2.next.next
        return head