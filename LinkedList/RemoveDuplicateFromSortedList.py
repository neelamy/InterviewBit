# Source : https://www.interviewbit.com/problems/remove-duplicates-from-sorted-list/
# Given a sorted linked list, delete all duplicates such that each element appear only once.

# Algo/DS : Linked List

# Complexity : O(n)

import LinkedListBasic as LL

class RemoveDuplicate:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, head_node):
        
        initial_head = head_node
        
        # traverse till next node is present
        while head_node.next:
            
            # if vale of current node = value of next node then skip next node
            if head_node.val == head_node.next.val :

                head_node.next = head_node.next.next
            else:
            	# else move to next node
                head_node = head_node.next
        
        # return the initial head         
        return initial_head


def main():

	# create linked list 
	A = LL.LinkedListFunction()

	A.push_in_list(3)

	A.push_in_list(3)

	A.push_in_list(2)

	A.push_in_list(1)

	A.push_in_list(1)

	print " Original List :" ,

	A.print_List() # Original List : 1 1 2 3 3 

	# Remove duplicates. Create new linked list using the head returned by the function
	new_list = LL.LinkedListFunction(RemoveDuplicate().deleteDuplicates(A.head))

	print "\n New List :" ,

	new_list.print_List() #  New List : 1 2 3


if __name__ == '__main__':
	main()