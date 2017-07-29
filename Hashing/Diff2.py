# Source : https://www.interviewbit.com/problems/diffk-ii/
# Given an array A of integers and another non negative integer k,
# find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

# Algo/DS : Hashing

# Complexity : O(n)

class Diff2:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
            
        number = {}
        
        for i in A:

        	# check if A[i] - B or A[i] + B is present in dictionary .If yes, return 1 
            if i - B in number or B + i in number : return 1
            
            # add A[i] to dictionary
            number[i] = 1
        

        return 0

def main():
	print Diff2().diffPossible([1,5,3], 2) #1


if __name__ == '__main__':
	main()