# Source : https://www.interviewbit.com/problems/valid-number/
# Validate if a given string is numeric.

# Algo/DS : String

# Complexity : O(n)

class isValid:
 
    def isNumber(self, A):

        # trim trailing spaces
        A = A.strip()
        
        # return 0 for empty string
        if not A : return 0
        
        # remove leading spaces
        temp = 0
        
        while A[temp] == " " and temp < len(A) -1 : temp += 1
            
        A = A[temp:]  

        # if last char is not digit then return 0
        if not A or not A[-1].isdigit(): return 0
        
        count_e = 0; count_dot = 0
        
        for i in range(len(A)):
            
            # if char is digit then proceed to next char
            if A[i].isdigit() : continue
            
            # +,- and . can be present at first position
            if i == 0 and A[i] in ['-','+','.']:
                
                continue

            # return 0 for anything else
            elif i == 0 and  not A[i].isdigit(): return 0
            
            # cases to check for e:
            # 1. only one occurence of e
            # 2. char before e should be digit
            if A[i] == 'e' :
                
                if count_e  or (i-1 > -1 and not A[i-1].isdigit()) : return 0
        
                count_e = 1
  

            # cases to check for .:
            # 1. only one occurence of .
            # 2. if e has already occured then return 0
            elif A[i] == '.':
    
                if count_e or count_dot : return 0
                 
                count_dot = 1
            
            # cases to check for +, -:
            # 1. should occur only after e   
            elif A[i] in ['+','-']:
                
                if i-1 > -1 and A[i-1] != 'e' : return 0
                
            # return 0 if anything else encountered   
            elif not A[i].isdigit() : return 0
            
        # return 1    
        return 1
                

def main():
    print isValid().isNumber("12e12") # 1
    print isValid().isNumber("12e1.2") # 0
    print isValid().isNumber("-12e-12") # 1

if __name__ == '__main__':
    main()