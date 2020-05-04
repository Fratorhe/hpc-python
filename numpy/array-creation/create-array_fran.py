import numpy as np 

# Start from a Python list containing both integers and floating point values, 
# and construct then a NumPy array from the list.
a = np.array([1,5,8.,8.5847,465,.1,1])

print(a)

# Generate a 1D NumPy array containing all numbers from -2.0 to 2.0 with a spacing of 0.2. 
# Use optional start and step arguments of the np.arange() function.

b = np.arange(start=-2, stop=2, step=0.2)
print(b)

# Generate another 1D NumPy array containing 11 equally spaced values between 0.5 and 1.5.
c = np.linspace(start=0.5, stop=1.5, num=11)

# Take some Python string and construct from it 
# NumPy array consisting of single characters (a character array).

word = 'consisting'
d = np.array(word, dtype = 'c')
print(d)
