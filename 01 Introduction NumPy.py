# %%
import numpy as np

# %%
# create 2 new lists height and weight
person_weight = [60, 72, 57, 90, 95, 72]
person_height = [1.6, 1.8, 1.5, 1.7, 1.9, 1.8]

# create 2 numpy arrays from height and weight
person_height_np = np.array(person_height)
person_weight_np = np.array(person_weight)

# %%
# print 'person_height_np'
person_height_np

# %%
# print 'person_weight_np'
person_weight_np

# %%
# print type of 'person_height_np'
print(type(person_height_np))


# %%
# indexing an array
# given array
my_array = np.array([1, 2, 3, 4, 5])
print(my_array)
# %%
# get the 1st element
# indexing starts from 0
first_element = my_array[0]
print(first_element)

# get the 3rd element
third_element = my_array[2]
print(third_element)
# %%
# indexing in 2 dimensions
my_array = np.array(
    [[101,231,321],
    [102,232,322],
    [103,233,323]])
my_array
# %%
# get the element in 3rd row and 2nd column
element = my_array[2][1]
print(element)
# %%
print(my_array[2,1])
# %%
# pick the second row from the array
second_row = my_array[1]
print(second_row)
# %%
# pick the second column from the array
second_column = my_array[:, 1]
print(second_column)
# %%
# slicing array
my_array = [1, 2, 3, 4, 5]
# %%
# pick the second, third and fourth element
elements = my_array[1:4]
print(elements)
# %%
# first three elements
first_three_elements = my_array[:3]
print(first_three_elements)
# %%
# last two elements
last_two_elements = my_array[-2:]
print(last_two_elements)
# %%
# slicing a 1D array
my_array = [1, 2, 3, 4, 5]
# %%
# pick the second, third and fourth element
elements = my_array[1:4]
print(elements)
# %%
# all elements
all_elements = my_array[:]
print(all_elements)
# %%
# slicing a2D array
my_array = np.array(
    [[101,231,321,412,511],
     [102,232,322,413,512],
     [103,233,323,414,513],
     [105,235,325,416,515]])
my_array
# %%
# select all rows except the 1st
selected_rows = my_array[1:]
print(selected_rows)
# select 3rd and 4th column
selected_columns = my_array[:, 2:4]
print(selected_columns)
# select all rows except 1st and select 3rd and 4th column
selected_elements = my_array[1:, 2:4]
print(selected_elements)
# %%
# operation on array
my_array1 = np.array([1, 2, 3, 4, 5])
my_array2 = np.arange(5)
my_array2
# %%
# add two arrays
addition = my_array1 + my_array2
print(addition)
# %%
# subtract two arrays
subtraction = my_array1 - my_array2
print(subtraction)
# %%
# multiply two arrays
multiplication = my_array1 * my_array2
print(multiplication)
# %%
# divide two arrays
division = my_array1 / my_array2
print(division)

# %%
