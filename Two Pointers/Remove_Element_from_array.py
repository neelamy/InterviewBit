# Source : https://www.interviewbit.com/problems/remove-element-from-array/
# Given an array and a value, remove all the instances of that value in the array. 

# Algo/DS : 2 pointers

# Complexity :O(n)

class Remove:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        
        if not A : return []
        
        i = 0; j = 0
        
        while i < len(A):
            
            # if element is same same as B then copy it at jth location
            if A[i] != B:
                
                A[j] = A[i]
                
                i += 1
                
                j += 1
                
            else:
                
                # skip current element and move to next element
                i += 1
  
        return j 

def main():
	print Remove().removeElement([4, 1, 1, 2, 1, 3], 1) # 3 and A is now [4, 2, 3]


if __name__ == '__main__':
	main()