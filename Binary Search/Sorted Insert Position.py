# Source : https://www.interviewbit.com/problems/sorted-insert-position/
# Given a sorted array and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# Algo/DS : Binary search

# Complexity : O(log n)

class BinarySearch:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        
        low = 0; high = len(A) - 1
    
        while low <= high :
                          
            mid = (low + high) / 2  

            #print low, high, mid
            
            if A[mid] == B : return mid
            
            if A[mid] > B: high = mid - 1
            
            else : low = mid + 1

        return low

def main():
	print BinarySearch().searchInsert([1,3,5,6], 7) #4
	print BinarySearch().searchInsert([1,3,5,6], 0) #0

if __name__ == '__main__':
	main()