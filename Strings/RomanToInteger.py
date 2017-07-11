# Source : https://www.interviewbit.com/problems/roman-to-integer/
# Given a roman numeral, convert it to an integer.

# Algo/DS : String, dictionary

# Complexity : O(n)

class RomanToInt:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):

        d = {'X': 10, 'L' : 50, 'C': 100, 'D': 500, 'M': 1000, 'V': 5, 'I': 1}

        n = 0

        for i in range(len(A)):

            if i + 1 < len(A) and d[A[i+ 1]]  > d[A[i]] :

            	n = n - d[A[i]]

            	continue

            n = n + d[A[i]]

        return n


def main():
	print RomanToInt().romanToInt("XIV") # 14


if __name__ == '__main__':
	main()