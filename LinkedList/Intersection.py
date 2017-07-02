# Source : https://www.interviewbit.com/problems/intersection-of-linked-lists/
# Write a program to find the node at which the intersection of two singly linked lists begins.

# Algo/DS : LinkedList

# Complexity :O(n) space = O(1)

class LinkedList:
	def __init__(self, x):
		self.val = x
		self.next = None

	def print_List(self):

		while self:

			print self.val ,

			self = self.next

class Intersection:

	#@param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
	def getIntersectionNode(self, A, B):

		# find length of linked list A and B
		len_of_A = self.find_length(A)

		len_of_B = self.find_length(B)

		ptr_to_A , ptr_to_B = A, B

		# traverse the extra length of the bigger list
		if len_of_A > len_of_B :

			for i in xrange(len_of_A - len_of_B):

				ptr_to_A = ptr_to_A.next

		elif len_of_B > len_of_A :

			for i in xrange(len_of_B - len_of_A):

				ptr_to_B = ptr_to_B.next

		# Now linked List A and linked list B have equal elements
		# move both the pointers till they are not same
		while ptr_to_A != ptr_to_B:

			ptr_to_B = ptr_to_B.next

			ptr_to_A = ptr_to_A.next

		# ptr_to_A now points to intersection node
		return ptr_to_A

	# return length of linked List
	def find_length(self, L):

		length = 0

		while L :

			length += 1
			
			L = L.next

		return length


def main():
	
	# create linked List A
	A = LinkedList(1)

	A.next = LinkedList(2)

	A.next.next = LinkedList(3)

	A.next.next.next = LinkedList(4)

	A.next.next.next.next = LinkedList(5)

	# create linked List B
	B = LinkedList(-1)

	B.next = A.next.next

	# print Linked lists
	print " Linked List A : ",

	A.print_List() #  Linked List A :  1 2 3 4 5 

	print " \n Linked List B : ",

	B.print_List() #  Linked List B :  -1 3 4 5 
	
	intersection = Intersection().getIntersectionNode(A, B)

	print "\n Intersection list : ",

	intersection.print_List() #  Intersection list :  3 4 5



if __name__ == '__main__':
	main()