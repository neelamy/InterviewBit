# Source : https://www.interviewbit.com/problems/remove-duplicates-from-sorted-list-ii/
# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

# Algo/DS : Linked List

# Complexity : O(n)

import LinkedListBasic as LL

class FindUnique:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        
        # set current to head and previous to None
        initial_head ,current = A , A
        
        previous = None
        
        # while current and next node exist
        while current and current.next:
            
            next_node = current.next
            
            # if current val != next node then previous = current and current = next node
            if current.val != next_node.val:
                
                previous = current
                
                current = next_node
                
            else:
                
                # current node is not unique and we have to remove it
                # find next node whose value is different from current
                while next_node and (current.val == next_node.val):
                    
                    next_node = next_node.next
                
                # set current to new next node with different val    
                current = next_node
                
                # if previous is none that means initial values are same so we need to update initial_head
                if previous == None :
                    
                    initial_head = current
                # otherwise remove dupliactes and set previous.next = current    
                else: previous.next = current


        # return initial_head
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

	# Find Unique elements. Create new linked list using the head returned by the function
	new_list = LL.LinkedListFunction(FindUnique().deleteDuplicates(A.head))

	print "\n New List :" ,

	new_list.print_List() #  New List :2 


if __name__ == '__main__':
	main()