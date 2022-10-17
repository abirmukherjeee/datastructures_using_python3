#!/usr/bin/env python
# coding: utf-8

# <h1>Python Linked Lists</h1>

# <i>
#     <b>Unlike Arrays (which stores elements in contiguous memory locations), Linked Lists store elements at random memory locations in the RAM, but every element contains a pointer to the next element.</b>
# 
# The data structure which stores a value and a pointer is called a <b><u>Node</u></b>.

# <h3>Issues of Arrays that Linked List tries to solve</h3>

# <h4>Insertion/Deletion is easier</h4>
# 
# 1. Time complexity of array insertion at by index, or at beginning or in the middle of the array is O(n). <br>
# 
#    This is because before insertion, at max n elements need to be shifted to the next memory location to make space for the insertion at the specified index, or in the worse case scenario if we use dynamic arrays (lists), all existing elements might need to be copied to a different memory location and the insertion needs to be performed if the existing allocated memory was exhausted. <br>
#    
#     Time complexity of insertion and deletion by index and/or before/after a value is <b>O(1)</b> in Linked Lists because we have to only edit the pointers of the new, previous and next node. <br>
#     
#     Time complexity of Linked List traversal is however <b>O(n)</b> in Linked Lists, so in insertion/deletion NOT at the beginning or end of the Linked List, i.e. insertion/deletion at the middle of the Linked List will first require traversal in O(n) time complexity and then insertion/deletion in O(1) time complexity. However, time complexity for insertion/deletion will remain O(1) and not get affected by time complexity of Linked List traversal, just like we do not consider complexity of sorting an array for performing Binary Search.
#     
# <u>Note:</u> Insertion/deletion of Array elements at the end can be done in O(1) time complexity, however in the worst case scenario, if we had exhausted the allocated memory space for the array, we might have to copy all existing array elements to the new space which changes the complexity to O(1). However, the amortized time complexity for array element insertion/deletion at the end is O(1).

# <h4>No memory leakage and pre-allocation of space not required</h4>
# 
# 2. Static arrays have fixed size and cannot be expanded. Dynamic arrays on the other hand can be expanded but might be under utilised and have plenty of memory leakage (also possible with static arrays if we initialise it with a very big size considering it cannot be expanded later). This makes arrays memory in-efiicient. <br>
# 
#    In case of insertion in Linked List, we can simply create a Node (without worrying about memory) and link it to the previous and next node with the help of pointers. In case of deletion, we simply remove the pointer of the previous and the next element from the Node and free up the space.

# <h3>Drawbacks of Linked List when compared to Arrays</h3>

# <h4>Element access by index</h4>
# 
# 1. Unlike arrays where element access by index is a constant time operation, i.e. O(1), Linked List element access by index is required <b><u>O(n)</u></b> time complexity.

# <h4>Size of memory utilised by Node is greater than that of individual array element objects</h4>
# 
# 2. Every Node contains pointer(s) in addition to the value that is contained in array elements.

# <h2>Time complexity of other Linked List operation</h2>

# <b><i>Time complexity for accessing Linked List element by value is <u>O(n)</u></i></b>

# <h2>Double Linked List</h2>

# <i>
#     Double Linked List is a data structure in which each node contains a pointer to it's previous node, in addition to the pointer of the next node and the value, thus making reverse traversal feasible.
# </i>

# <h2>Python Linked List implementation and basic operations</h2>

# In[3]:


class Node: #Represents an individual element in the Linked List
    def __init__(self, data = None, next = None): #Node class constrcutor with 2 parameters - Single Linked List
        self.data = data #Can contain integers, strings or complex objects
        self.next = next #Pointer to next element


# In[10]:


class LinkedList: #Creates the Linked List and contains functions for basic Linked List operations
    def __init__(self): #LinkedList class constuctor which initilizes the Linked List
        self.head = None #Variable which points to the head (first element) of the Linked List

    ##Operation 1 - Insert at beginning of Linked List
    def insert_at_beginning(self, data): #Single function parameter of data
        node = Node(data, self.head) #Creates a Node by passing 2 arguments - data for Node's data and the current Linked List head as the next element
        self.head = node #Make newly created node as head (first element) of Linked List
    ##T(n) = O(1)

    ##Operation 2 - Linked List traversal
    ##Utility function to print and verify Linked List operations
    def print_linked_list(self): #No input function parameters
        iterator = self.head #Temporary iterator variable for the Linked List

        if iterator is None: #Check if Linked List is empty
            print("Linked List is empty.")
            return

        ll_str = "" #Temporary string variable to append Linked List node data's in and print it for verification

        while iterator: #Keep iterating throught the Linked List until None (no more nodes left)
            ll_str += str(iterator.data) + " --> " #Append data of node to string followed by "-->" for visualisation
            iterator = iterator.next #Point iterator to next Linked List element

        print(ll_str)
    ##T(n) = O(n)
        
    ##Operation 3 - Insert at end of Linked List
    def insert_at_end(self, data): #Single function parameter of data
        node = Node(data, None) #Creates a Node by passing 2 arguments - data for Node's data and pointer to the next element is None because this node is the last element. No elements after this element.
        iterator = self.head #Temporary iterator variable for the Linked List
        
        if iterator is None: #Check if Linked List is empty
            self.head = node #Insert at head, i.e. if Linked List is empty and element to be inserted at end is same as element to be inserted at beginning because there is only one element.
            return
        
        while iterator.next: #Keep iterating throught the Linked List until None (no more nodes left)
            iterator = iterator.next #Point iterator to next Linked List element
        #Post the completion of the while loop, iterator points at last existing element of the Linked List
        #Linked List traversal T(n) = O(n)
        
        iterator.next = node #Insert new node as next element of existing last element of Linked List
    ##T(n) = O(n) if we consider Linked List traversal as part of insertion at the end as traveral time is linearly related to the input size
    ##T(n) = O(1) if we consider only updating pointers the action of insertion at the end as updating pointers is a constant time operation and has no relation to the input size
        
    ##Operation 4 - Create new Linked List from Python array/list
    def new_ll_from_list(self, data_list): #List function parameter of containing data of nodes
        self.head = None #Create new head pointer for new Linked List
        
        for data in data_list: #Iterate over list elements
            self.insert_at_end(data) #Function call to insert element with data at end of Linked List
    ##Linked List creation from list T(n) = O(n)
            
    ##Operation 5 - Linked List traversal
    ##Utility function to get the length of Linked List elements
    def get_length(self): #No input function parameters
        count = 0 #Temporary variable to update count of Linked List element as we iterate over Linked List
        itr = self.head #Temporary iterator variable for the Linked List
        
        while itr: #Keep iterating throught the Linked List until None (no more nodes left)
            count += 1 #Keep updating count for each new element of Linked List
            itr = itr.next #Point iterator to next Linked List element
            
        return count
    ##T(n) = O(n)
    
    ##Operation 6 - Remove from given index of Linked List
    def remove_at_index(self, index): #Single function parameter of index at which element needs to be removed
        if index < 0 or index >= self.get_length(): #Check if index is valid
            raise Exception("Invalid Index to remove data from.")
            
        if index == 0: #If head has to be removed
            self.head = self.head.next #Makes next element of existing head as new head
            return
        
        itr = self.head #Temporary iterator variable for the Linked List
        count = 0 #Index counter
        
        while itr: #Keep iterating throught the Linked List until None (no more nodes left)
            if count == index - 1: #If we reach the element whose next element has to be removed
                itr.next = itr.next.next #Update the next of the previous element as the next of the current element
                break
            
            itr = itr.next #Point iterator to next Linked List element
            count += 1 #Keep updating index
    ##T(n) = O(n) if we consider Linked List traversal as part of removal of element by index as traveral time is linearly related to the size of the existing Linked List and can be 'n' in the worst case scenario
    ##T(n) = O(1) if we consider only updating pointers the action of removal of element by index as updating pointers is a constant time operation and has no relation to the size of the existing Linked List

    ##Operation 7 - Insert at given index of Linked List
    def insert_at_index(self, index, data): #2 function parameter - the data of the element which needs to be inserted and the index at which it should ne inserted
        if index < 0 or index >= self.get_length(): #Check if index is valid
            raise Exception("Invalid index to insert data at.")
            
        if index == 0: #If element needs to be inserted at head
            self.insert_at_beginning(data) #Call insert at beginning function passing data as function argument
            
        count = 0 #Index counter
        itr = self.head #Temporary iterator variable for the Linked List
        
        while itr: #Keep iterating throught the Linked List until None (no more nodes left)
            if count == index - 1: #If we reach the element after which the new element needs to be inserted
                node = Node(data, itr.next) #Create a node with the data and next element pointing to the next of previous element
                itr.next = node #Insert new node as next node of the previous index element
                break
            
            itr = itr.next #Point iterator to next Linked List element
            count += 1 #Keep updating index
    ##T(n) = O(n) if we consider Linked List traversal as part of insertion of element at index as traveral time is linearly related to the size of the existing Linked List and can be 'n' in the worst case scenario
    ##T(n) = O(1) if we consider only updating pointers the action of insertion of element by index as updating pointers is a constant time operation and has no relation to the size of the existing Linked List

    def insert_after_value(self, value, data):
        itr = self.head
        
        if not itr:
            print("Linked List is empty.")
            return
        
        while itr:
            if itr.data == value:
                node = Node(data, itr.next)
                itr.next = node
                break
                
            if not itr.next:
                print("Node with value not present in Linked List.")
                break
            
            itr = itr.next
            
    def remove_by_value(self, value):
        itr = self.head
        
        if not itr:
            print("Linked List is empty.")
            return
        
        if itr.data == value:
            self.head = self.head.next
        
        while itr.next:
            if itr.next.data == value:
                itr.next = itr.next.next
                break
                
            if not itr.next.next:
                if itr.next.data != value:
                    print("Node with value not present in Linked List.")
                    break
                
            itr = itr.next


# In[11]:


#Driver code

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(5) #5 -->
    ll.insert_at_beginning(50) #50 --> 5 -->
    ll.insert_at_end(500) #50 --> 5 --> 500 -->
    ll.print_linked_list()
    print("Length: " + str(ll.get_length()))
    ll.new_ll_from_list(["apple", "banana", "cucumber", "donut"]) #apple --> banana --> cucumber --> donut -->
    ll.print_linked_list()
    print("Length: " + str(ll.get_length()))
    ll.remove_at_index(1) #apple --> cucumber --> donut -->
    ll.print_linked_list()
    print("Length: " + str(ll.get_length()))
    
    #Intentionally raising exception
    try:
        ll.remove_at_index(10) #Invalid Index to remove data from.
    except Exception as e:
        print(e)
        
    ll.insert_at_index(0, "figs") #figs --> apple --> cucumber --> donut -->
    ll.insert_at_index(2, "jackfruit") #figs --> apple --> jackfruit --> cucumber --> donut -->
    ll.print_linked_list()
    print("Length: " + str(ll.get_length()))
    
    ll.insert_after_value("apple", "guava") #figs --> apple --> guava --> jackfruit --> cucumber --> donut -->
    ll.print_linked_list()
    ll.insert_after_value("grapes", "mango") #Node with value not present in Linked List.
    
    ll.remove_by_value("cucumber") #figs --> apple --> guava --> jackfruit --> donut --> 
    ll.print_linked_list()
    ll.remove_by_value("mango") #Node with value not present in Linked List.


# <h2>Python Doubly Linked List implementation and basic operations</h2>
# 
# <h3>Exercise</h3>
# 
# Implement doubly linked list. The only difference with regular linked list is that double linked has prev node reference as well. That way you can iterate in forward and backward direction. Your node class will look this this:
# 
# class Node: <br>
#     def __init__(self, data=None, next=None, prev=None): <br>
#         self.data = data <br>
#         self.next = next <br>
#         self.prev = prev <br>
#         
# Add following new methods: <br>
# 
# def print_forward(self): <br>
#     # This method prints list in forward direction. Use node.next for this. <br>
# 
# def print_backward(self): <br>
#     # Print linked list in reverse direction. Use node.prev for this. <br>
#     
# Implement all other methods in regular linked list class and make necessary changes for doubly linked list (you need to populate node.prev in all those methods)

# In[66]:


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        
class DoubleLinkedList:
    def __init__(self):
        self.head = None

        
            
        
    def get_length(self):
        count = 0
        itr = self.head
        
        while itr:
            count += 1
            itr = itr.next
            
        return count
    
        
    def print_forward(self):
        itr = self.head
        
        if not itr:
            print("Doubly Linked List is empty.")
            return
            
        ll_str = ""
        
        while itr:
            ll_str += str(itr.data) + " <--> "
            itr = itr.next
            
        print(ll_str)
        
        
    def get_tail(self):
        itr = self.head
        
        while itr.next:
            itr = itr.next
            
        return itr


    def print_backward(self):
        if not self.head:
            print("Doubly Linked List is empty.")
            return
        
        tail = self.get_tail()
        ll_str = ""
        
        while tail:
            ll_str += str(tail.data) + " <--> "
            tail = tail.prev
            
        print(ll_str)


    def insert_at_beginning(self, data):
        node = Node(data, self.head, None)
        
        if self.head:
            self.head.prev = node
            
        self.head = node

    
    def insert_at_end(self, data):
        if not self.head:
            self.head = Node(data, None, None)
            return
        
        tail = self.get_tail()
        
        tail.next = Node(data, None, tail)
        
        
    def insert_at_index(self, index, data):
        if index < 0 or index > self.get_length():
            print("Invalid index to insert at.")
            return
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        itr = self.head
        
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if itr.next:
                    itr.next.prev = node
                itr.next = node
                break
            
            count += 1
            itr = itr.next
            
            
    def remove_from_index(self, index):
        if index < 0 or index > self.get_length():
            print("Invalid index to insert at.")
            return
        
        if not self.head:
            print("Linked list empty.")
            return
        
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
        
        itr = self.head
        count = 0
        
        while itr:
            if count == index - 1:
                if itr.next.next:
                    itr.next.next.prev = itr
                    
                itr.next = itr.next.next
                
                break
            
            count += 1
            itr = itr.next
            
            
    def insert_from_list(self, arr):
        self.head = None
        
        for a in arr:
            self.insert_at_end(a)


if __name__ == '__main__':
    dll = DoubleLinkedList()
    dll.insert_at_beginning(5)
    dll.print_forward()
    dll.print_backward()
    print("Length:",dll.get_length())
    dll.insert_at_beginning(50)
    dll.insert_at_beginning(500)
    dll.insert_at_end(100)
    dll.print_forward()
    dll.print_backward()
    print("Length:",dll.get_length())
    dll.insert_at_index(4,200)
    dll.insert_at_index(1,700)
    dll.print_forward()
    dll.print_backward()
    print("Length:",dll.get_length())
    dll.insert_from_list(["Apple", "Samsung", "Tesla", "DS", "Algo"])
    dll.print_forward()
    dll.print_backward()
    print("Length:",dll.get_length())
    dll.remove_from_index(0)
    dll.print_forward()
    dll.print_backward()
    print("Length:",dll.get_length())
    dll.remove_from_index(3)
    dll.print_forward()
    dll.print_backward()
    print("Length:",dll.get_length())

