# Linked List     
class Element:
    def __init__(self, value): 
        self.value = value  # node le represent garni value
        self.next = None # Next Node. Reference to the next element
        
class LinkedList:
    def __init__(self, head = None):
        self.head = head
        
    def append(self, new_element): # function to add new values in our linked list
        current = self.head       # start from head.
        if self.head:    # if head is not null
            while current.next:  # while there is a reference. Meaning there is a "While there is a next value"
                current = current.next
            current.next = new_element  # set reference of the tail to the new element (Apppending)
        else:
            self.head= new_element   #set new element as head. This is executed only when our linked list is empty
