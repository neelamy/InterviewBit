# Source : https://www.interviewbit.com/problems/greatest-common-divisor/

# Algo/DS : recursion, maths

# Complexity :log(n)


class CalculateGCD:

    def gcd(self, A, B):
        
        if B == 0 : return A
        
        if A < B : A,B = B,A
        
        return self.gcd(B, A%B) 


def main():
	print CalculateGCD().gcd(4,6)


if __name__ == '__main__':
	main()