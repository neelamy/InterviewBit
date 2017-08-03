# Source : https://www.interviewbit.com/problems/sliding-window-maximum/
# A long array A[] is given to you. There is a sliding window of size w which is 
# moving from the very left of the array to the very right. You can only see the w 
# numbers in the window. Each time the sliding window moves rightwards by one position.
# You have to find the maximum for each window. 

# Algo/DS : Dqueue

# Complexity : O(n)

class Solution:
    
    def slidingMaximum(self, A, B):
        
        if B >= len(A): return [max(A)]
        
        # Create a Double Ended Queue, "dqueue" that will store indexes of array elements
    	# The queue will store indexes of useful elements in every window and it will
    	# maintain decreasing order of values from front to rear in "dqueue", i.e., 
    	# element in "dqueue" are sorted in decreasing order
        dqueue = []
        
        # res will store the final result
        res =[]
        
        # Process first k (or first window) elements of array 
        for i in range(B):
            
            # For very element, the previous smaller elements are useless so
        	#remove them from dqueue
            while dqueue and A[dqueue[-1]] < A[i]:
                
                dqueue.pop()

            # Add new element at rear of queue    
            dqueue.append(i)
        
        # first element of dqueue is largest number in window so store it in res
        res.append(A[dqueue[0]])
        
        # Process rest of the elements, i.e., from arr[B] to arr[n-1]
        for i in range(B, len(A)):
            
            # Remove the elements which are out of this window
            if dqueue and dqueue[0] < i - B + 1:
                
                # Remove from front of queue
                dqueue.pop(0)
            
            # Remove all elements smaller than the currently
        	# being added element (remove useless elements)
            while dqueue and A[dqueue[-1]] < A[i]:
        
                dqueue.pop()
            
            # Add current element at the rear of dqueue   
            dqueue.append(i)
            
            
            res.append(A[dqueue[0]])
            
        return res


def main():
	
	A = [   10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

	B = 2

	print Solution().slidingMaximum(A, B) # 10,9,8,7,6,5,4,3,2



if __name__ == '__main__':
	main()