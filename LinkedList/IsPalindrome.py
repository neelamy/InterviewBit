# Source : https://www.interviewbit.com/problems/palindrome-list/
# Given a singly linked list, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively
# Expected solution is linear in time and constant in space.

# Algo/DS : Linked List

# Complexity :O(n), space - O(1)

import LinkedListBasic as LL

class Palindrome:

   	def reverseList(self, L):

   		if not L : return

	  	initial_head = L
		 
		next_node = L.next
		   
		while next_node:
		 	 
		 	next_of_next = next_node.next
		 	 
		 	next_node.next = L
		 	 
		 	L = next_node
		 	 
		 	next_node = next_of_next
		 	 
		initial_head.next = None
		 
		return L

	def split_list_in_half(self, L):

		initial_head = L

		fast_ptr, slow_ptr = L, L

		step = 0

		while fast_ptr.next:

			fast_ptr = fast_ptr.next

			step += 1

			if step % 2 == 0 : slow_ptr = slow_ptr.next

		list2 = slow_ptr.next 

		slow_ptr.next = None

		return initial_head, list2

	def compareList(self, A, B):

		if not A or not B : return 1

		while A and B:
   
	 	 	if A.val != B.val : return 0
	 	 	 
	 	 	A = A.next

	 	 	B = B.next
	 	 	 
	 	return 1


	def isPalindrome(self, A):

		list1, list2 = self.split_list_in_half(A)

		list2 = self.reverseList(list2)

		return self.compareList(list1, list2)

   

def main():

	# create linked list 
	A = LL.LinkedListFunction()

	for i in [1,2,1]:

		A.push_in_list(i)

	print " Original List :" ,

	A.print_List() # Original List : 1 2 1

	print     
	# reverse linked list. Create new linked list using the head returned by the function
	if Palindrome().isPalindrome(A.head):

		print " Linked List is palindrome"

	else:

		print " Linked List is not palindrome"


if __name__ == '__main__':
	main()