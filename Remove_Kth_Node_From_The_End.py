"""Remove Kth node from the end of Linked List"""
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
	next_node = head.next
	node_to_delete = head
	current_node_number = 2
	candidate_to_delete = 1
	while next_node.next is not None:
		if (current_node_number-candidate_to_delete) == (k):
			node_to_delete = node_to_delete.next
			candidate_to_delete +=1
		next_node = next_node.next
		current_node_number+=1
	if current_node_number == k:
		head.value, head.next = head.next.value, head.next.next
	elif current_node_number != k:
		node_to_delete.next = node_to_delete.next.next