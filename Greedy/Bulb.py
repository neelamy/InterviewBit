# Source : https://www.interviewbit.com/problems/bulbs/
# Given an initial state of all bulbs, find the minimum number of switches you 
# have to press to turn on all the bulbs.

# Algo/DS : Greedy

# Complexity : O(n)

class SwitchBulb:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        
        if not A : return 0
        
        n = 1
        
        j = 0
        
        # find count of alternate 0 and 1 excluding same adjacent values eg. (0,1,1 = 2), (0,0 = 1), (0,1,0 = 3)
        # we dont include adjacent value which are same as they will be adjusted together
        # eg. 0,0 will be 1,1 in 1 go 
        for i in range(len(A)):
            
            if A[i] == A[j]:
                
                continue
                
            n += 1
            
            j = i
                
        # if starting element is 1 so we dont have to change it so reduce n by 1  
        # basiclly start counting from first 0      
        if A[0] == 1 : return n - 1
        
        return n
                
        

def main():
	print SwitchBulb().bulbs([0,1,0,1]) # 4
	print SwitchBulb().bulbs([0,1,0,1,1,0,1,0]) # 7
	print SwitchBulb().bulbs([1,1,0,1,1,0,1,0]) # 5


if __name__ == '__main__':
	main()