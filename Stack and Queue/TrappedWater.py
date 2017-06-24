# Source : https://www.interviewbit.com/problems/rain-water-trapped/

# Algo/DS : Stack

# Complexity : O(n)

# program to find maximum amount of water that can
# be trapped within given set of bars.
class Solution:
   
	def trap(self, A):
			
		n = len(A) 

		LHS, RHS =[0] * n, [0] * n

		LHS[0] = A[0]

		RHS[-1] = A[-1]

		water = 0	

		# left[i] contains height of tallest bar to the
		# left of i'th bar including itself
		for i in xrange(1, n):
			LHS[i] = max(A[i], LHS[i-1])

		
		# Right [i] contains height of tallest bar to
		# the right of ith bar including itself
		for i in xrange(n-2, -1, -1):
			RHS[i] = max(RHS[i+1], A[i])

		# Calculate the accumulated water element by element
    	# consider the amount of water on i'th bar, the
    	# amount of water accumulated on this particular
    	# bar will be equal to min(left[i], right[i]) - arr[i] .
		water = [min(LHS[i],RHS[i]) - A[i] for i in range(n)]

		return sum(water)

   
						

def main():
	A = [3, 0, 0, 2, 0, 4] 
	print Solution().trap(A)   #10


if __name__ == '__main__':
	main()