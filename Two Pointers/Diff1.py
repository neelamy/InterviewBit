# Source : https://www.interviewbit.com/problems/diffk/
# Given an array A of sorted integers and another non negative integer k, 
# find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

# Algo/DS : 2 pointers

# Complexity : O(n)

class Diff:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        
        i = 0 ;j = 0
        
        while i < len(A) and j < len(A):
            
            # if diff is equal to B then return 1
            if A[j] - A[i] == B and i != j : return 1
            
            # if diff is less then move j to next number to increase the diff
            elif A[j] - A[i] < B: j +=1
            
            # if diff is more then there is no need to go further with same i
            # move i to next number to decrease the diff
            else : i += 1
     
        return 0


def main():
	print Diff().diffPossible([1,3,5],4) # 1


if __name__ == '__main__':
	main()