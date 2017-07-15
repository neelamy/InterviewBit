# Source : https://www.interviewbit.com/problems/remove-element-from-array/
# Given an array and a value, remove all the instances of that value in the array. 

# Algo/DS : 2 pointers

# Complexity :O(n)

class Remove:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        
        count = 0

        for i in A:

            if i == B: continue

            else:
                A[count] = i
                count +=1
        
  
        return count 

def main():
	print Remove().removeElement([4, 1, 1, 2, 1, 3], 1) # 3 and A is now [4, 2, 3]


if __name__ == '__main__':
	main()