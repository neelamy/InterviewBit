# Source : https://www.interviewbit.com/problems/remove-nth-node-from-list-end/
# Remove Nth Node from List EndBookmark Suggest Edit

# Algo/DS : Linked List

# Complexity : O(n)

import LinkedListBasic as LL

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
         
            fast_ptr = A
          
            slow_ptr = None
 
            # move fast_ptr forward by B nodes
            for i in xrange(B):

            	fast_ptr = fast_ptr.next if fast_ptr else fast_ptr

            # if end reached then remove first node
            if fast_ptr is None: return A.next
            
            # Distance between slow_ptr and fast_ptr is now N+1
            # when fast_ptr reached end ie. None then slow_ptr will point to 
            # node before N
            slow_ptr = A
            
            while fast_ptr.next:
                
                fast_ptr = fast_ptr.next
                
                slow_ptr = slow_ptr.next
                
            #  slow_ptr points to N+1th node from end.Make it point to N-1th node
            slow_ptr.next = slow_ptr.next.next
            
            return A
                
            
def main():

    # create linked list A and B
    A = LL.LinkedListFunction()

    for i in [5,4,3,2,1]:

        A.push_in_list(i)

    print " A :" ,

    A.print_List() # 1 2 3 4 5  

    # Merge linked list. Create new linked list using the head returned by the function
    RemovedNthNode_list = LL.LinkedListFunction(Solution().removeNthFromEnd(A.head, 1))

    print " \n New List :" ,

    RemovedNthNode_list.print_List() # 1 2 3 4 


if __name__ == '__main__':
    main()