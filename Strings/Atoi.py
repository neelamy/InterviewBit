# Source : https://www.interviewbit.com/problems/atoi/
# Implement atoi to convert a string to an integer.

# Algo/DS : String

# Complexity : O(n)
class AtoiFunction:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        
        res = 0
        
        i = 0
        
        sign = 0
        
        while i < len(A):

        	# skip all leading spaces
            while i < len(A) and A[i] == " ":
                   
                i +=1
            
            # if sign is present then set value of sign     
            if A[i] in ['+', '-']:
                
                sign = 0 if A[i] == '+' else 1
                
                i += 1
            
            # if anything but integer is found then return 0    
            if not A[i].isdigit():
                
                return 0
            
            #take all digit and combine to form the number
            # break as soon as non-digit is encountered
            while i < len(A) and A[i].isdigit():
                    
                res = res * (10) +  (ord(A[i]) - ord('0'))
                   
                i +=1

            # break the loop    
            break
      
       	# set sign
        if sign: res = -res
        
        # handle integer overflow case
        if res > 2147483647: return 2147483647
        
        if res < - 2147483648 : return -2147483648
            
        return res
        
def main():
	print AtoiFunction().atoi("23hfhjj 45 nnn") # 23
	print AtoiFunction().atoi("-67") # -67
	print AtoiFunction().atoi("+ 7") # 0 (space after + is nt accepted)


if __name__ == '__main__':
	main()