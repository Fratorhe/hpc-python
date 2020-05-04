import numpy as np
import matplotlib.pyplot as plt

nums = np.random.uniform(0,10,100)

print(np.mean(nums))
print(np.std(nums))

plt.hist(nums, density=True)
plt.show()