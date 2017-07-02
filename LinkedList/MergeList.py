# Source : https://www.interviewbit.com/problems/merge-two-sorted-lists/
# Merge Two Sorted ListsBookmark Suggest Edit

# Algo/DS : Linked List

# Complexity : O(n)

import LinkedListBasic as LL

class MergeList:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
    	
    	# create dummy node
        dummy = LL.ListNode(0)
        
        # save this initial head    
        initial_head = dummy
        
        # dummy.next will point to next smallest number.
        # move dummy to dummy.next and update A or B accordingly
        while A and B:
            
            if A.val <= B.val :
            
                dummy.next = A
            
                A = A.next
            
            else:
            
                dummy.next = B
            
                B = B.next
                
            dummy = dummy.next
        
        # append the remaining list to dummy        
        if A:
            
            dummy.next = A
            
        elif B:
            
            dummy.next = B
            
        return initial_head.next
            



def main():

	# create linked list A and B
	A = LL.LinkedListFunction()

	for i in [20,8,5]:

		A.push_in_list(i)

	B = LL.LinkedListFunction()

	for i in [15,11,4]:

		B.push_in_list(i)

	print " A :" ,

	A.print_List() # 5 -> 8 -> 20 

	print " \n B :" ,

	B.print_List() # 4 -> 11 -> 15    


	# Merge linked list. Create new linked list using the head returned by the function
	merged_list = LL.LinkedListFunction(MergeList().mergeTwoLists(A.head, B.head))

	print " \n Merged List :" ,

	merged_list.print_List() # 4 -> 5 -> 8 -> 11 -> 15 -> 20 


if __name__ == '__main__':
	main()