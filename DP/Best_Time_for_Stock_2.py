# Source : https://www.interviewbit.com/problems/best-time-to-buy-and-sell-stocks-ii/
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like

# Algo/DS : DP

# Complexity :O(n)

########################### This is correct but lengthy code ###################################
# class Stock:
#     # @param A : tuple of integers
#     # @return an integer
#     def maxProfit(self, A):
        
#         if not A : return 0
        
#         max_profit,temp_profit = 0, 0
        
#         max_price = A[-1]
        
#         for i in range(len(A) -2, -1, -1):
            
#             # if element is bigger than next number then that day stocks should be sold
#             # so make it new max_price, store temp_profit and reset temp_profit to 0
#             if A[i] > A[i + 1]:
                
#                 max_price = A[i]
                
#                 max_profit += temp_profit
                
#                 temp_profit = 0
            
#             # element is less than next so buy stock and calculate profit
#             temp_profit  = max(temp_profit, max_price - A[i])            
        
#         # once all element have been traversed , add remaining temp_profit in max_profit   
#         max_profit += temp_profit
        
#         return max_profit


class Stock:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
               	
       	max_profit = 0

       	for i in range(len(A)-1):

       		if A[i] < A[i + 1]:

       			max_profit += A[i + 1] - A[i]

        return max_profit

def main():
	print Stock().maxProfit([2,4,6,1,8,4]) # 11


if __name__ == '__main__':
	main()