#!/usr/bin/env python
# coding: utf-8

# <h1>Python Hash Table/Map - Dictionaries</h1>

# <h5>Python implements hash table/map using an in-built data structure called dictionary, i.e. Dictionary is the Python specific implementation of hash table/map.</h5>

# <h2>Array vs Hash Table/Map</h2>

# Suppose we want to create a data structure in which we can store data in the format of key-value pairs, where the value can be accessed based on the key.
# 
# <u>Example:</u> We want to store the stock prices of a share for a week and want to look up the value based on the date.

# <h3>Array Implementation of the problem</h3>

# In[1]:


#Initialise array with date and stock prices

stock_prices = [
    ["march 6", 310.0],
    ["march 7", 340.0],
    ["march 8", 380.0],
    ["march 9", 302.0],
    ["march 10", 297.0],
    ["march 11", 323.0]
]

stock_prices


# Here we have created a 2D array/list, where each day's data is a sub-list in which the first element (index 0) is the date the second element (index 1) is the price of the stock on that particular day.
# 
# <b>What is the complexity to find the value of a particular key using an array?</b>
# 
# Or to put it simply, what is the time complexity to retrieve the price of our stock on "march 9"?

# In[2]:


#Retrieve price of stock on "march 9"

for stock_price in stock_prices:
    if stock_price[0] == "march 9":
        print(stock_price[1])
        break


# <b><font color = "red">The time complexity of the solution is <u>O(n)</u>.</b>
#     
# <b>Can the complexity be reduced using an alternate data structure?</b>
# 
# <h5><font color = "green">In Python, there is a data structure called dictionary which can retrieve the price in O(1) time complexity, i.e. in constant time.</h5>

# <h3>Dictionary implementation of the problem</h3>

# In[3]:


#Initialise dict() with date and stock prices

stock_prices = {
    "march 6": 310.0,
    "march 7": 340.0,
    "march 8": 380.0,
    "march 9": 302.0,
    "march 10": 297.0,
    "march 11": 323.0
}

stock_prices


# In[4]:


#Retrieve price of stock on "march 9"

stock_prices["march 9"]


# <b><font color = "green">The time complexity of the retrieval from the dictionary in this case is <u>O(1)</u>.</b>
#     
# The under-lying data structure of a dictionary is a hash table/map. Let us discuss implement of a hash table in Python.

# <h3>Array Memory Presentation</h3>

# When we store data in a 2D array (list), in the memory they reside in contiguous memory locations on the RAM.
# 
# <u>Example:</u> In this case of storing stock prices by date in the above 2D array, the memory representation would be something like:
# 
# <img align="left" src="2D Array Memory Presentation.png" alt="2D Array Memory Presentation" style="height:300px;">

# <h3>Dictionary (Hash Table/Map) Memory Presentation</h3>

# In hash table/map, have first take a 1D array of say, size 'n'. For simplicity purpose, let us consider an array of size 10, i.e. n = 10. Now every key in our hash map is passed through a hash function (in details later), which returns a specific integer value, 'k'. The value associated with the specific key is then stored at the index 'k' which was returned by the hash function.
# 
# <img align="left" src="Hash Table Mapping.png" alt="Hash Table Mapping" style="height:300px;">

# So, just like a normal array uses index to access it's elements, a hash table/map uses the key to access it's elements.
# 
# <img align="left" src="Hash Table Index.png" alt="Hash Table Index" style="height:300px;">

# <h2>Hash Function<h2>
#     
# <img align="left" src="Hash Function.png" alt="Hash Function" style="width:300px;">

# There are multiple ways of implementing hash functions, let us look at a simple one using ASCII values.
# 1. Here we first take each character (including spaces) of the key and find the sum of their ASCII values.
# 2. Since we need the index (at which we want to store the key's value) within the range of the array size, we do a mod (%) operation on the sum of ASCII values by the size of the array.
# 
# <a href="https://www.geeksforgeeks.org/hash-functions-and-list-types-of-hash-functions/" target="_blank">Click here</a> for more on <b><u>Hash Functions and list/types of Hash functions</u></b> from GFG.
# 
# <img align="left" src="Hash Function Implementation.png" alt="Hash Function Implementation" style="height:450px;">

# <i>
# <b>
#     Thus, time complexity for lookup for key is O(1) - amortized. <br>
#     Also, time complexity for insertion/deletion is also O(1) - amortized.
# </b>
# </i>

# In Python, we make use of the odr() fucntion to get the ASCII value of characters.

# In[3]:


print("ASCII value of A-Z is in the range from", ord('A'), "to", ord('Z'))
print("ASCII value of a-z is in the range from", ord('a'), "to", ord('z'))


# <h3>Hash Function Implementation</h3>

# In[4]:


def get_hash(key):
    h = 0
    for c in key:
        h += ord(c)
        
    return h % 100 #Considering array has 100 elements (0-99)


# In[5]:


get_hash("march 6")


# <h2>Hash Table/Map Implementation</h2>

# In[7]:


class HashTable:
    def __init__(self):
        self.MAX = 100 #Specifying array size
        self.arr = [None for i in range(self.MAX)] #Initilise array of self.MAX size using List Comprehension - list of 100 None (index 0 to 99). ##List Comprehension --> [0 for x in range(n)]
        
    def get_hash(self, key):
        h = 0
        for c in key:
            h += ord(c)
        
        return h % self.MAX


# In[8]:


t = HashTable() #Create an object of class HashTable ##__init__(self) class constrcutor is invoked
t.get_hash("march 6")


# Now, we have successfully created a hash function which returns a value for our key within the bounds of the array indices in which we want to store the values. Next, we need:
# 1. Function to add/remove an the key's value to the array index returned by the hash function (Insertion/Deletion) - set_item(key, value) and delete_item(key)
# 2. Function to get the value from the array index returned by the hash function (Look-up/Access) - get_item(key)

# <b><i>More specifically, we want to add an item in our hash table/map using a statement like: <br>
#     t.add("march 6", 130) <br>
#     and retriece the value from the table/map using a statement like: <br>
#     t.get("march 6") </i></b>

# In[30]:


#Create the insertion/addition function

class HashTable:
    def __init__(self):
        self.MAX = 100 #Specifying array size
        self.arr = [None for i in range(self.MAX)] #Initilise array of self.MAX size using List Comprehension - list of 100 None (index 0 to 99). ##List Comprehension --> [0 for x in range(n)]
        
    def get_hash(self, key):
        h = 0
        for c in key:
            h += ord(c)
        
        return h % self.MAX
    
    def add(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value


# In[31]:


t = HashTable()
t.add("march 6", 130)


# In[32]:


#Let us see what happened to our array
print(t.arr)


# <b><i>We can see 130 is inserted at index 9.</i><b>

# In[12]:


#Create the look-up/retrieval function

class HashTable:
    def __init__(self):
        self.MAX = 100 #Specifying array size
        self.arr = [None for i in range(self.MAX)] #Initilise array of self.MAX size using List Comprehension - list of 100 None (index 0 to 99). ##List Comprehension --> [0 for x in range(n)]
        
    def get_hash(self, key):
        h = 0
        for c in key:
            h += ord(c)
        
        return h % self.MAX
    
    def add(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value
        
    def get_value(self, key):
        h = self.get_hash(key)
        return self.arr[h]


# In[13]:


t = HashTable()
t.add("march 6", 130)


# In[15]:


t.get_value("march 6")


# In[17]:


t.get_value("march 7") #Not inserted yet


# We can see <b>get_value("march 6")</b> returned <b>130</b> and <b>get_value("march 7")</b> returned <b>None</b>.

# <b><i>What if we could perform the same actions in a more convenient way, like: <br>
#     t["march 6"] = 130, and, <br>
#     t["march 6"] would have returned 130? </i><b>

# <b><i><font color="green">Fortunately, Python operators supports this. We will implement the same below:</i></b>
#     
# <a href="https://docs.python.org/3/library/operator.html" target="_blank">Click here</a> for more on <b><u>Standard operators as functions</u></b> from Python Docs.

# In[33]:


#Use Python standard operators to make functionality more convenient

class HashTable:
    def __init__(self):
        self.MAX = 100 #Specifying array size
        self.arr = [None for i in range(self.MAX)] #Initilise array of self.MAX size using List Comprehension - list of 100 None (index 0 to 99). ##List Comprehension --> [0 for x in range(n)]
        
    def get_hash(self, key):
        h = 0
        for c in key:
            h += ord(c)
        
        return h % self.MAX
    
    def __setitem__(self, key, value): #Just replaced add with __setitem__
        h = self.get_hash(key)
        self.arr[h] = value
        
    def __getitem__(self, key): #Just replaced add with __getitem__
        h = self.get_hash(key)
        return self.arr[h]


# In[34]:


t = HashTable()
t["march 6"] = 130 #Invokes __setitem__ ##See Python Docs for understanding how.


# In[35]:


t["march 6"] #Invokes __getitem__ ##See Python Docs for understanding how.


# In[36]:


t["march 1"] = 20
t["dec 17"] = 27


# In[37]:


#Let us see what happened to our array
print(t.arr)


# <b><i>We can see all the values we inserted at index returned by the hash function for their particular key.</i></b>

# In[24]:


t["dec 17"]


# In[25]:


t["december 17"] #Not a valid key that in inserted or set yet ##Should return "None"


# In[26]:


t["march 1"]


# In[27]:


#Delete existing value based on key using Python Standard Operators

class HashTable:
    def __init__(self):
        self.MAX = 100 #Specifying array size
        self.arr = [None for i in range(self.MAX)] #Initilise array of self.MAX size using List Comprehension - list of 100 None (index 0 to 99). ##List Comprehension --> [0 for x in range(n)]
        
    def get_hash(self, key):
        h = 0
        for c in key:
            h += ord(c)
        
        return h % self.MAX
    
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value
        
    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None #Update the value of the index returned by for the key to "None"


# In[29]:


t = HashTable()
t["march 6"] = 130
t["march 1"] = 20
t["dec 17"] = 27

print("Before deleting:", t.arr)
print()

#Delete entry of "march 6"
del t["march 6"]
print("After deleting:", t.arr) #130 should be absent


# <b><i>We can see 130 missing at index 9 after deletion.</i><b>

# <h2>Collision Handling in Hash Table/Map</h2>

# <b><i>A collision, or more specifically, a hash code collision in a Hash Table/Map, is a situation where two or more key objects produce the same final hash value and hence point to the same bucket location or array index.</i></b>
# 
# <u>Example:</u> (dog, god), (cat, act), (tab, bat) are only examples of words with the same set of characters. Certainly the sum of the ASCII numbers for their characters will be similar if we follow the hashing based on ASCII number addition technique. Secondly, not just for words with similar characters, but based on the hash function used to accomodate the key-value mapped elements within a fixed array size, there can be scenarios where two or more key objects produce the same final hash value and hence point to the same bucket location or array index.

# <img align="left" src="Hash Table Collision.png" alt="Hash Table Collision" style="height:300px;">

# <h4>Let's see the issue with a code</h4>

# In[5]:


#Code which does not handle Hash Table/Map Collisions

class HashTable:
    def __init__(self):
        self.MAX = 10 #Specifying array size
        self.arr = [None for i in range(self.MAX)] #Initilise array of self.MAX size using List Comprehension - list of 10 None (index 0 to 9). ##List Comprehension --> [0 for x in range(n)]
        
    def get_hash(self, key):
        h = 0
        for c in key:
            h += ord(c)
        
        return h % self.MAX
    
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value
        
    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


# In[6]:


t = HashTable()


# In[7]:


t.get_hash("march 6")


# In[8]:


t.get_hash("march 17")


# We notice, with our hash function implementation, both our key objects, "march 6" and "march 17", return index 9 to place their respective values in.

# In[9]:


t["march 6"] = 120
t["march 8"] = 67
t["march 9"] = 24


# In[10]:


t["march 6"]


# In[11]:


t["march 17"] = 459


# In[12]:


t["march 17"]


# In[13]:


t["march 6"] #Should return wrong value - 459, and not 120


# <b><i><font color="red">The value being returned for "march 6" is not 120 which is wrong. Instead it returned 459 for "march 6" which is actually the value for key "march 17" as both the key objects mapped to the same array index in our hash function implementation.</i></b>

# <b><i>The value at index 9 of the array is updated from 120 to 459</i></b>
# 
# <img align="left" src="Hash Collision Replacement.png" alt="Hash Collision Replacement" style="height:300px;">

# <b>How do we handle such collisions?</b>
# 
# <b><i><font color="green">Of many available ways of handling Hash Table/Map Collision, we will look at Chaining/Separate Chaining (preffered way of handling Hash Table/Map collision) and Probing (Linear and Quadratic).</i></b>

# <h3>Chaining/Separate Chaining</h3>

# <i>In chaining/separate chaining, instead of directly storing the element at the index returned by the hash function for the key object, we store a Linked List (in Python, we can use normal lists and store keys and their values as tuples treating them as individual elements in the list) at each index and keep adding new nodes/tuples at the end of the existing list at that index. This way, the list at each index can keep growing and multiple keys can share the same hash value.</i>

# <i>
# <b>The amortized average case time complexity Θ(1)which is a constant time operation, however, the worst case time complexity can go upto O(n).</b>
#     
# <u>Explanation:</u> Imagine a bad hashing function, where all the keys generate the same hash value pointing to the same index, we will have all the elements in a bucket in one index and it will act as a long Linked List. In that case, the search complexity will be same as that of a Linked List, which is O(n).
# </i>

# <b><i>In chaining/separate chaining, it is important to store both the key (at index 0) and the value (at index 1) within a sub-datastructure as a single element at the end of the index returned by the hash function as there can be multiple key-value pairs at a single array index.</i></b>

# <h3>Implementation of Hash Table/Map Collision handling using Chaining/Separate Chaining</h3>

# In[15]:


#Handle Hash Table/Map Collisions using Chaining/Separate Chaining while insering key-value pairs by avoiding
#overwriting

#First change - Use sub-list at each array index which can store multiple tuples

#Second change - When we were not handling collisions, we used to replace the value at index returned by the hash
#function. Now, we have a list at that index and we need to keep appending the latest key-value pair to end of the
#list at that index

class HashTable:
    def __init__(self):
        self.MAX = 10 #Specifying array size
        self.arr = [[] for i in range(self.MAX)] #List of 10 empty lists (index 0 to 9) where every sub-list can contain multiple tuples because we can not store just the value but also need to store the key for look-up as each index might have multiple values
                                                 #Initilise array of self.MAX size using List Comprehension. ##List Comprehension --> [0 for x in range(n)]
        
    def get_hash(self, key):
        h = 0
        for c in key:
            h += ord(c)
        
        return h % self.MAX
    
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        #Scenario - self.arr[h] now contains a list to which we need to do either of the following:
        #Case 1 - Update the value of the key if the key already exists
        #Case 2 - Append a new key-value pair to the end if the key doesn't exist in the list
        
        found = False #Used as flag for checking if key already exists in a tuple in the array index
        
        #Case 1 implementation
        for i, element in enumerate(self.arr[h]):
            if element[0] == key:
                self.arr[h][i] = (key, value)
                #We are inserting the key-value pairs in tuples. Tuples are immutable, so we cannot do:
                #element[1] = value
                #Instead of tuple, had we used another array/list, it would have worked.
                found = True
        
        #Case 2 implementation
        if not found:
            self.arr[h].append((key, value))


# In[16]:


t = HashTable()
print(t.arr)


# In[17]:


t["march 6"] = 120
t["march 8"] = 67
t["march 9"] = 4
print(t.arr)


# In[18]:


t["march 17"] = 459 #Adding "march 17" in the sub-list at index 9 with "march 6"
print(t.arr)


# In[19]:


t["march 6"] = 78 #Updating the value for key "march 6"
print(t.arr)


# In[20]:


#Modify Hash Table/Map retrieval when each array index has multiple key-value pairs

#We iterate through all the element at the array index returned by the hash function and match the key with the key
#present in the tuple (index 0 of element) and return the value of that particular element (index 1 of element)


class HashTable:
    def __init__(self):
        self.MAX = 10 #Specifying array size
        self.arr = [[] for i in range(self.MAX)] #List of 10 empty lists (index 0 to 9) where every sub-list can contain multiple tuples because we can not store just the value but also need to store the key for look-up as each index might have multiple values
                                                 #Initilise array of self.MAX size using List Comprehension. ##List Comprehension --> [0 for x in range(n)]
        
    def get_hash(self, key):
        h = 0
        for c in key:
            h += ord(c)
        
        return h % self.MAX
    
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        #Scenario - self.arr[h] now contains a list to which we need to do either of the following:
        #Case 1 - Update the value of the key if the key already exists
        #Case 2 - Append a new key-value pair to the end if the key doesn't exist in the list
        
        found = False #Used as flag for checking if key already exists in a tuple in the array index
        
        #Case 1 implementation
        for i, element in enumerate(self.arr[h]):
            if element[0] == key:
                self.arr[h][i] = (key, value)
                #We are inserting the key-value pairs in tuples. Tuples are immutable, so we cannot do:
                #element[1] = value
                #Instead of tuple, had we used another array/list, it would have worked.
                found = True
        
        #Case 2 implementation
        if not found:
            self.arr[h].append((key, value))
            
    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]


# In[21]:


t = HashTable()
t["march 6"] = 120
t["march 8"] = 67
t["march 9"] = 4
t["march 17"] = 459


# In[22]:


print(t.arr)


# In[9]:


t["march 6"]


# In[10]:


t["march 8"]


# In[11]:


t["march 9"]


# In[12]:


t["march 17"]


# In[13]:


t["march 6"] = 78 #Update value of "march 6"


# In[14]:


t["march 6"]


# In[24]:


#Modify Hash Table/Map key-value pair deletion when each array index has multiple key-value pairs

class HashTable:
    def __init__(self):
        self.MAX = 10 #Specifying array size
        self.arr = [[] for i in range(self.MAX)] #List of 10 empty lists (index 0 to 9) where every sub-list can contain multiple tuples because we can not store just the value but also need to store the key for look-up as each index might have multiple values
                                                 #Initilise array of self.MAX size using List Comprehension. ##List Comprehension --> [0 for x in range(n)]
        
    def get_hash(self, key):
        h = 0
        for c in key:
            h += ord(c)
        
        return h % self.MAX
    
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        
        for i, element in enumerate(self.arr[h]):
            if element[0] == key:
                self.arr[h][i] = (key, value)
                found = True
                break
                
        if not found:
            self.arr[h].append((key, value))
            
    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
            
    def __delitem__(self, key):
        h = self.get_hash(key)
        for i, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][i]


# In[29]:


t = HashTable()
t["march 6"] = 120
t["march 8"] = 67
t["march 9"] = 4
t["march 17"] = 459
t["march 6"] = 78


# In[30]:


print(t.arr)


# In[31]:


t["march 6"]


# In[32]:


del t["march 6"]
print(t.arr)


# In[34]:


t["march 6"] #Return "None", i.e. No Output


# In[35]:


t["march 9"]


# In[36]:


del t["march 8"]
print(t.arr)


# <h2>Exercise 1</h2>
# 
# nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following:<br>
# 
# 1. What was the average temperature in first week of Jan?<br>
# 2. What was the maximum temperature in first 10 days of Jan?<br>
# 
# Figure out data structure that is best for this problem.

# In[45]:


#This problem can be solved using lists/arrays

temp = list()

with open("nyc_weather.csv", "r+") as file:
    for line in file:
        try:
            t = int((line.split(","))[1])
            temp.append(t)
        except:
            pass
    
print(temp)


# In[46]:


#1
sum(temp[:7])/len(temp[:7])


# In[47]:


#2
max(temp[:10])


# <h2>Exercise 2</h2>
# 
# nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following: <br>
# 
# 1. What was the temperature on Jan 9?<br>
# 2. What was the temperature on Jan 4?<br>
# 
# Figure out data structure that is best for this problem

# In[48]:


#Best data structure for solving this problem is hash table/map. We will use Python dictionary.

temp = dict()

with open("nyc_weather.csv", "r+") as file:
    for line in file:
        try:
            d = (line.split(","))[0]
            t = int((line.split(","))[1])
            temp[d] = t
        except:
            pass
    
print(temp)


# In[49]:


#1
temp["Jan 9"]


# In[50]:


#2
temp["Jan 4"]


# <h2>Exercise 3</h2>
# 
# poem.txt Contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in python and print every word and its count as show below. Think about the best data structure that you can use to solve this problem and figure out why you selected that specific data structure. <br>
# 
# 'diverged': 2,<br>
# 'in': 3,<br>
# 'I': 8

# In[56]:


word_count = dict()

with open("poem.txt", "r+") as file:
    for line in file:
        words = line.split()
        for word in words:
            word = word.replace("\n","")
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
                
word_count


# <h3>Probing</h3>

# <i>The alternate approach of handling Hash Table/Map collisions is using Probing (Linear and Quadratic), Doble Hashing and Open Addressing. With each of these individual approaches have their respective pros and cons when weighed against each other, we will only implement Linear Probing considering it's ease in implementation over the rest. </i>
# 
# <a href="https://www.geeksforgeeks.org/hashing-set-3-open-addressing/" target="_blank">Click here</a> for detailed description of each of the collision handling techniques from GFG.

# <b><i>In linear probing, the hash table is searched sequentially that starts from the original location of the hash. If in case the location that we get is already occupied, then we check for the next location.</i></b>
# 
# The function used for rehashing is as follows: <b><u>get_hash(key) = (n+1) % self.MAX</u></b> until an empty index is returned by the get_hash(key) function.

# <h3>Implementation of Hash Table/Map Collision handling using Linear Probing</h3>

# In[116]:


class HashTable:  
    def __init__(self):
        self.MAX = 10 # I am keeping size very low to demonstrate linear probing easily but usually the size should be high
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            element = self.arr[prob_index]
            if element is None:
                return
            if element[0] == key:
                return element[1]
           
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key,val)
        else:
            new_h = self.find_slot(key, h)
            self.arr[new_h] = (key,val)
        print(self.arr)
        
    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0,index)]
    
    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key:
                return prob_index
        raise Exception("Hashmap Overflow")
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return # item not found so return. You can also throw exception
            if self.arr[prob_index][0] == key:
                self.arr[prob_index] = None
        print(self.arr)


# In[117]:


t = HashTable()
t["march 6"] = 20
t["march 17"] =  88


# In[118]:


t["march 17"] = 29


# In[119]:


t["nov 1"] = 1


# In[120]:


t["march 33"] = 234


# In[121]:


t["dec 1"]


# In[122]:


t["march 33"]


# In[123]:


t["march 33"] = 999


# In[124]:


t["march 33"]


# In[125]:


t["april 1"] = 87


# In[126]:


t["april 2"] = 123


# In[127]:


t["april 3"] = 234234


# In[128]:


t["april 4"] = 91


# In[129]:


t["May 22"] = 4


# In[130]:


t["May 7"] = 47


# In[131]:


t["Jan 1"] = 0


# In[132]:


del t["april 2"]


# In[133]:


t["Jan 1"] = 0


# In[134]:


try:
    t["dec 31"] = 99
except Exception as e:
    print(e)


# <i>Here, once the initially initilised array is full, we are returning an exception stating, "Hashmap Overflow" for ease of implementation. However, in an actual implementation of Hash Table/Map, we were required to triple (increase by 2x) the size of the initial array, re-map the existing elements from the current array to the new array following the hash function's algorithm against the new size of the array, and finally insert the new element. This is a continuous process.</i>
