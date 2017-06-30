# Source : https://www.interviewbit.com/problems/anagrams/
# Given an array of strings, return all groups of strings that are anagrams.

# Algo/DS : Hash Table

# Complexity :O(n log n)

from collections import defaultdict

class Anagram:

    def anagrams(self, A):
        
        # create dictionary of all unique letter words
        dictionary = self.create_dic(A)
    	
    	# list has to printed in correct order eg [1,3][2,4] and not [2,4][1,3]
    	# for this sort the value list. This will sort based on the 1st element of each list
        return sorted(dictionary.values())

           
    def  create_dic(self, A):

        dictionary = defaultdict(list)

        for index, word in enumerate(A):
            
            # sort the word and add its index in dictionary using sorted word as key
            # eg : cat, atc,tca,tac etc will all have one key : "act"
            # sorted returns a list so join the list to form a string
            word = "".join(sorted(word))

            dictionary[word].append(index+ 1)

        return dictionary


def main():
	print Anagram().anagrams([ "cat", "dog", "god", "tca"]) # [[1, 3], [2, 4]]


if __name__ == '__main__':
	main()	