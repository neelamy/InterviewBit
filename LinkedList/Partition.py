# Source : https://www.interviewbit.com/problems/partition-list/
# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
#You should preserve the original relative order of the nodes in each of the two partitions.

# Algo/DS : Linked List

# Complexity :O(n) space- O(1)

import LinkedListBasic as LL

class partitionList:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        
        lessthan =  LL.ListNode(0)
        
        greaterEqual = LL.ListNode(0)
        
        l1, l2 = lessthan, greaterEqual
        
        while A:
            
            if A.val < B:
                
                lessthan.next = A
                
                lessthan = lessthan.next
                
            else:
                
                greaterEqual.next = A
                
                greaterEqual = greaterEqual.next
                
            temp = A
                
            A = A.next
            
            temp.next = None
                
                
        lessthan.next = l2.next
        
        
        return l1.next

def main():

	# create linked list 
	A = LL.LinkedListFunction()

	for i in [2,5,2,3,4,1]:

		A.push_in_list(i)

	print " Original List :" ,

	A.print_List() # Original List : 5 4 3 2 1 

	# reverse linked list. Create new linked list using the head returned by the function
	partitioned_list = LL.LinkedListFunction(partitionList().partition(A.head, 3))

	print "\n Partitioned List :" ,

	partitioned_list.print_List() # Partitioned List : 1 2 2 4 3 5


if __name__ == '__main__':
	main()