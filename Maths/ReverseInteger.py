# Source : https://www.interviewbit.com/problems/reverse-integer/
# Reverse digits of an integer.

# Algo/DS : Maths

# Complexity : log(n)


class ReverseInteger:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        
        sign = True if A < 0 else False
        
        n = 0; i = 0
        
        # remove sign
        A = abs(A)
        
        while A > 0:
            
            n = (10 * n) +  (A % 10)
            
            A = A /10

        # to handle overflow case
        if n > ( 2 ** 31):
            
            n = 0

        return  -n if sign else n
            

def main():
	print ReverseInteger().reverse(-123) #321


if __name__ == '__main__':
	main()