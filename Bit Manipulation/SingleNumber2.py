# Source : https://www.interviewbit.com/problems/single-number-ii/
# Given an array of integers, every element appears thrice except for one which occurs once.
# Find that element which does not appear thrice.

# Algo/DS : Bit manipulation

# Complexity :O(n) space - O(1)

class SingleNumber2:
	# @param A : tuple of integers
	# @return an integer
	def singleNumber(self, A):

		res = 0

		# check one bit at a time. Int has 32 bits
		for i in range(33):

			set_bit = 1 << i

			count = 0

			# for that bit, check how many times it is set in A
			for number in A :

				count = count + 1 if number & set_bit else count

			# if count%3 != 0 then that bit is set in single number
			res = res | set_bit if count % 3 != 0 else res

		return res

def main():
	print SingleNumber2().singleNumber([1, 2, 4, 3, 3, 2, 2, 3, 1, 1]) # 4


if __name__ == '__main__':
	main()