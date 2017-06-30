# Source : https://www.interviewbit.com/problems/equal/
# Given an array A of integers, find the index of values that satisfy A + B = C + D, where A,B,C & D are integers values in the array
# Input: [3, 4, 7, 1, 2, 9, 8]
# Output: [0, 2, 3, 5] (O index)

# Algo/DS : Hashing

# Complexity :O(n^3)

from collections import defaultdict
class EqualSum:

    def equal(self, A):
       
        dictionary = defaultdict(list)

        # save (i,j) pair in dictionary[i+j]
        # sum represents the key and i,j are elements that form that sum
        for i in range(len(A)):

            for j in range(i + 1, len(A)):

                n = A[i] + A[j]

                # store (i,j) pair in dictionary only if both i,j are unique and 
                # not already present in dictionary[sum]
                if i in dictionary[n] or j in dictionary[n]: continue

                dictionary[n].extend([i,j])

        # take all dictionary values which have more than or equal to 4 elements
        # i.e. 2 pairs having same sum
        res = [dictionary[i] for i in dictionary if len(dictionary[i]) >= 4]

        # sort and take first 4 element of 1st sum
        return sorted(res)[0][:4]

def main():
	print EqualSum().equal([3, 4, 7, 1, 2, 9, 8]) # [0, 2, 3, 5]
	print EqualSum().equal([1,1,1,1,1]) # [0,1,2,3]


if __name__ == '__main__':
	main()