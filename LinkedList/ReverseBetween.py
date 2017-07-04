# Source : https://www.interviewbit.com/problems/reverse-link-list-ii/
# Reverse a linked list from position m to n. Do it in-place and in one-pass. 

# Algo/DS : Linked List

# Complexity :O(n)

import LinkedListBasic as LL


class Reverse:

     def reverseBetween(self, A, m, n):
        
        head = A

        # in case of 0 or 1 node, return A
        if A is None or A.next is None: return A
        
        # previous will point to node after which reverse will start
        previous = None
        
        for i in range(1, m):
            
            previous = A
            
            A = A.next if A.next else None
        
        # curr is node which will later point to next of last reversed node
        curr = A

        next_node = A.next
         
        # reverse next n-m nodes 
        for i in range( n-m):
            
            next_of_next = next_node.next
            
            next_node.next = A
            
            A = next_node
            
            next_node = next_of_next
        
        # if previous is None then head must be updated
        # else previous.next will point to  last reversed node  
        if previous: previous.next = A

    	else : head = A

        curr.next = next_node
            
        return head

def main():

	# create linked list 
	A = LL.LinkedListFunction()

	for i in [5,4,3,2,1]:

		A.push_in_list(i)

	print " Original List :" ,

	A.print_List() # Original List : 1->2->3->4->5

	# reverse linked list. Create new linked list using the head returned by the function
	reverse_list = LL.LinkedListFunction(Reverse().reverseBetween(A.head, 2,4))

	print "\n Reversed List :" ,

	reverse_list.print_List() #  Reversed List : 1->4->3->2->5


if __name__ == '__main__':
	main()