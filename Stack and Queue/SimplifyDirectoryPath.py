# Source : https://www.interviewbit.com/problems/simplify-directory-path/
# 			Given an absolute path for a file (Unix-style), simplify it.
#			path = "/home/", => "/home"
#			path = "/a/./b/../../c/", => "/c"

# Algo/DS : Stack

# Complexity :O(n)

class simplifyDirectoryPath:
  
    def simplifyPath(self, A):
        
        # split string based on "/"
        A =  A.split("/")
        
        stack = []
       
        # ignore '/' and '.'
        # for '..' if there are element in stack then pop the last element
        # if element is alphabet then insert in stack
        for i in A:
            
            if i == '/' or i =='.': continue
            
            elif i.isalpha() : stack.append(i)
            
            elif i == '..' and stack:
                    
                stack.pop()

        
        result ='/'

        #join stack element using '/' as delimiter
        result +="/".join(stack)

        return result

def main():
	print simplifyDirectoryPath().simplifyPath("/a/./b/../../c/") # "/c"


if __name__ == '__main__':
	main()