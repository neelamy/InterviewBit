# Source : https://www.interviewbit.com/problems/remove-duplicates-from-sorted-array/
# Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.
# Also, update the array

# Algo/DS : Two pointers

# Complexity :O(n)

class DeleteDuplicate:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        
        #ptr will have all non repeated numbers
        ptr = 0
        
        if len(A) == 1: return 1,A
        
        for i in range(1, len(A)):
            
            # if A[i] is duplicate then move pointer i
            if A[ptr] == A[i]:
                
                continue
            
            else:

                # if A[i] is unique then copy it at ptr+1
                A[ptr + 1] = A[i]
                
                ptr = ptr + 1
                
        # update A       
        A = A[0:ptr + 1]
                
        return ptr+1, A

def main():
	print DeleteDuplicate().removeDuplicates([1,1,2])


if __name__ == '__main__':
	main()