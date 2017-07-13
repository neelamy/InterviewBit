# Source : https://www.interviewbit.com/problems/highest-product/
# Given an array of integers, return the highest product possible by multiplying 3 numbers from the array

# Algo/DS : Greedy

# Complexity :O(n lg n)

class MaxProduct:
    # @param A : list of integers
    # @return an integer
    def maxp3(self, A):
        
        if len(A) < 3 : return 0
        
        A = sorted(A)
        
        # highest product is max of (case 1 and case 2):
        # case 1 : Top 3 elements so product of last 3 number
        # case 2 : 1 +ve and 2 -ve numbers so take largest + ve and 2 -ve numbers which has max magnitude
        #          when A is sorted it would be A[0] and A[-1] 
        return max(A[-1] * A[-2] * A[-3], A[-1] * A[0] * A[1])
        
 

def main():
	print MaxProduct().maxp3([0,-1,3,100,-70,-50]) # 350000


if __name__ == '__main__':
	main()