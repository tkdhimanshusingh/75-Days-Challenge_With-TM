n=len(arr)
        profit,buy,sell=0,arr[0],arr[0]
        for i in range(len(arr)-1):
            if buy>arr[i]:
                buy=arr[i]
            if sell<arr[i]:
                sell=arr[i]
            if arr[i+1]<sell:
                profit+=(sell-buy)
                buy=arr[i+1]
                sell=arr[i+1]
        profit+=arr[-1]-buy
        return(profit)