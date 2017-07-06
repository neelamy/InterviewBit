# Source : https://www.interviewbit.com/problems/k-reverse-linked-list/
# Given a singly linked list and an integer K, reverses the nodes of the
# list K at a time and returns modified linked list. The length of the list is divisible by K

# Algo/DS : Linked List

# Complexity :O(n)

import LinkedListBasic as LL

class KReverse:

	def swap( self,A, B):

		# first item A, will become the last node after reverse
		Last_node = A

		next_node = A.next

		# reverse next B-1 links
		for i in range(B-1):

			next_to_next = next_node.next if next_node else None

			next_node.next = A

			A = next_node

			next_node = next_to_next

		# Last_node will now point to next_node 
		Last_node.next = next_node

		# start node of this reversed list will now be A
		return A, Last_node, next_node

	def reverseList(self, A, B):

		head = LL.ListNode(0)

		reversed_list = head

		while A:

			head.next, Last_node, A = self.swap(A, B)

			head = Last_node

		return reversed_list.next




def main():

	# create linked list 
	A = LL.LinkedListFunction()

	for i in [6,5,4,3,2,1]:

		A.push_in_list(i)

	print " Original List :" ,

	A.print_List() # Original List : 5 4 3 2 1 

	# reverse linked list. Create new linked list using the head returned by the function
	reverse_list = LL.LinkedListFunction(KReverse().reverseList(A.head, 3))

	print "\n Reversed List :" ,

	reverse_list.print_List() #  Reversed List : 1 2 3 4 5


if __name__ == '__main__':
	main()