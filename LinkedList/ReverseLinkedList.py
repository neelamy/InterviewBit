# Source : https://www.interviewbit.com/problems/reverse-linked-list/
# Reverse a linked list. Do it in-place and in one-pass.

# Algo/DS : Linked List

# Complexity :O(n)

import LinkedListBasic as LL


class Reverse:

    def reverseList(self, L):

      	initial_head = L
        
        next_node = L.next
          
        while next_node:
            
            next_of_next = next_node.next
            
            next_node.next = L
            
            L = next_node
            
            next_node = next_of_next
            
        initial_head.next = None
        
        return L

def main():

	# create linked list 
	A = LL.LinkedListFunction()

	for i in range(1,6):

		A.push_in_list(i)

	print " Original List :" ,

	A.print_List() # Original List : 5 4 3 2 1 

	# reverse linked list. Create new linked list using the head returned by the function
	reverse_list = LL.LinkedListFunction(Reverse().reverseList(A.head))

	print "\n Reversed List :" ,

	reverse_list.print_List() #  Reversed List : 1 2 3 4 5


if __name__ == '__main__':
	main()