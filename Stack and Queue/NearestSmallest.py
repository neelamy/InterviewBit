# Source : https://www.interviewbit.com/problems/nearest-smaller-element/
# Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.

# Algo/DS : Stack

# Complexity :O(n)

class NearestSmallest:
    # @param arr : list of integers
    # @return a list of integers
    def prevSmaller(self, arr):
        
        res = [-1] * len(arr)
        
        # stack will eventually contain numbers in descending order
        stack = []
        
        for i in range(len(arr)):	
            
            # stack will contain element less than current element of arr
            while stack and stack[-1] >= arr[i]:

                stack.pop()
            
            # if stack exists then last element of stack is less than current element 
            if stack: res[i] = stack[-1]   

            # add current element to stack
            stack.append(arr[i])
                    
        return res


def main():
	print NearestSmallest().prevSmaller([39, 27, 11, 4, 24, 32, 32, 1 ]) #[-1, -1, -1, -1, 4, 24, 24, -1]

if __name__ == '__main__':
	main()