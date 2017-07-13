# Source : https://www.interviewbit.com/problems/longest-increasing-subsequence/
# Find the longest increasing subsequence of a given sequence / array.

# Algo/DS : DP

# Complexity :O(n^2)

class LongestSubsequence:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        
        n = len(A)
        
        res = [1] * n
        
        for i in range(1, n):
            
            for j in range(0, i):
                
                if A[i] > A[j]:
                    
                    res[i] = max(res[j] + 1, res[i])
                    
        return max(res)


def main():
	print LongestSubsequence().lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) #6


if __name__ == '__main__':
	main()