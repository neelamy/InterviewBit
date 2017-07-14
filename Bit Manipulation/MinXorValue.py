# Source : https://www.interviewbit.com/problems/min-xor-value/
# Given an array of N integers, find the pair of integers in the array which have minimum XOR value. Report the minimum XOR value.

# Algo/DS : Bit Manipulation

# Complexity : O(n) * log(N)

class MinXor:
    # @param A : list of integers
    # @return an integer

    def findMinXor(self, A):
        
        A = sorted(A)
        
        xor = A[0] ^ A[1]

        for i in range(1, len(A)-1 ):
            
            xor = min(xor, A[i] ^ A[i+1])
                
        return xor
                

def main():
	print MinXor().findMinXor([0,2,5,7]) # 2 (0 XOR 2) 


if __name__ == '__main__':
	main()