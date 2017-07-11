# Source :https://www.interviewbit.com/problems/longest-common-prefix/
# Write a function to find the longest common prefix string amongst an array of strings.

# Algo/DS : String

# Complexity :O(no of strings * len of smallest string)

class Prefix:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        
        commonPrefix = ""
        
        flag = True
        
        for i in range(len(A[0])):
            
            char = A[0][i]
            
            for strings in A[1:]:
                
                if i >= len(strings) or  char != strings[i] :
                    
                    flag = False
                    
                    break
                
            if flag == False: break
            
            commonPrefix = commonPrefix + char
        
        return commonPrefix


def main():
    print Prefix().longestCommonPrefix(["abcdefgh","aefghijk","abcefgh"])


if __name__ == '__main__':
    main()