import random
import numpy as np
import matplotlib.pyplot as plt

nums = list()
num_of_samples = 500

#  Create a population of 1000 items
for i in range(0,1000):
    x = random.randint(0,100)
    print(x)
    nums.append(x)



#  Create samples.
sample_averages = list()
for i in range(0,num_of_samples):
    sample = random.sample(nums, 10)
    a = np.average(sample)
    print a
    sample_averages.append(a)

mu = np.average(sample_averages)
sigma = np.std(sample_averages)

# the histogram of the data
n, bins, patches = plt.hist(sample_averages, 25, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *  np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')
plt.xlabel('Average of Sample')
plt.ylabel('Count')
plt.title('Central Limit Theroem')
plt.show()

