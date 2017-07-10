# Source : https://www.interviewbit.com/problems/reverse-the-string/
# Given an input string, reverse the string word by word.

# Algo/DS : Stack

# Complexity :

class ReverseString:
    # @param A : string
    # @return string
    def reverseWords(self, A):
        
        rev_string = ""
        
        word =""
        
        for i in range(len(A)):

            if A[i] == " "  and word == "" : continue

            # add non space char to word
            if A[i] != " " : word += A[i]
            
            else:
                
                # if space is encountred then add word in fromt of rev_string
                rev_string = word + " " + rev_string
                
                word = ""
                
        rev_string = word +" " + rev_string
                
        return rev_string.strip()


def main():
	print ReverseString().reverseWords("the sky       is blue") # "blue is sky the"


if __name__ == '__main__':
	main()