# Source : https://www.interviewbit.com/problems/window-string/
#Given a string S and a string T, find the minimum window in S which will contain all the characters in T in linear time complexity.

# Algo/DS : String, hashing

# Complexity : O(n)

class WindowString:
  
    def minWindow(self, S, T):

    	# return if S is empty
        if len(S) < len(T) : return  ""

        d_pattern, d_string = {} ,{}

        # store count of each char of T in d_pattern
        for i in T:

            d_pattern[i] = 1 + d_pattern.get(i,0)

        start = 0 ; final_start = -1; count = 0

        min_length = len(S) + 1

        # check all char of S
        for index , item in enumerate(S):

        	# store count of each char of S in d_string
            d_string[item] = 1 + d_string.get(item,0)

            # if char is in T and its number of occurance is S is less than T
            # then increase count
            if item in d_pattern and d_string[item] <= d_pattern[item] : 

                count += 1

            # when count reaches len(T), try to remove extra chars
            if count == len(T) : 

            	# if char at start is not in T or its number of occurance is more than T
            	# move start to next char and reduce the count of that char in d_string
                while S[start] not in d_pattern or d_pattern[S[start]] < d_string[S[start]] :

                    d_string[S[start]] -= 1

                    start += 1

                # set min_len and final start
                if min_length > index - start + 1:

                        min_length = index - start + 1
                
                        final_start = start

        # return the substring starting from final_start till it has min_length char
        return S[final_start: final_start + min_length] if final_start != -1 else ""

def main():
	
	print WindowString().minWindow("ADOBECODEBANC", "ABC") #BANC


if __name__ == '__main__':
	main()