#!/usr/bin/env python
# coding: utf-8

# <h1>Python Lists</h1>

# <i>
# <b>Python lists are dynamic arrays which store objects in contiguous memory locations.</b>
#
# <u>Note:</u> Unlike Java and C++, in which we can store only items of similar data types in arrays (homogeneous), Python lists are heterogeneous in nature as each array element is treated as an object.
# </i>

# <h2>Operations on Python Lists</h2>

# <h3>Initialise a list with prices of a stock for a week</h3>




stock_prices = [98, 100, 103, 101, 102, 99, 101]


# <h3>Access elements</h3>

# <i>Index starts with 0</i>




#Price on Day 1
stock_prices[0]





#Price on Day 3
stock_prices[2]


# <i>
# <b>Access or look-up time complexity for array elements by index is O(1).</b>
#
# <u>Explanation:</u> The array name variable points to the address of only the first array element (index 0 address - referred to as "base_address" of the array). Based on the index we specify, the element is accessed by, <b>element_address = base_address + (specified_index * size_of_each_element)</b> which is a contsant time operation.
# </i>

# <h3>Search and/or access by value</h3>




#Linear Search - O(n)
def linear_search(stock_prices, n):
    for i, stock_price in enumerate(stock_prices):
        if stock_price == n:
            return i

    return 0

#Binary Search - O(log n)
def binary_search(stock_prices, n):
    l, h = 0, (len(stock_prices) - 1)

    while l <= h:
        mid = (l + h) // 2

        if stock_prices[mid] == n:
            return mid

        elif stock_prices[mid] > n:
            h = mid - 1

        elif stock_prices[mid] < n:
            l = mid + 1

    return 0

#Driver code
stock_prices = [98, 100, 103, 101, 102, 99, 101]
n = int(input("Enter element to search: "))

print("\nLinear Search:")
if linear_search(stock_prices, n):
    print("Stock price was", n, "on day",  (linear_search(stock_prices, n) + 1))
else:
    print("Stock price was never" + str(n) + "in the given week's stock prices.")

print("\nBinary Search:")
if binary_search(sorted(stock_prices), n):
    print("Stock price was", n, "on one of the days in the given week's stock prices. Can not comment on which day as stock_prices was sorted for binary_search to perform successfully and the original order of stock_prices with respect to day has been lost.")
    print("Stock price was", n, "at position",  (binary_search(sorted(stock_prices), n) + 1), "in sorted list.")
else:
    print("Stock price was never", n, "in the given week's stock prices.")


# <i>
# <b>
# Access or look-up time for array index by value, or, search for existence of array element or array index, is O(n) for unsorted data - <u>Linear Search</u><br>
#
# Search for exitence of array element or array index by value is O(log n) for SORTED data - <u>Binary Search</u>
# </b>
# </i>

# <h3>Array Traversal</h3>




for stock_price in stock_prices:
    print(stock_price)


# <i>
# <b>Array traversal time complexity is O(n).</b>
# </i>

# <h3>Insert element at given index</h3>




#Insert new price 97 in stock_prices at index 1
#Syntax - array_name.insert(index_to_insert_into, value_to_insert)

stock_prices = [98, 100, 103, 101, 102, 99, 101]
stock_prices.insert(1, 97)
stock_prices


# <i>
#     <b>
#         Insertion element at given index time complexity is O(n).
#     </b>
#
# <u>Explanation:</u> Once we insert at element at a given position, we need to copy all the following elements to the next memory location. Since at most, we might need to move n elements, thus worst case time complexity is O(n).
# </i>

# <h3>Delete element by value and/or index</h3>




#Remove by value - For elements (values) with multiple occurences (duplicates), by default first occurence will be removed.
stock_prices = [98, 100, 103, 101, 102, 99, 101]
stock_prices.remove(101)
print(stock_prices)

#Remove by index
stock_prices = [98, 100, 103, 101, 102, 99, 101]
stock_prices.pop(2)
print(stock_prices)


# <i>
#     <b>
#         Time complexity for element deletion will be O(n).
#     </b>
#
# <u>Explanation:</u> Once an element is removed, we need to copy all the following elements to the previous memory location. Since at most, we might need to move n elements, thus worst case time complexity is O(n).
# </i>

# <h2>Static Array vs Dynamic Array</h2>

# <h3><i>Python lists are dynamic arrays</i></h3>

# <h4>Example using JAVA</h4>
#
# <h5>Static Array</h5>
#
# int stockPrices[] = new int[5]; <b><i>Initialises intereger array with max 5 elements.</i></b>
#
# stockPrices[0] = 98;</br>
# stockPrices[1] = 100;</br>
# stockPrices[2] = 103;</br>
# stockPrices[3] = 101;</br>
# stockPrices[4] = 102;
#
# stockPrices[6] = 101; <b><i><font color="red">Not allowed. Throws ArrayIndexOutOfBound exception.</i></b>
#
# <u>Explanation:</u> "<i><u>int stockPrices[] = new int[5];</u></i>" initilised an integer array with max_size of 5 (allowed index 0 to 4). Whenever we try to insert an additional element, we get ArrayIndexOutOfBound exception. <b>Size of static arrays is immutable.</b>

# <h4>Example using JAVA</h4>
#
# <h5>Dynamic Array</h5>
#
# ArrayList\<Integer\> stockPrices = new ArrayList\<Integer\>(); <b><i>Initialises dynamic intereger array. Dynamic arrays do not have any max element constaint.</i></b>
#
# stockPrices.add(98);</br>
# stockPrices.add(100);</br>
# stockPrices.add(103);</br>
# stockPrices.add(101);</br>
# stockPrices.add(102);</br>
# stockPrices.add(99);</br>
# stockPrices.add(101);
#
# <u>Explanation:</u> When we initilised a dynamic integer array object with "<i><u>ArrayList\<Integer\> stockPrices = new ArrayList\<Integer\>();</u></i>", a fixed amount of continuous memory is allocated in the RAM for the array. The neighbouring areas to these memory locations can be allocated to other programs or other variables of the same program, thus making them unavailable for expansion of our dynamic array when the initially allocated memory space is exhausted. When we have exhausted the initially allocated memory and try to insert newer elements, the array will be allocated a new memory area in different memory location with an additional memory twice the existing memory allocated, thus making the total size 3x - copy over the existing elements and then keep inserting newer elements. This is a continuous process for as many elements are to be inserted and the array size keeps growing. Thus, the <b>size of dynamic arrays is expandable (mutable).</b>
#
# <u>Note:</u> When dynamic arrays grow, there is an overhead of allocating new memory and copying over existing elememts to new memory area repeatedly. The memory thus grows in Geometric Progression.

# <b>
#     Python lists are heterogeneous in nature as it treats all list elements at objects (with references, i.e. their values) and can store integers, strings, dictionaries, even other lists as elements of the same list.
# </b>

# <h2>n-Dimensional Array</h2>

# <h3>2-Dimensional Array</h3>




stock_prices = [
    [2, 3, 5, 6],
    [97, 92, 95, 98],
    [41, 48, 59, 62, 88]
]

stock_prices[1][2] #Access element of row 2, column 3


# <h1>Exercise 1</h1>
#
# Let us say your expense for every month are listed below:</br>
# January - 2200</br>
# February - 2350</br>
# March - 2600</br>
# April - 2130</br>
# May - 2190</br>
#
# Create a list to store these monthly expenses and using that find out:
#
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this




#Initilise list
monthly_expense = [2200, 2350, 2600, 2130, 2190]
monthly_expense





#1
if monthly_expense[1] - monthly_expense[0] > 0:
    print(monthly_expense[1] - monthly_expense[0])
else:
    print("Expense is February was not more than January.")





#2
sum(monthly_expense[:3])





#3
if 200 in monthly_expense:
    print("Yes")
else:
    print("No")





#4
monthly_expense.append(1980)
monthly_expense





#5
monthly_expense[3] = monthly_expense[3] - 200
monthly_expense[3]


# <h1>Exercise 2</h1>
#
# You have a list of your favourite marvel super heros.</br>
# heros=['spider man','thor','hulk','iron man','captain america']
#
# Using this find out:
#
# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint - Use dir() functions to list down all functions available in list)




#Initialise list
heros = ['spider man','thor','hulk','iron man','captain america']
heros





#1
len(heros)





#2
heros.append("black panther")
heros





#3
heros.remove("black panther")

for i, hero in enumerate(heros):
    if hero == "hulk":
        index = i
        break

heros.insert(index + 1, "black panther")
heros





#4
heros[1:3] = ["doctor strange"]
heros





#5 - Hint
dir(heros)





#5
heros = ['spider man', 'doctor strange', 'iron man', 'captain america']

#Shallow sort
print(sorted(heros))
print(heros)

#In-place sort
heros.sort()
print(heros)


# <h2>Exercise 3</h2>
#
# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function




def create_list(n):
    arr = list()

    for i in range(1,n,2):
        arr.append(i)

    return arr

#Driver code
n = int(input("Enter n: "))
print(create_list(n))
