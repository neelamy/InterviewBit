# Source : https://www.interviewbit.com/problems/single-number/
# Given an array of integers, every element appears twice except for one. Find that single one.

# Algo/DS : Bit manipulation

# Complexity : O(n)

class NonReapeting:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        
        xor = reduce(lambda x,y : x ^ y ,A)
            
        return xor
            

def main():
	print NonReapeting().singleNumber([1 ,2 ,2 ,3 ,1]) #3


if __name__ == '__main__':
	main()