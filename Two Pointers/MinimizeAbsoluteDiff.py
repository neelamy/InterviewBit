# Source : https://www.interviewbit.com/problems/minimize-the-absolute-difference/
# Given three sorted arrays A, B and Cof not necessarily same sizes.
# minimize | max(a,b,c) - min(a,b,c) |.

# Algo/DS : 3 pointers

# Complexity :O(n)

class Minimize:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        
        # start from the first element of each array 
        i = 0;j = 0; k = 0

        # set diff to intial value 
        diff = (max(A[i],B[j],C[k]) - min(A[i],B[j],C[k]))
            
        while i < len(A) and j < len(B) and k < len(C):
                
            new_diff = max(A[i],B[j],C[k]) - min(A[i],B[j],C[k])
            
            # if new_diff is smaller then reset diff to this new value   
            diff = min( diff, new_diff )
            
            # Find the minimum of A[i], B[j] and C[k] and move pointer to right so as to
            # reduce the diff  
            # X - Y = Difference  so to reduce difference increase Y 
            if A[i] == min(A[i],B[j],C[k]) : i += 1
                
            elif B[j] == min(A[i],B[j],C[k]) : j += 1
                
            elif C[k] == min(A[i],B[j],C[k]) : k += 1
              
        return diff 

def main():

	A = [ 1, 4, 5, 8, 10 ]

	B = [ 6, 9, 15 ]

	C = [ 2, 3, 6, 6 ]

	print Minimize().solve(A,B,C) # 1  We get the minimum difference for a=5, b=6, c=6 as | max(a,b,c) - min(a,b,c) | = |6-5| = 1.


if __name__ == '__main__':
	main()