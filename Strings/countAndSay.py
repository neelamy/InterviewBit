# Source : https://www.interviewbit.com/problems/count-and-say/
#The count-and-say sequence is the sequence of integers beginning as follows: 1, 11, 21, 1211, 111221, ...

# Algo/DS : Stack

# Complexity :


class Solution:
	# @param A : integer
	# @return a strings

	def countAndSay(self, A):

		if A < 1 : return ""
		
		current_string = "1"
		
		while A > 1:
	 	
			new_string = ""
			
			# start checking from the begining of the string
			i = 0
			
			while i < len(current_string) :
				
				count = 0
				
				char = current_string[i]
				
				# increment count for same char
				while i < len(current_string)  and current_string[i] == char:
					
					count += 1
					
					i = i + 1
				
				# add count and char to new string	
				new_string += str(count)+ char			  
			
			current_string = new_string 
			
			A = A - 1
			 
		return current_string


def main():
	print Solution().countAndSay(5) # 111221


if __name__ == '__main__':
	main()