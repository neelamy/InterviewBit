# Source : https://www.interviewbit.com/problems/largest-continuous-sequence-zero-sum/
# Find the largest continuous sequence in a array which sums to zero.

# Algo/DS : Hashing

# Complexity : O(n)

class Sequence:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A): 
        
        # d[i] will be cumulative sum of array till index i
        d = {}
        
        # store max length of sequence
        max_length = 0
        
        cumulative_sum = 0
        
        # stores starting index of sequence
        start = 0
        
        for i in range(len(A)):
            
            # calculate cumulative sum till index i
            cumulative_sum += A[i]
            
            # if cumulative sum = 0 then start index will be 0
            # length of current sequence will be  i + 1
            if cumulative_sum == 0:
                
                max_length = max(max_length , i + 1 )
                
                start = 0
            
            # if cumulative sum is not in d then add it in d   
            elif cumulative_sum not in d:
                
                d[cumulative_sum] = i
            
            # if cumulative sum is present in d then length of seq = i - d[cuml sum] 
            # and start index =  d[cuml sum] + 1
            # Logic : if cuml sum till index i is say 5 and at index j sum is again 5
            # that means sum of array element from i + 1 till j is 0
            # A + B = A  means B = 0 
            elif max_length < i  - d[cumulative_sum]:
                
                max_length = i - d[cumulative_sum]
                
                start = d[cumulative_sum] + 1
                
        #print start, max_length        
        return A[start : start + max_length]

def main():
	
	print Sequence().lszero([1, 2, -2, 4, -4]) # [2, -2, 4, -4]


if __name__ == '__main__':
	main()