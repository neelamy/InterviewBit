# Source :https://www.interviewbit.com/problems/minimum-characters-required-to-make-a-string-palindromic/#
# You are given a string. The only operation allowed is to insert characters in the beginning of the string.
# How many minimum characters are needed to be inserted to make the string a palindrome string

# Algo/DS : String , KMP

# Complexity : O(needed)

class MakePalindrome:

	def calculateLPSArray(self, s):

		m = len(s)

		lps = [0] * m

		prefix = 0 ; suffix= 1

		# the loop calculates lps[i] for i = 1 to M-1
		while suffix < m:

				# if prefix and suffix  chrachter matches then lps[suffix] = 
				# length of prefix which is prefix + 1
				# increament suffix and prefix
			if s[prefix] == s[suffix]:

				lps[suffix] = prefix + 1

				prefix += 1

				suffix += 1

			else:
				# if prefix is 0 then suffix doesnt match even with 1st char
				# so lps[suffix] = 0
				# increament suffix
				if prefix == 0:

					lps[suffix] = 0

					suffix += 1

				else:
					# prefix doesnt match with suffix so now move prefix to
					# position where its suffix is equal to prefix 
					# i.e. lps[prefix - 1] .The idea is similar
		        	# to search step.
		        	# Note that we donot increament suffix.
					prefix = lps[prefix - 1]

		return lps

	# Find min character to make A palindrome by appending chars only at the begining of A
	def solve(self, A):
        
        # reverse A
		rev = A[::-1]
        
        #make new string by appending A with sentinel and reverse of A
		new_A = A + '$' + rev
        
        # find lps of new string
		lps = self.calculateLPSArray(new_A)
        
        # min char required is len(A) - lps[-1]
		return len(A) - lps[-1]

def main():
	print MakePalindrome().solve('ACTA') # 3 ATCACTA


if __name__ == '__main__':
	main()