# Source : https://www.interviewbit.com/problems/largest-rectangle-in-histogram/
# Given n non-negative integers representing the histogram bar height where the
# width of each bar is 1, find the area of largest rectangle in the histogram.

# Algo/DS : Stacks

# Complexity : O(n)

class HistogramArea:
   
    def largestRectangleArea(self, A):
    
        stack = []
        
        max_area = 0
        
        for i in range(len(A)):
            
            # push index in stack if stack is empty or new element is greater than top element of stack
            if not stack or A[stack[-1]] < A[i]:
                
                stack.append(i)
                
            else:
                #pop from stack till top element of stack is smaller than current element
                # for each popped element calculate current area
                while stack and A[stack[-1]] > A[i] :
                    
                    # value of top element of stack
                    bar = A[stack.pop()]
                    
                    # element smaller than bar on RHS is at index i
                    RHS = i
                    
                    # element smaller than bar on LHS is at top of stack
                    LHS = stack[-1] if stack else 0 
                    
                    # calculate current_area.
                    # current_area = bar * (RHS-LHS-1)
                    # if stack is empty then all element left of i are smaller so area = bar * RHS
                    current_area = (bar * (RHS - LHS - 1)) if stack else (bar * RHS)
                    
                    max_area = max(max_area, current_area)
                
                # append current element's index in stack    
                stack.append(i)
                    
        # repeat above steps till stack is not empty
        while stack :
                    
            bar = A[stack.pop()]
                    
            RHS = i + 1
                    
            LHS = stack[-1] if stack else 0
                    
            current_area = (bar * (RHS - LHS - 1)) if stack else (bar * RHS)
                    
            max_area = max(max_area, current_area)        
            
            
        return max_area    

def main():
	
	print HistogramArea().largestRectangleArea([2,1,5,6,2,3]) # 10


if __name__ == '__main__':
	main()