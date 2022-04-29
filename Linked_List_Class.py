@@ -1,138 +0,0 @@
class Node:
    """
        A class used to represent a Node from a linked list
    """
    
    def __init__(self, data):

        """
            Initialize the Node class. 

            data : str
                The value store in the Node
            next: Node
                The location to the consecutive Node 
        """

        self.data = data
        self.next = None
        
class Linked_List:
    """
        A class that is use to represent a list of Node items
    """
    DATA = []
    START = 0
    END = 1
    
    def __init__(self):
        """
            Initialize the Linked List class

            head : Node
                Initialize the head of the list
        """
        self.head = None
        
        
    def get_data_values(self, list_of_values):
        
        self.DATA = list_of_values
        
    def get_values(self):
        
                   
        value = self.DATA[self.START:self.END]
        value = value[0]
        self.START += 1
        self.END += 1
            
        return value
   
      
    def create_link_list_recursively(self, llist, value):
               
        # Create a new node everytime the method is called
        node = Node(value)
           
        # Check if it is the last person in the list
        if value == self.DATA[(len(self.DATA)-1)]:
            # If the last person set return the node
            return node
        else: 
            if llist.head == None:
                 llist.head = node
                 node.next = self.create_link_list_recursively(llist, self.get_values())
                 return node
            else:
                 node.next = self.create_link_list_recursively(llist, self.get_values())
                 return node

    def create_list(self):
        self.create_link_list_recursively(self,self.get_values())
        
    def get_a_node(self, item):
        
         # Create a node to move through the list and set it to the head of the list
        traverse = self.head
        found = None
        
        # If there are other nodes after display the data in each Node
        while traverse != None:
            # Check if the current node is equal to the value received
            if traverse.data == item:
                found = traverse
            
            traverse = traverse.next
            
        return found
    
    def delete_a_node(self, item):
        # Create a node to move through the list and set it to the head of the list
        traverse = self.head
        
        # Check if the data is found at head
        if traverse.data == item.data:
            # Set the head of the list to the next node
            self.head = traverse.next
        # If the data isn't at the head
        else:
            # Set the previous node to the head
            previous_node = self.head
            
            # Go through the list
            while traverse != None:
                
                # Check if the data entered matches the data at the current node
                if traverse.data == item.data:
                    # Set the previous node next pointer to the current node next pointer
                    previous_node.next = traverse.next
                   
                    break
            # If data is not in the current node
                else:
                    # Set the previous node to the current node
                    previous_node = traverse
                    # Set the current node to the current node's next node
                    traverse = traverse.next

                
                
    def print_linked_list(self, linked_list):

        """
           Print all the nodes in the list

           : param linked_list : Linked_List object
                List where all the nodes are stored
        """

        # Create a node to move through the list and set it to the head of the list
        traverse = linked_list.head
        
        # If there are other nodes after display the data in each Node
        while traverse != None:
            # Display current node data 
            print(traverse.data)
            # Set the next node 
            traverse = traverse.next
