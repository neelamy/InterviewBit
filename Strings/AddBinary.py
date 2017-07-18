# Source : https://www.interviewbit.com/problems/add-binary-strings/
# Given two binary strings, return their sum (also a binary string).

# Algo/DS : String

# Complexity : O(n)

class BinarySum:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        
        # convert A and B to list of int
        A = map(int,A)
        
        B = map(int,B)
        
        carry = 0
        
        # ans will hold final result
        ans = ""
        
        # start iterating from the end of Array A and B
        i = len(A) - 1; j = len(B) - 1
        
        # add till either A or B or carry is present
        while i > -1 or j > -1 or carry:

            s = carry
            
            if i > -1 : s += A[i]

            if j > -1 : s += B[j]
            
            ans = str( s % 2) + ans  
            
            carry = s / 2
            
            i -= 1
            
            j -= 1
 
        
        return ans

def main():
	print BinarySum().addBinary("100","11") # 111


if __name__ == '__main__':
	main()