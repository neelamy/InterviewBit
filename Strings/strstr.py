# Source : https://www.interviewbit.com/problems/implement-strstr/
# strstr - locate a substring ( needle ) in a string ( haystack )

# Algo/DS : String, KMP

# Complexity :O(n + m) n = length of string , m = length of search string

class FindPattern:
    # @param haystack : string
    # @param needle : string
    # @return an integer
    
    def calculateLPSArray(self,s):

        m = len(s)
    
        lps = [0] * m
    
        prefix = 0 ; suffix= 1
    
        # the loop calculates lps[i] for i = 1 to M-1
        while suffix < m:
    
                # if prefix and suffix  chrachter matches then lps[suffix] = 
                # length of prefix which is prefix + 1
                # increament suffix and prefix
            if s[prefix] == s[suffix]:
    
                lps[suffix] = prefix + 1
    
                prefix += 1
    
                suffix += 1
    
            else:
                # if prefix is 0 then suffix doesnt match even with 1st char
                # so lps[suffix] = 0
                # increament suffix
                if prefix == 0:
    
                    lps[suffix] = 0
    
                    suffix += 1
    
                else:
                    # prefix doesnt match with suffix so now move prefix to
                    # position where its suffix is equal to prefix 
                    # i.e. lps[prefix - 1] .The idea is similar
                    # to search step.
                    # Note that we donot increament suffix.
                    prefix = lps[prefix - 1]
        return lps

    # O(n)
    def strStr(self, haystack, needle):
        
        if not haystack or not needle :return -1
 
        lps = self.calculateLPSArray(needle)
    
        original_index , search_index = 0, 0
    
        n = len(haystack); m = len(needle) 
    
        while original_index < n :
    
            # if chars match then increament search_index
            if haystack[original_index] == needle[search_index]:
    
                search_index += 1
                
                original_index += 1
    
            else:
    
                # else if search_index != 0 then reset it
                if search_index != 0:
    
                    search_index = lps[search_index - 1]
                    
                else:
                    # # if serach_index is 0 then just move to next char of original string
                    original_index += 1
    
            # if search string reaches its end then match has been found
            # reset search index
            if search_index  == m : 
    
                return  original_index - m
    
        return -1 


def main():
	print FindPattern().strStr("bbaabbbbbaabbaabbbbbbabbbabaabbbabbabbbbababbbabbabaaababbbaabaaaba", "babaaa") # 48


if __name__ == '__main__':
	main()