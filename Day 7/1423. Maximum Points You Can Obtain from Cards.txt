class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lb,ub=0,len(cardPoints)-k
        non_win_sum=sum(cardPoints[ub:])
        ans=non_win_sum
        while ub<len(cardPoints):
            non_win_sum=non_win_sum+cardPoints[lb]-cardPoints[ub]
            ans=max(ans,non_win_sum)
            lb+=1
            ub+=1
        return(ans)