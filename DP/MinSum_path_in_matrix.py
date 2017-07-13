# Source : https://www.interviewbit.com/problems/min-sum-path-in-matrix/
# Given a m x n grid filled with non-negative numbers, find a path from top left 
# to bottom right which minimizes the sum of all numbers along its path.

# Algo/DS : DP

# Complexity :O(n^2)

class minPathMatrix:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, A):
        
        r = len(A)
        
        c = len(A[0])
        
        for i in range(1, r):
            
            A[i][0] = A[i-1][0] + A[i][0]
            
        for i in range(1,c):
            
            A[0][i] = A[0][i-1] + A[0][i]
            
        for i in range(1, r):
            
            for j in range(1, c):
                
                A[i][j] = A[i][j] + min(A[i-1][j],A[i][j-1])
                
        return A[r-1][c-1]

def main():
	print minPathMatrix().minPathSum([[1,3,2],[4,3,1],[5,6,1]]) # 8


if __name__ == '__main__':
	main()