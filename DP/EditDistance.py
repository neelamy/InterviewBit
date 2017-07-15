# Source : https://www.interviewbit.com/problems/edit-distance/
# Given two words A and B, find the minimum number of steps required to
# convert A to B. (each operation is counted as 1 step.)

# Algo/DS : DP

# Complexity :O(len(A)* len(B))

class EditDistance:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        
        A = A.strip()
        
        B = B.strip()

        len_A = len(A)
        
        len_B = len(B)
        
        # create len_A * len_B matrix
        dist = [[0 for j in range(len_B + 1)] for i in range(len_A+ 1)]
        
        # if A ="" then  dist[0] = length of B 
        dist[0] = [i for i in range(len_B+ 1)]
         
        # if B ="" then  dist[i][0] = length of A   
        for i in range(len_A +1):
            
            dist[i][0] = i
        
        # start from i=j=1 and continue till i = len(A) and j = len(B)        
        for i in range(1, len_A + 1):
            
            for j in range(1, len_B + 1):
                
                if A[i-1] == B[j-1]:
                    
                    # if chars are same, take value till previous char ie dist[i-1][j-1]
                    dist[i][j] = dist[i-1][j-1]
                    
                else:
                	# dist[i][j] = 1 + min(replace, insert, delete)
                    dist[i][j] = 1 + min(dist[i-1][j-1], dist[i][j-1],dist[i-1][j])
     
        return dist[-1][-1]

def main():
	print EditDistance().minDistance("Anshuman", "Antihuman")


if __name__ == '__main__':
	main()