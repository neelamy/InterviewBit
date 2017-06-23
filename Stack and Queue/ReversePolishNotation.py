# Source : 	https://www.interviewbit.com/problems/evaluate-expression/
# 			Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#			Valid operators are +, -, *, /. Each operand may be an integer or another expression.

# Algo/DS : Stack

# Complexity : O(n)

class Solution:
   
    def evalRPN(self, A):
        
        stack = []
        
        for i in A:
            
            # push all numbers in stack
            if i not in ['+','-','*','/']:
                
                stack.append(int(i)) # convert no to int before adding in stack
                
            else:

            	#if sufficient elements are not in stack then return 0
            	if len(stack) < 2 : return 0
                
                # in case of operator, pop last two numbers and perform operation and then push result in stack
                second_no = stack.pop()
                
                first_no = stack.pop()
                
                if i == '+' : z = first_no + second_no
                
                elif i == '-' : z = first_no - second_no
                
                elif i == '*' : z = first_no * second_no
                
                elif i == '/' : z = first_no /second_no
                
                stack.append(z)
                
        return stack[0] if len(stack) == 1 else 0


def main():
	print Solution().evalRPN(["2", "1", "+", "3", "*"]) # -> ((2 + 1) * 3) -> 9


if __name__ == '__main__':
	main()