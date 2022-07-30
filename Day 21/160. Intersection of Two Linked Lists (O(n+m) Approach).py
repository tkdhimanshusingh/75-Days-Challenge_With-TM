class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        list1,list2=headA,headB
        while(list1 != list2):
            list1=list1.next if list1 else headB
            list2=list2.next if list2 else headA
        return list1