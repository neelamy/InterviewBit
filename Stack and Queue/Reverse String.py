# Source : https://www.interviewbit.com/problems/reverse-string/
# Given a string S, reverse the string using stack.

# Algo/DS : Stack

# Complexity : O(n)

class StringReversal:
    # @param A : string
    # @return a strings
    def reverseString(self, A):
        
        # append each element of A in stack
        stack = [i for i in A]
            
        reverse_string = ""
        
        # pop last element from stack and add to the string
        for i in range(len(stack)):

            reverse_string += stack.pop()
        
        # return the reversed string
        return reverse_string


def main():
	print StringReversal().reverseString("abcd") # dcba


if __name__ == '__main__':
	main()