# Source : https://www.interviewbit.com/problems/ways-to-decode/
# Given an encoded message containing digits, determine the total number of ways to decode it

# Algo/DS : DP

# Complexity :O(n)

class Decode:
    # @param A : string
    # @return an integer
    def numDecodings(self, A):

		# if code starts with 0 then return        
        if A[0] == '0' : return 0
        
        res = [0] * len(A)
        
        res[0] = 1
        
        for i in range(1,len(A)):
            
        	# if current number is 0 then previous number should be 1 or 2
        	# Also in case of '0', previous number has to combined with it
        	# so res[i] = res[i-2] as there is only 1 way to add A[i-1]& A[i]
            if A[i] == "0" and A[i-1] not in ["1","2"] :
            
                return 0
                
            if A[i] == "0" and A[i-1]  in ["1","2"] :
                
				res[i] = res[i-2] if i != 1 else res[i-1]
                
				continue
            
            # if number combined with previous number lies between 10 and 26
            # then total ways = res [i-1] + res[i-2]
            # res[i-1] : ways considering A[i] individually
            # res[i-2] : ways considering A[i-1] + A[i] together

            res[i] = res[i-1]

            if int(A[i-1] + A[i]) < 27 and int(A[i-1] + A[i]) > 9: 
                
            	res[i] += res[i-2] if i != 1 else 1 
               
        # print res
        return res[-1]


def main():
	print Decode().numDecodings("12") # 2
	print Decode().numDecodings("10") # 1
	print Decode().numDecodings("2611055971756562") # 4


if __name__ == '__main__':
	main()