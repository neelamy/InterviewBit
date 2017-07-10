# Source : https://www.interviewbit.com/problems/palindrome-string/
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Algo/DS : Stack

# Complexity :O(n)

class Palindrome:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):

        A = A.lower()
        
        i, j = 0, len(A) -1
   
        while i <= j:

   
            while not A[i].isalnum() and i <j:
         
                i = i + 1

            while not A[j].isalnum() and i < j:
         
                j = j - 1
    
        
            if A[i]!= A[j] : return 0

            i = i + 1

            j = j- 1
          
        return 1


def main():
    print Palindrome().isPalindrome("A man, a plan, a canal: Panama") # 1


if __name__ == '__main__':
    main()