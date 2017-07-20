# Source : https://www.interviewbit.com/problems/merge-two-sorted-lists-ii/
# Given two sorted integer arrays A and B, merge B into A as one sorted array.

# Algo/DS : 2 pointers

# Complexity : O(N)

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return A modified after the merge
    def merge(self, A, B):
        
        if not B : return A
        
        if not A : return B
        
        i = 0 ; j = 0
        
        temp = []
        
        while i < len(A) and j < len(B):
            
            if A[i] <= B[j]:
                
                temp.append(A[i])
                
                i += 1
            else:
                
                temp.append(B[j])
                
                j +=1
   
        while i < len(A) :
            
            temp.append(A[i])
                
            i += 1
                       
        while j < len(B) :
            
            temp.append(B[j])
                
            j +=1
            
        return temp  

def main():

	print MergeList().merge([1,5,8],[6,9]) #[1,5,6,8,9]


if __name__ == '__main__':
	main()