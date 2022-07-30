class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l=head=ListNode()
        while(list1 and list2):
            if list1.val<list2.val:
                l.next=list1
                list1=list1.next
            else:
                l.next=list2
                list2=list2.next
            l=l.next
        if list1:
            l.next=list1
        elif list2:
            l.next=list2
        return head.next