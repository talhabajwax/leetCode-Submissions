class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest=prices[0]
        great=0
        
        for i in range(0,len(prices)):
            if prices[i]<lowest:
                lowest=prices[i]
            if prices[i]>lowest:
                profit=prices[i]-lowest
                if profit > great:
                    great=profit
        return great

            
            
        