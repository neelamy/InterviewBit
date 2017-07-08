# Source : https://www.interviewbit.com/problems/generate-all-parentheses/
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid

# Algo/DS : Stack

# Complexity : O(n)

class Parentheses:
    # @param A : string
    # @return an integer
    def isValid(self, A):
        
        stack = []
        
        for i in A:
            
            if i in [ '(', '[','{']:
                
                stack.append(i)
                
            else:
                
                if stack :
                    
                    bracket = stack.pop()
                    
                else :

                	return 0
                
                if (bracket == '[' and i == ']' ) or (bracket == '(' and i == ')' ) or (bracket == '{' and i == '}' ):
                    
                    continue
                
                else : 

                	return 0
                
        return 0 if stack else  1


def main():
	print Parentheses().isValid("()[]{}") # 1

	print Parentheses().isValid("}]") # 0

if __name__ == '__main__':
	main()