# Source : https://www.interviewbit.com/problems/stairs/

# Algo/DS : DP

# Complexity : O(n)

class Stairs:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        
        if A < 2 : return A

        no_of_ways = [0] * A
         
        no_of_ways[0] = 1
        
        no_of_ways[1] = 2
        
        # for ith step, number of ways = (no of ways to reach (i-1) and take 1 step to reach i) + 
        # 									(no of ways to reach (i-2) and take 2 step to reach i)
        for i in range(2,A):
            
            no_of_ways[i] = no_of_ways[i-1] + no_of_ways[i-2]
            
      
            
        return no_of_ways[-1]

def main():
	print Stairs().climbStairs(5) # 8


if __name__ == '__main__':
	main()