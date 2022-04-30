class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        mx_horizontal_diff=horizontalCuts[0]
        mx_vertical_diff=verticalCuts[0]
        for i in range(1,len(horizontalCuts)):
            mx_horizontal_diff=max(mx_horizontal_diff,horizontalCuts[i]-horizontalCuts[i-1])
        for i in range(1,len(verticalCuts)):
            mx_vertical_diff=max(mx_vertical_diff,verticalCuts[i]-verticalCuts[i-1])
        mx_horizontal_diff=max(mx_horizontal_diff,h-horizontalCuts[-1])
        mx_vertical_diff=max(mx_vertical_diff,w-verticalCuts[-1])
        return (mx_horizontal_diff*mx_vertical_diff)%(10**9+7)