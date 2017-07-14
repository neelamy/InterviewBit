# Source : https://www.interviewbit.com/problems/number-of-1-bits/
# Write a function that takes an unsigned integer and returns the number of 1 bits it has

# Algo/DS : Bit Manipulation

# Complexity :O(n)

class NumberOf1:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        
        count = 0
        
        while A:
            
            if A & 1 : count += 1
            
            A = A >> 1
                   
        return count


def main():
	print NumberOf1().numSetBits(12) #3


if __name__ == '__main__':
	main()