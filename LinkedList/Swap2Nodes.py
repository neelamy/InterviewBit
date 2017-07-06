# Source : https://www.interviewbit.com/problems/swap-list-nodes-in-pairs/
# Given a linked list, swap every two adjacent nodes and return its head.

# Algo/DS : Linked List

# Complexity : O(n)

import LinkedListBasic as LL

class Swap:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
 
        head = LL.ListNode(0)

        head.next = A

        current = head

        while current.next and current.next.next:

          	current.next = self.swapNode(current.next,current.next.next)

        	current = current.next.next
        
        return head.next

    # swap the next of two nodes
    def swapNode(self, node1, node2):

      	node1.next = node2.next

    	node2.next = node1

    	return node2

def main():

	# create linked list 
	A = LL.LinkedListFunction()

	for i in [4,3,2,1]:

		A.push_in_list(i)

	print " Original List :" ,

	A.print_List() # Original List : 1,2,3,4 

	# reverse linked list. Create new linked list using the head returned by the function
	swapped_list = LL.LinkedListFunction(Swap().swapPairs(A.head))

	print "\n Swapped List :" ,

	swapped_list.print_List() #  Reversed List : 2 1 4 3


if __name__ == '__main__':
	main()