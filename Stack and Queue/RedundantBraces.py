# Source : 	https://www.interviewbit.com/problems/redundant-braces/
# 			Write a program to validate if the input string has redundant braces?
# 			((a + b)) has redundant braces so answer will be 1
#			(a + (a + b)) doesn't have have any redundant braces so answer will be 0

# Algo/DS : stack 

# Complexity :O(n)

class Solution:
    
    def braces(self, A):
        
        A = list(A)
        
        stack = []
        
        while A:
            
            item = A.pop(0)
            
            # add everything to stack if its not ')'
            if item != ')':
                
                stack.append(item)
                
            else:
                
                # between '(' and ')' there should be more than 1 item
                count_element = 0
                
                s = stack.pop()
                
                while s != '(':
                    
                    s = stack.pop()
                     
                    count_element = count_element + 1 
                
                if count_element <= 1:
                    return 1
                      
        return  0


def main():
	print Solution().braces("((a + b))") # 1


if __name__ == '__main__':
	main()