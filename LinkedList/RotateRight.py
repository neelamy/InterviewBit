# Source : https://www.interviewbit.com/problems/rotate-list/
# Given a list, rotate the list to the right by k places, where k is non-negative.

# Algo/DS : Linked List

# Complexity :O(n)

import LinkedListBasic as LL

class Rotate:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):

        fast_ptr = A
          
        slow_ptr = None
        
        # check basic conditions
        if A is None or A.next is None or B== 0: return A
 
        # move fast_ptr forward by B nodes
        for i in xrange(B):

            fast_ptr = fast_ptr.next if fast_ptr else None

        # set slow_ptr to start of the list
        slow_ptr = A
        
        # move both pointers till fast_ptr reaches the last node           
        while fast_ptr.next:
                
            fast_ptr = fast_ptr.next
                
            slow_ptr = slow_ptr.next

        # last node will now point to head of the initial list
        fast_ptr.next = A
       
       # list will now start from node next to slow_ptr     
        A = slow_ptr.next
        
        # slow_ptr will now be last node
        slow_ptr.next = None
          
        return A



def main():

	# create linked list 
	A = LL.LinkedListFunction()

	for i in [5,4,3,2,1]:

		A.push_in_list(i)

	print " Original List :" ,

	A.print_List() # Original List : 1 2 3 4 5

	# Rotate linked list. Create new linked list using the head returned by the function
	rotate_list = LL.LinkedListFunction(Rotate().rotateRight(A.head, 2))

	print "\n Rotated List :" ,

	rotate_list.print_List() #  Reversed List : 4 5 1 2 3


if __name__ == '__main__':
	main()
