# Source : https://www.interviewbit.com/problems/sort-by-color/
# Given an array with n objects colored red, white or blue, 
# sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

# Algo/DS : 2 pointers

# Complexity :O(n) space - O(1)

class Colors:
    # @param A : list of integers
    # @return A after the sort

    def sortColors(self, A):
        
        l = 0; r = len(A) -1; i = 0
        
        # we move all 0 to left and 2 to right. 1 will then be automatically in its right place
        while i <= r:

        	# do not change anything for 1
            if A[i] == 1 : i += 1
        	
        	# move 2 to the right end of the array
        	# i is not updated as new element brought from right
        	# needs to be inspected
            elif A[i] == 2 : 
                
                A[i],A[r] = A[r],A[i]
               
                r = r -1
            # move 0 to left side of array
            # update i as number brought from left will 1
            # and we make no changes for 1
            elif A[i] == 0:
                
                A[i],A[l] = A[l], A[i]
                
                i = i+ 1

                l = l + 1
              
        return A
            
            

def main():
	print Colors().sortColors([0,1,2,0,1,2]) # [0,0,1,1,2,2]


if __name__ == '__main__':
	main()