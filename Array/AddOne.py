# Source : https://www.interviewbit.com/problems/add-one-to-number/
#Given a non-negative number represented as an array of digits,
#add 1 to the number ( increment the number represented by the digits ).
#The digits are stored such that the most significant digit is at the head of the list.

# Algo/DS : Array

# Complexity :O(n)

class AddOne:
			# @param A : list of integers
			# @return a list of integers
	def plusOne(self, A):

		n = len(A)
		
		carry = 1
					
		
		while carry and n > 0:
			
			n = n - 1
			
			new_number = A[n] + carry
			
			A[n] = new_number % 10
			
			carry = new_number / 10
					
		# if carry still present then add it at the begining of the array
		if carry :
					
			A.insert(0,carry)
					
		index = 0
		 
		# remove all leading 0 if present			
		for item in A:
					
			if item == 0 : index = index + 1

			else: break
					
		return A[index:]

def main():
	print AddOne().plusOne([9, 9, 9, 9, 9 ]) # 100000


if __name__ == '__main__':
	main()