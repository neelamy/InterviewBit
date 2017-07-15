# Source : https://www.interviewbit.com/problems/intersection-of-sorted-arrays/
# Find the intersection of two sorted arrays.

# Algo/DS : 2 pointers, Arrar

# Complexity : O(n)

class Intersection:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        
        res = []
        
        i = 0; j = 0
        
        while i < len(A) and j < len(B):
            
            if A[i] == B[j] : 
                
                res.append(A[i])
                
                i += 1
                
                j += 1
                
            elif A[i] < B[j]: i += 1
            
            else : j += 1
            
        return res


def main():
	print Intersection().intersect([1,2,3,3,4,5,6],[3,3,5]) # [3,3,5]


if __name__ == '__main__':
	main()	