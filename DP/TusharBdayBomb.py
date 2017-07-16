# Source : https://www.interviewbit.com/problems/tushars-birthday-bombs/

# Algo/DS : DP

# Complexity :O(n)

class TusharBday:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def bombs(self, A, B):
        
        #find min element in the array. This is min strength
        min_element = min(B)
        
        # max kick = A / min_strength
        max_kick = A/min_element
        
        min_index = B.index(min_element)
        
        # create new array of eligible candidates. This will be strictly in descending order.
        # Start from min_strength and traverse left. Pick element i unless there is lesser element j
        # on its left because in that case we will select j as we need smaller index
        # eligible_cand = [min_index]
        
        for i in range(min_index -1 , -1, -1):
            
            # if element in eligible_cand is bigger than current element then pop them
            while eligible_cand and  B[i] <= B[eligible_cand[0]]:
                
                eligible_cand.pop(0)
            
            # append index to eligible_cand   
            eligible_cand = [i] + eligible_cand

        # or we can take all elements till min_strength. This also works
        #eligible_cand = range(0,min_index+1)
        
        # this will store final result
        res = []
        
        # we inspect eligible_cand array and check if we can replace an instance of min_element
        # with any element of eligible_cand with lesser index. We remove one instance at a time so that
        # max number of kicks remain unchanged

        # residue is (one instance of min strength + (A % min strength))
        residue = (A % min_element) + min_element 
       
        count = 0 ; i = 0
        
        while i < len(eligible_cand):

            # if element is less than residue then it can replace one instance of min_element
            if B[eligible_cand[i]] <= residue  :

            	# increase count
                count += B[eligible_cand[i]]

                # if count exceed A then return
                if count > A: return res

                # else append index to res array
                res.append(eligible_cand[i])

                # new residue is (one instance of min_element + whatever is left from
                # previous residue after subtracting element taken recently)
                residue = (residue - B[eligible_cand[i]] )+ min_element

            else:

            	# if current element is greater than residue then move to next element
                i += 1
                                
        return res


def main():
	print TusharBday().bombs(11, [6,8,5,4,7])


if __name__ == '__main__':
	main()