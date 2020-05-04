import numpy as np

# a = np.random.random((256, 256, 3))


# # 1
# b = np.ones((256, 1))

# # 2 
# b = np.ones((256, 256)) 

# # 3
# b = np.ones((256, 3))   

# # 4
# b = np.ones((1, 3)) 

# print(a+b)


# ## Simplified for understanding

# a = np.random.random((2, 2, 3))

# # 1
# b = np.ones((2, 1)) # sums 1 to each element

# # 2 
# # b = np.ones((2, 2)) # does not work!

# # 3
# # b = np.ones((2, 3))  # sums 1 to each element

# # 4
# # b = np.ones((1, 3)) # sums 1 to each element

# print(a)
# print('-----')
# print(a+b)