# Source : https://www.interviewbit.com/problems/list-cycle/
# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
# why this logic works : https://www.quora.com/How-does-Floyds-cycle-finding-algorithm-work

# Algo/DS : Linked List

# Complexity :O(n)


class LinkedList:
	
	def __init__(self, x):
		self.val = x
		self.next = None

	def print_List(self):

		while self:

			print self.val ,

			self = self.next

class ListCycle:
   
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        
        slow_ptr, fast_ptr = A, A
        
        while fast_ptr:
            
            slow_ptr = slow_ptr.next

            fast_ptr = fast_ptr.next.next if fast_ptr.next and fast_ptr.next.next else None
                
            if fast_ptr == slow_ptr :
                
                break  # cycle detected so break from loop            
        
        # if end of list reached then no cycle
        if fast_ptr == None : return None
        
        # set slow pointer to the begining of list
        slow_ptr = A
        
        # move both pointers to next node till they meet
        while slow_ptr != fast_ptr:
            
            slow_ptr = slow_ptr.next
            
            fast_ptr = fast_ptr.next
            
        # the node where they meet is the beginning of the loop cycle   
        return slow_ptr

def main():

	# create linked list 
	A = LinkedList(1)

	A.next = LinkedList(2)

	A.next.next = LinkedList(3)

	A.next.next.next = LinkedList(4)

	# cycle created. node 4 points back to node 3
	A.next.next.next.next = A.next.next 

	#Find list cycle 
	cycle_start_node = ListCycle().detectCycle(A)

	print cycle_start_node.val if cycle_start_node is not None else "No Cycle Detected"


if __name__ == '__main__':
	main()