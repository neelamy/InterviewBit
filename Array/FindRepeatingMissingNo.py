# Source : https://www.interviewbit.com/problems/repeat-and-missing-number-array/

# Algo/DS : Array , bit manipulation

# Complexity : O(n), space = O(1)


# Note : x ^ x = 0 so xor will remove all even nos and only odd nos are left
# if all nos are repeated except one : xor all elements of A. This will return only one odd element of array
# if only 1 no is repeated : (xor all element of A) xor ( 1^2^3....n). This will make all elements even except one repeated element which will now be odd


class RepeatMissingNumber:

    def repeatedNumber(self, A):
       
        n = len(A) 
        
        # Get the xor of all elements
        xor = reduce(lambda x, y : x^y , A)

        xor ^= reduce(lambda x, y : x^y , xrange(1, n+ 1))

        # Get the rightmost set bit in set_bit_no
        set_bit = xor & ~(xor - 1)

        x = reduce(lambda x, y : x^y ,[i for i in A if set_bit & i])

        y = reduce(lambda x, y : x^y ,[i for i in A if not set_bit & i])

        x ^= reduce(lambda x, y : x^y ,[i for i in xrange(1, n+ 1) if set_bit & i])

        y ^= reduce(lambda x, y : x^y ,[i for i in xrange(1, n+ 1) if not set_bit & i])

        return x , y

def main():
    print RepeatMissingNumber().repeatedNumber([2,3,1,3,5]) # 3, 4


if __name__ == '__main__':
    main()