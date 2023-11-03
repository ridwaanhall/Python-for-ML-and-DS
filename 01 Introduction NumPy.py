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
