#!/usr/bin/env python
# coding: utf-8

# ## Script to calculate Basic Statistics

# ### Equation for the mean:   $\mu_x = \sum_{i=1}^{N}\frac{x_i}{N}$
# 
# ### Equation for the standard deviation:  $\sigma_x = \sqrt{\sum_{i=1}^{N}\left(x_i - \mu \right)^2}\frac{1}{N-1}$
# 
# 
# **Instructions:**
# 
# **(1) Before you write code, write an algorithm that describes the sequence of steps you will take to compute the mean and standard deviation for your samples.  The algorithm can be written in pseudocode or as an itemized list.***
# 
# **(2) Use 'for' loops to help yourself compute the average and standard deviation.**
# 
# **(3) Use for loops and conditional operators to count the number of samples within $1\sigma$ of the mean.**
# 
# **Note:** It is not acceptable to use the pre-programmed routines for mean and st. dev., e.g. numpy.mean()

# ### Edit this box to write an algorithm for computing the mean and std. deviation.
# 
# ~~~
# 
# 
# 
# 
# 
# 
# ~~~

# ### Write your code using instructions in the cells below.

# # Kaitlin Neville
# ## Creation Date: 21 September 2021
# ### Basic Statistics 
# 
# 

# In[2]:


# Import the matplotlib module here.  No other modules should be used.

# Import plotting library
import matplotlib.pyplot as plt


# In[24]:


# Create a list variable that contains at least 25 elements.  You can create this list any number of ways.  
# This will be your sample.

family_ages = [21, 22, 3, 44, 45, 18, 91, 102, 65, 54, 32, 31, 6, 12, 45, 78, 43, 27, 99, 32, 87, 90, 53, 28, 22, 67, 60]


# In[25]:


# Pretend you do not know how long x is; compute it's length, N, without using functions or modules.

Age_count = 0 

for age in family_ages:
    Age_count = Age_count + 1
    
print(Age_count)


# In[26]:


# Compute the mean of the elements in list x.

sum=0

# for each number in family_ages (i) add each to the sum
for i in family_ages:
    sum +=i

# once sum is found, mean can be found 
# mean is equal to sum divided by the number of items in the list (Age_count) 
mean = sum/Age_count

print(mean)


# In[27]:


# Compute the std deviation, using the mean and the elements in list x.

from math import sqrt 

family_ages = [21, 22, 3, 44, 45, 18, 91, 102, 65, 54, 32, 31, 6, 12, 45, 78, 43, 27, 99, 32, 87, 90, 53, 28, 22, 67, 60]

# adds up a each component on the list minus mean to the second power 
sum = 0 
for i in family_ages: 
    sum += (i-mean)**2

# Standard Deviation formula: 

standard_dev = sqrt(sum/Age_count -1)
print(standard_dev)



# In[31]:


# Use the 'print' command to report the values of average (mu) and std. dev. (sigma).

#already printed throughout the code

print('Age Count:',Age_count)
print('Mean:',mean)
print('Standard Deviation:',standard_dev)


# In[37]:


# Count the number of values that are within +/- 1 std. deviation of the mean.  
# A normal distribution will have approx. 68% of the values within this range.  
# Based on this criteria is the list normally distributed?

upper_range = mean + standard_dev
print('Upper Range:',upper_range)
lower_range = mean - standard_dev
print('Lower Range:',lower_range)

# There are 17 values that fall between +/- 1 std. of the mean 

values = 17
Distribution = values/Age_count
print('Distribution:',Distribution)


# In[38]:


# Use print() and if statements to report a message about whether the data is normally distributed.

if 0.675 < Distribution < 0.685:
    print('Normally Distributed')
    
else: 
    print('Not Normally Distributed')


# In[41]:


### Use Matplotlb.pyplot to make a histogram of x.

import matplotlib.pyplot as plt
 
family_ages = [21, 22, 3, 44, 45, 18, 91, 102, 65, 54, 32, 31, 6, 12, 45, 78, 43, 27, 99, 32, 87, 90, 53, 28, 22, 67, 60]


plt.hist(family_ages, bins=10)

plt.xlabel("Ages")
plt.ylabel("Count")
plt.show()


# ### OCG 593 students, look up an equation for Skewness and write code to compute the skewness. 
# #### Compute the skewness and report whether the sample is normally distributed.

# # Definition for Skewness:
# 
#  $$\mu_3 = {\sum_{i=1}^{N}\left(x_i - \mu \right)^3}\frac{1}{{N-1}*\sigma^3}$$
#  
# $x_i$ : the ith number of the list
# 
# $\mu$ : is the mean
# 
# $\sigma$ : is the standard of deviation 
# 

# In[43]:


from math import sqrt 

family_ages = [21, 22, 3, 44, 45, 18, 91, 102, 65, 54, 32, 31, 6, 12, 45, 78, 43, 27, 99, 32, 87, 90, 53, 28, 22, 67, 60]

sum = 0 
for i in family_ages: 
    sum += (i-mean)**3

# Standard Deviation formula: 

skewness = (sum/((Age_count -1)*standard_dev**3))
print('Skewness:',skewness)


# In[44]:


if 0.675 < Distribution < 0.685:
    print('Sample is Normally Distributed')
    
else: 
    print('Sample is Not Normally Distributed')


# In[ ]:




