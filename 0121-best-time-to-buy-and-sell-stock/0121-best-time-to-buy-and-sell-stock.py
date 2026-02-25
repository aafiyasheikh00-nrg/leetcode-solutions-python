class Solution(object):
    def maxProfit(self, prices):
        b,s=0,1 # b= buy; s= sell
        maxP=0

        while s<len(prices):
            if prices[b]<prices[s]:
                profit=prices[s]-prices[b]
                maxP=max(maxP,profit) #maximum i.e max from (maxP and profit)
            else:
                b=s #if buy price is more then we move to next (to s) so we                     also increment s by 1
            s=s+1
        return maxP
            
        