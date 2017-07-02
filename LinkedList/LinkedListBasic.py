# Basic functions of linked list



class ListNode:

	def __init__(self, x):

		self.val = x

		self.next = None

class LinkedListFunction:

	def __init__(self, head = None):

		self.head = head

	def push_in_list(self, data):

		new_node = ListNode(data)

		new_node.next = self.head

		self.head = new_node

	def print_List(self):

		temp = self.head

		while temp:

			print temp.val ,

			temp = temp.next



if __name__ == '__main__':
	main()