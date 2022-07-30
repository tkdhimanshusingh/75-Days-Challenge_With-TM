class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s=set()
        while(headA or headB):
            if headA==headB:
                return headA
            if (headA in s):
                return headA
            if (headB in s):
                return headB
            if headA:
                s.add(headA)
                headA=headA.next
            if headB:
                s.add(headB)
                headB=headB.next
        return None