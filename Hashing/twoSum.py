# Source : https://www.interviewbit.com/problems/2-sum/
# Given an array of integers, find two numbers such that they add up to a specific target number.

# Algo/DS : Hashing

# Complexity :O(n)


class SumOfTwo:

	def twoSum(self, A, B):

		map_no_to_index = {}

		for index, value in enumerate(A):

			required_no = B - value

			if required_no in map_no_to_index : return (map_no_to_index[required_no], index + 1)

			if value not in map_no_to_index:  map_no_to_index[value] = index + 1

		return []




def main():
	print SumOfTwo().twoSum([2, 7, 11, 15], 9) # 1,2


if __name__ == '__main__':
	main()