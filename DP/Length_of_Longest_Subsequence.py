# Source : https://www.interviewbit.com/problems/length-of-longest-subsequence/
# Given an array of integers, find the length of longest subsequence which is first increasing then decreasing.

# Algo/DS : DP, Bitonic sequence

# Complexity :O(n^2)

class Bitonic:
    # @param A : tuple of integers
    # @return an integer
    def longestSubsequenceLength(self, A):
        
        n = len(A)
        
        increasing_sequence = [1] * n
        
        decreasing_sequence = [1] * n
        
        
        for i in range(1, n):
            
            for j in range(0,i):
                
                if A[i] > A[j] : increasing_sequence[i] = max(increasing_sequence[i], increasing_sequence[j] + 1)

   
        for i in range(n - 2, -1, -1):
            
            for j in range(n - 1,i, -1):
                
                if A[i] > A[j] : decreasing_sequence[i] = max(decreasing_sequence[i], decreasing_sequence[j] + 1)

        res = [i + j for i, j in zip(increasing_sequence, decreasing_sequence)]
        
        return max(res) - 1 if res else 0

def main():
	print Bitonic().longestSubsequenceLength([1 ,3, 5, 6, 4 ,8, 4, 3 ,2, 1])


if __name__ == '__main__':
	main()