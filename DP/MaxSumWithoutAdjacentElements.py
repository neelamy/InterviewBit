# Source : https://www.interviewbit.com/problems/max-sum-without-adjacent-elements/
# Given a 2 * N Grid of numbers, choose numbers such that the sum of the numbers
# is maximum and no two chosen numbers are adjacent horizontally, vertically or diagonally, and return it.

# Algo/DS : DP

# Complexity :O(n)

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, A):
        
        n = len(A[0])
        
        B = [0]* n
        
        # B will store max of each column
        for i in range(0, n):
            
            B[i] = max(A[0][i], A[1][i])

        # res will contain max sum if element A[i] is included    
        res = [0] * n
        
        # if only 2 columns are present then return the max column value
        if n <= 2 : return max(B)
        
        # res[0]= B[0] and res[1]= B[1]
        res[:2] = B[0:2]
        
        # res[2] = res[0] + B[0]
        res[2] = B[2] + B[0]
        
      	# res[i] = B[i] + max(res[i-2], res[i-3])
      	# we do not consider res[i-4], res[i-6], res[i-8] as res[i-2] is max sum considering all those elements
      	# we do not consider res[i-5], res[i-7], res[i-9] as res[i-3] is max sum considering all those elements
        for i in range(3,n):
            
            res[i] = B[i] + max(res[i-2], res[i-3])
            
        return max(res)


def main():
	print Solution().adjacent([[1,2,3,4],[2,3,4,5]]) # 8


if __name__ == '__main__':
	main()