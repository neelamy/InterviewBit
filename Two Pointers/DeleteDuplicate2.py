# Source : https://www.interviewbit.com/problems/remove-duplicates-from-sorted-array-ii/
# Given a sorted array, remove the duplicates in place such that each element can appear atmost twice and return the new length.

# Algo/DS : 2 pointers

# Complexity : O(n) space -O(1)

class RemoveDuplicate2:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        
        count = 0
        
        n = len(A)
        
        for i in range(n):
            
            if i < n - 2 and A[i] == A[i + 1] and A[i] == A[i + 2] : continue
        
            else:
                
                A[count] = A[i]
                
                count += 1
                
        return count
        

def main():
	print RemoveDuplicate2().removeDuplicates([1,1,1,2]) # 3 A = [1,1,2]


if __name__ == '__main__':
	main()