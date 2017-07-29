# Source : https://www.interviewbit.com/problems/array-3-pointers/
# You are given 3 arrays A, B and C. All 3 of the arrays are sorted.
#Find i, j, k such that :
#max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.

# Algo/DS : 3 pointers

# Complexity : O(n) n = length of (A+B+C)

class FindMin:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):

    	# start from the last element of each array
    	i = len(A) - 1 ;j = len(B) - 1; k = len(C) - 1
		
		# set diff to intial value 
        diff = max(abs(A[i]-B[j]),abs(B[j] - C[k]), abs(C[k] - A[i]))
              
        while i > -1 and j > -1 and k > -1:
                
            new_diff = max(abs(A[i]-B[j]),abs(B[j] - C[k]), abs(C[k] - A[i]))
            
            # if new_diff is smaller then reset diff to this new value  
            diff = min(diff, new_diff)
             
            # Find the maximum of A[i], B[j] and C[k] and move pointer to left so as to
            # reduce the diff  
            if abs(A[i]-B[j]) == new_diff :

                if A[i] >= B[j] : i -= 1

                else: j -= 1
    
            elif abs(B[j] - C[k]) == new_diff:

                if B[j] >= C[k] : j -= 1

                else: k -= 1
                
            elif abs(C[k] - A[i]) == new_diff:

                if C[k] >= A[i] : k -= 1

                else: i -=1

     	# return diff           
        return diff 

def main():

    A = [1, 4, 10]

    B = [2, 15, 20]

    C = [10, 12]

    print FindMin().minimize(A,B,C) # 5 With 10 from A, 15 from B and 10 from C.


if __name__ == '__main__':
	main()