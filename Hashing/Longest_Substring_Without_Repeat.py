# Source : https://www.interviewbit.com/problems/longest-substring-without-repeat/
# Given a string, find the length of the longest substring without repeating characters.

# Algo/DS : Hashing

# Complexity :O(n + d) d : chars in dictionary 

class Substring:
  
    def lengthOfLongestSubstring(self, A):
        
        d = {}
        
        max_length = 0

        i, start = 0, 0 
     
        # traverse string A
        while i < len(A):
            
            # if A[i] is already in d then keep moving start till
            # A[i] is not in d. Remove start entry from d as well
            if A[i] in d :
              
                while A[i] in d:

                    del d[A[start]]
                    
                    start += 1
            
            # set count in d for A[i]
            d[A[i]] = 1
            
            # set max_length    
            max_length = max(max_length, i + 1 - start) 
               
            i += 1
        
        return max_length


def main():
	
	print Substring().lengthOfLongestSubstring("abcabcbb") # 3 "abc"


if __name__ == '__main__':
	main()