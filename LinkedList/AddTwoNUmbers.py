# Source : https://www.interviewbit.com/problems/add-two-numbers-as-lists/
# Add Two Numbers as ListsBookmark Suggest Edit
# You are given two linked lists representing two non-negative numbers. The digits are stored
# in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list

# Algo/DS : Linked List

# Complexity :O(n)

import LinkedListBasic as LL

class Addition:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        
        ans = LL.ListNode(0)
        
        head = ans
        
        carry = 0
        
        while A or B or carry:
            
            x = A.val if A else 0
            
            y = B.val if B else 0
            
            l = x + y + carry
            
            ans.next = LL.ListNode( l % 10)
            
            carry = l / 10
            
            A = A.next if A else None
            
            B = B.next if B else None
            
            ans = ans.next
            
            
        return head.next




def main():

	# create linked list 
	A = LL.LinkedListFunction()

	for i in [3,4,2]:

		A.push_in_list(i)

	print " List A:" ,

	A.print_List() #List A: 2 4 3 

	B = LL.LinkedListFunction()

	for i in [4,6,5]:

		B.push_in_list(i)

	print "\n List B:" ,

	B.print_List() # List B: 5 6 4

	# reverse linked list. Create new linked list using the head returned by the function
	sum_list = LL.LinkedListFunction(Addition().addTwoNumbers(A.head, B.head))

	print "\n Sum List :" ,

	sum_list.print_List() #  Sum List : 7 0 8


if __name__ == '__main__':
	main()
