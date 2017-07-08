# Source : https://www.interviewbit.com/problems/sort-list/
# Sort a linked list in O(n log n) time using constant space complexity.

# Algo/DS : LInked List, Merge sort

# Complexity :O(nlogn)

import LinkedListBasic as LL

class MergeSort:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def sortList(self, A):

		if A is None or A.next is None : return A

		l1,l2 = self.split_list_in_half(A)

		l1 = self.sortList(l1)

		l2 = self.sortList(l2)

		return self.MergeList(l1,l2)

				
	def split_list_in_half(self, L):

		fast_ptr, slow_ptr = L, L

		while slow_ptr and fast_ptr and fast_ptr.next and fast_ptr.next.next:

			fast_ptr = fast_ptr.next.next

			slow_ptr = slow_ptr.next

		list2 = slow_ptr.next 

		slow_ptr.next = None

		return L, list2

	def MergeList(self, L1,L2):

		head = LL.ListNode(0)

		if L1 is None : return L2

		if L2 is None: return L1

		temp = head

		while L1 and L2:

			if L1.val <= L2.val:

				temp.next = L1

				L1 = L1.next

			else:

				temp.next = L2

				L2 = L2.next 

			temp = temp.next

		if L1: temp.next = L1

		if L2 : temp.next = L2

		return head.next



def main():

	# create linked list 
	A = LL.LinkedListFunction()

	for i in [ 3,4,5,1]:

		A.push_in_list(i)

	print " Original List :" ,

	A.print_List() # Original List : 1 5 4 3 


	# reverse linked list. Create new linked list using the head returned by the function
	mergesort_list = LL.LinkedListFunction(MergeSort().sortList(A.head))

	print "\n Sorted List :" ,

	mergesort_list.print_List() #  Sorted List : 1 3 4 5


if __name__ == '__main__':
	main()