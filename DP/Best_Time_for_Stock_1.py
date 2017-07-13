# Source :https://www.interviewbit.com/problems/best-time-to-buy-and-sell-stocks-i/
# Say you have an array for which the ith element is the price of a given stock on day i.
#If you were only permitted to complete at most one transaction (ie, buy one 
#and sell one share of the stock), design an algorithm to find the maximum profit.

# Algo/DS : DP

# Complexity :O(n)

class BestTimeForStock:

    def maxProfit(self, A):

    	highestPrice, max_profit = 0, 0
        
        for i in range(len(A)-1, -1, -1):

        	highestPrice = max(highestPrice, A[i])

        	max_profit = max(max_profit, highestPrice - A[i])

        return max_profit


def main():
	print BestTimeForStock().maxProfit([4,3,4,5,1 ]) # 2


if __name__ == '__main__':
	main()