# numbers = [10, 2, 5, 3, 7, 2]
# len(): Returns the number of elements in the list.

# length = len(numbers)
# print(length) 

# numbers = [10, 2, 5, 3, 7, 2]   

# append(): Adds an element to the end of the list.

# numbers.append(20)
# numbers.append(0)
# print(numbers)


# numbers = [10, 2, 5, 3, 7, 2]   
# insert(): Inserts an element at a specified position.

# numbers.insert(1,15)    
# numbers.insert(3, 25) 
# print(numbers)

# remove(): Removes the first occurrence of a specific element.

# numbers = [10, 2, 5, 3, 7, 2, 7, 7]  
# print(numbers)

# numbers.remove(7) 
# print(numbers)








# pop(): Removes and returns the last element of the list or an element at a specified index.

# numbers = [10, 2, 5, 3, 7, 2, 50] 
# print(numbers.pop())   

# fruits = ["apple", "banana", "grape", "pineapple", "orange", "grape"]

# Remove the element at index 2 (grape)
# popped_fruit = fruits.pop(2)
# print(popped_fruit)

# print(f"'{popped_fruit}' which was at index 2, has been removed from fruits")
  

# index(): Returns the index of the first occurrence of a specified element.


# example
# fruits = ["apple", "banana", "grape", "pineapple", "orange", "grape"]

# # Find the index of the first occurrence of "grape"
# grape_index = fruits.index("grape")
# print(f"The index of  the first occurence of 'grape' in the list is: {grape_index}")  



# count(): Returns the number of occurrences of a specified element.

# Example
# Count the number of occurrences of 2 in the list

# numbers = [10, 2, 5, 2,3, 7, 2, 50, 2]
 
# count_2 = numbers.count(2)
# print(f"The number of occurrences of '2' in the list is: {count_2}")  



# fruits = ["apple", "banana", "grape", "pineapple", "orange", "grape", "grape"]
# count_grape = fruits.count("grape")

# print(f"grape occurs {count_grape} times in the fruits list")



# sort(): Sorts the list in ascending order.
# numbers = [10, 2, 5, 3, 7, 2, 50] 
# numbers.sort()          
# print(numbers)






# reverse(): Reverses the order of elements in the list.
numbers = [10, 2, 5, 3, 7, 2, 50] 
numbers.reverse()  
print(numbers)  

fruits = ["apple", "banana", "grape", "pineapple", "orange", "grape"]    
fruits.reverse()
print(fruits)