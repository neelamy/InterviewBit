# Source : https://www.interviewbit.com/problems/assign-mice-to-holes/
# Assign mice to holes so that the time when the last mouse gets inside a hole is minimized

# Algo/DS : Greedy

# Complexity : O(n lg n)

class AssignMiceToHole:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def mice(self, A, B):
        
        A = sorted(A)
        
        B = sorted(B)
        
        diff = [ abs( max(i,j) - min(i,j)) for i,j in zip(A,B)]
        
        return max(diff)
        

def main():
	print AssignMiceToHole().mice([4,-4,2],[4,0,5]) # 4


if __name__ == '__main__':
	main()