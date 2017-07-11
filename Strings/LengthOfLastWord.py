# Source : https://www.interviewbit.com/problems/length-of-last-word/
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

# Algo/DS : String

# Complexity : O(n)

class LastWordLength:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        
        word_length = 0
        
        for i in range(len(A)):
            
            # increment word length if char is not a space
            if A[i] != " " :

                word_length += 1

            else:

            	# skip all spaces
                while i < len(A) and A[i] == " ":

                    i = i + 1

                # if after spaces any letter is found then its a new word
                if i < len(A) and A[i] != " " :
 
                    word_length = 0
        # return word length      
        return word_length 


def main():
	print LastWordLength().lengthOfLastWord(" Hello World  ")


if __name__ == '__main__':
	main()