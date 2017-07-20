# Source : https://www.interviewbit.com/problems/integer-to-roman/#
# Given an integer, convert it to a roman numeral, and return a string corresponding to its roman numeral version

# Algo/DS : String

# Complexity :

class InttoRoman:
    
    # find the place of left most digit
    # eg : 456 return 400, 3567 return 3000
    def digit(self,A):

        i = 0

        while A > 9:

            A = A / 10

            i += 1

        return A * (10 ** i)

    # Check in following order:
    #1. if A in d : return d[A]
    #2. Find left most digit,
    #	i) if it is present in d add it to result
    #	ii) else, check if left_digit can be formed by subtracting 2 dictionary values
    #	iii) else, find appropriate number from dictionary and add value to result
    # A = A - left_digit
    def intToRoman(self, A):
        
        d = {10 : 'X', 50 : 'L', 100: 'C', 500: 'D', 1000: 'M' , 5 :'V', 1: 'I'}
        
        # this will store the final result
        res = ""
   
        while A:

        	# if A is present in d then return d[A]
            if A in d : 

                res += d[A]

                return res

            # find the place of left most digit
            left_most = self.digit(A)

            # if left_most is present in d then add d[left_most] to res
            if left_most in d :

                res += d [left_most]

                A = A - left_most

                continue

            # else check if left_most can be formed by subtracting two values of d
            # eg : 4 = 5- 1 then add d[1] + d[5] to res. 
            # Note small number should be before bigger number to show subtraction
            
            flag = False

            for i in d:

                for j in d:

                    if  i - j == left_most :

                        res += d[j] + d[i]

                        A = A - left_most

                        flag = True


            # check which number from dictionary is greater than A and can be used
            # Note : use values in d in descending order
            if not flag :

	            for i in sorted(d)[::-1]:

	                if left_most > i :

	                	# use d[i] quotient number of times
	                	# eg : 3000/1000 = 3 so repeat M 3 times
	                    res += d[i] * (left_most/i)

	                    A = A - (i * (left_most/i))

	                    break       
        return res



def main():
	print InttoRoman().intToRoman(6) # VI

	print InttoRoman().intToRoman(400) # CD

	print InttoRoman().intToRoman(99) # XCIX


if __name__ == '__main__':
	main()