class Solution:
  
    def minWindow(self, S, T):

        if len(S) < len(T) : return  ""

      
        
        d_pattern, d_string = {} ,{}

        for i in T:

            d_pattern[i] = 1 + d_pattern.get(i,0)

        start = 0 ; final_start = -1; count = 0

        min_length = len(S) + 1

      
       
        for index , item in enumerate(S):

            d_string[item] = 1 + d_string.get(item,0)

            if item in d_pattern and d_string[item] <= d_pattern[item] : 


                count += 1

            

            if count == len(T) : 


                while S[start] not in d_pattern or d_pattern[S[start]] < d_string[S[start]] :

                    d_string[S[start]] -= 1

                    start += 1

                if min_length > index - start + 1:

                        min_length = index - start + 1
                
                        final_start = start

            #print min_length

        return S[final_start: final_start + min_length] if final_start != -1 else ""


        
S = "A"

T ="A"

print Solution().minWindow(S,T)