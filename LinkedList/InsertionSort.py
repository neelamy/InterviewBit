# Source : https://www.interviewbit.com/problems/insertion-sort-list/
# Sort a linked list using insertion sort.

# Algo/DS : Linked List

# Complexity :O(n^2)

import LinkedListBasic as LL

class insertionSort:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        
        if A is None or A.next is None: return A
        
        # take first node as head of sorted list
        head = A
        
        # move A to next element in the list
        A = A.next

        # separate sorted list from A by making head.next = None
        head.next = None
         
        while A:

            next_node = A.next
            
            # for each element of A, start looking from 1st element of sorted list
            current = head
            
            # previous is node after which current node A will be inserted
            previous = None
            
            # move forward in sorted list till its value is less than value of A
            while current and current.val <= A.val :
                    
                previous = current
                
                current = current.next
                    
            # if previous is None then A will be new head    
            if previous == None:
                
                head = A
                
                head.next = current
                
            else:
                
                # else insert A after previous
                tmp = previous.next
                
                previous.next = A
                
                previous.next.next = tmp          
            
            # move A to next element
            A = next_node
        
        return head

def main():

	# create linked list 
	A = LL.LinkedListFunction()

	for i in [2,4,1,3]:

		A.push_in_list(i)

	print " Original List :" ,

	A.print_List() # Original List : 3 1 4 2  

	# reverse linked list. Create new linked list using the head returned by the function
	sorted_list = LL.LinkedListFunction(insertionSort().insertionSortList(A.head))

	print "\n Reversed List :" ,

	sorted_list.print_List() #  Reversed List : 1 2 3 4


if __name__ == '__main__':
	main()