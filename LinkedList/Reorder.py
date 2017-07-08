# Source : https://www.interviewbit.com/problems/reorder-list/
# Given a singly linked list L1,L2,L3,L4,......Ln reorder it to: L1,Ln,L2,Ln-1..... 
# You must do this in-place without altering the node's values.

# Algo/DS : Linked List

# Complexity :

import LinkedListBasic as LL

class Reorder:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def reorderList(self, A):
		
		if A is None or A.next is None : return A
		
		# split list into 2 half
		l1, l2 = self.split_list_in_half(A)

		# reverse l2
		l2 = self.reverseList(l2)
		
		# merge both list. After each element of l1 insert next element of l2
		while l1 and l2:

			previous_next = l1.next

			l1.next = l2

			l2 = l2.next

			l1.next.next = previous_next

			l1 = previous_next

		return A
			


	def split_list_in_half(self, L):

		fast_ptr, slow_ptr = L, L

		while slow_ptr and fast_ptr and fast_ptr.next and fast_ptr.next.next:

			fast_ptr = fast_ptr.next.next

			slow_ptr = slow_ptr.next

		list2 = slow_ptr.next 

		slow_ptr.next = None

		return L, list2


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

	for i in [ 4,3,2,1]:
	
		A.push_in_list(i)

	print " Original List :" ,

	A.print_List() # Original List : 1 2 3 4 

	# reverse linked list. Create new linked list using the head returned by the function
	reorder_list = LL.LinkedListFunction(Reorder().reorderList(A.head))

	print "\n Reversed List :" ,

	reorder_list.print_List() #  Reversed List : 1 4 2 3


if __name__ == '__main__':
	main()