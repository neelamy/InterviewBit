# Source : https://www.interviewbit.com/problems/4-sum/
# Given an array S of n integers, are there elements a, b, c, and d in S such
# that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Algo/DS : Hashing

# Complexity :O(n^2)

from collections import defaultdict

class fourSum:


    def fourSum(self, A, B):

        sum_of_two = defaultdict(list)
        
     	is_sum_used ={}

     	# create dictionary of sum of each possible pair
        for i in range(len(A)):

            for j in range(i + 1, len(A)):

                    n = A[i]+ A[j]

                    # save index pair as indices are uniques where as values can be repeated if at different indices
                    sum_of_two[n].append((i,j)) 
                    
                    is_sum_used[n] = False

      
        res = set()

        # for each sum(i.e. a+b), check if c + d i.e. B -(a+b) is present in dictionary
        # if yes, take all unique combination of both the lists
        for sum1 in sum_of_two:

            sum2 = B - sum1

            if sum2 in sum_of_two and is_sum_used[sum2] == False:

                for pair1 in sum_of_two[sum1]:

                    for pair2 in sum_of_two[sum2]:

                    	#  make sure same index is not used in both pairs
                        if  pair1[0]  in pair2 or pair1[1] in pair2 : continue 

                        # sort the list before adding as set consider(1,2) and (2,1) as different pair
                        # we have to eliminate all the duplicates
                       	res.add(tuple(sorted(pair1 + pair2)))
                
                # mark both sum as used so that they are not used again
                # eg if sum1= 1 and sum2 = 3 then sum1= 3 should be avoided        
                is_sum_used[sum1], is_sum_used[sum2] = True, True
          

        final_result = set()

        # convert index values to their actual values and eliminate duplicates
        for quadruplets in res:

            final_result.add(tuple(sorted(([A[index] for index in quadruplets]))))

        # return sorted result
        return  sorted(final_result)
        

def main():

	print fourSum().fourSum([23, 20, 0, 21, 3, 38, 35, -6, 2, 5, 4, 21 ], 29) # [0 2 4 23 ] [0 3 5 21 ] [0 4 5 20 ] [2 3 4 20 ] 



if __name__ == '__main__':
	main()