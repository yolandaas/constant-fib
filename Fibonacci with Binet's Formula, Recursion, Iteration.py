#!/usr/bin/env python
# coding: utf-8

# In[122]:


# (c) Yolanda Shen and Saketh Kollu


# In[2]:


# Run this cell to set up the notebook, but please don't change it.

# These lines import the Numpy and Datascience modules
import numpy as np
from math import sqrt
from datascience import *
import time

# These lines are for the plot graphs
import matplotlib
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import warnings
warnings.simplefilter('ignore', FutureWarning)


# In[3]:


# Binet's Formula for the nth term of the Fibonacci sequence
def fib_binet(n):
    PHI = 1.618033988749895
    root5 = sqrt(5)
    return ((PHI ** n) - ((-PHI) ** (-n))) / root5


# In[4]:


fib_binet(10)


# In[5]:


# Recursive formula for the nth term of the Fibonacci sequence
def fib_recursive(n):
    if n <= 2:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


# In[6]:


fib_recursive(10)


# In[7]:


# Iterative formula for the nth term of the Fibonacci sequence
def fib_iterative(n):
    previous = 1
    current = 1
    while n > 2:
        temp = current
        current += previous 
        previous = temp 
        n -= 1
    return current


# In[12]:


fib_iterative(10)


# In[13]:


# Calculates the execution time in milliseconds of a function 'f' with input 'n'
def execution_time(f, n):
    scale = 100000
    start = time.time()
    RV = f(n)
    end = time.time()
    delta = end - start
    return RV, delta * scale


# In[14]:


execution_time(fib_binet, 30)


# In[15]:


execution_time(fib_recursive, 30)


# In[16]:


execution_time(fib_iterative, 30)


# In[22]:


# This cell calculates the value and the execution time of all three functions  for all the values in the range 'n'

n = np.arange(35)

# Binet's
fib_binet_calculation = []
fib_binet_time = []
for i in n:
    fib_calc, exec_time = execution_time(fib_binet, i)
    fib_binet_calculation.append(fib_calc)
    fib_binet_time.append(exec_time)

# Recursive
fib_recursive_calculation = []
fib_recursive_time = []
for i in n:
    fib_calc, exec_time = execution_time(fib_recursive, i)
    fib_recursive_calculation.append(fib_calc)
    fib_recursive_time.append(exec_time)

# Iterative
fib_iterative_calculation = []
fib_iterative_time = []
for i in n:
    fib_calc, exec_time = execution_time(fib_iterative, i)
    fib_iterative_calculation.append(fib_calc)
    fib_iterative_time.append(exec_time)

# Building the Table
fibonacci = Table().with_columns('n', n, "Binet Calculation", fib_binet_calculation, "Recursive Calculation", fib_recursive_calculation, "Iterative Calculation", fib_iterative_calculation, "Binet Time", fib_binet_time, "Recursive Time", fib_recursive_time, "Iterative Time", fib_iterative_time)

# Calculating the Difference in Accuracy and Time
calculation_delta_binet_recursive = abs(fibonacci.column("Binet Calculation") - fibonacci.column("Recursive Calculation"))
calculation_delta_binet_iterative = abs(fibonacci.column("Binet Calculation") - fibonacci.column("Iterative Calculation"))
calculation_delta_iterative_recursive = abs(fibonacci.column("Iterative Calculation") - fibonacci.column("Recursive Calculation"))
time_delta_binet_recursive = abs(fibonacci.column("Binet Time") - fibonacci.column("Recursive Time"))
time_delta_binet_iterative = abs(fibonacci.column("Binet Time") - fibonacci.column("Iterative Time"))
time_delta_iterative_recursive = abs(fibonacci.column("Iterative Time") - fibonacci.column("Recursive Time"))
fibonacci = fibonacci.with_columns("calculationDelta Binet/Recursive", calculation_delta_binet_recursive, "calculationDelta Binet/Iterative", calculation_delta_binet_iterative, "calculationDelta Iterative/Recursive", calculation_delta_iterative_recursive, "timeDelta Binet/Recursive", time_delta_binet_recursive, "timeDelta Binet/Iterative", time_delta_binet_iterative, "timeDelta Iterative/Recursive", time_delta_iterative_recursive)

fibonacci.show()


# In[111]:


# Graph for the Execution Time of all three functions

fibonacci.select("n", "Binet Time", "Recursive Time", "Iterative Time").scatter("n")


# In[112]:


# The Recursive Formula has an exponential run time, but you can see that the Iterative and Binet times are very close. Let's take a closer look at the two.


# In[113]:


# Graph for the Execution Time of Binet's Formula and the Iterative function

fibonacci.select("n", "Binet Time", "Iterative Time").scatter("n")


# In[114]:


# Interestingly, Binet's Formula seems to take longer when n < 18. This makes sense, because Binet's Formula must run through the entire 
# formula for every calculation, while the Iterative function relies on the previous iteration. In this case, it takes less time to do < 18 iterations
# than it does to calculate the formula.

# However, you notice that while Binet Time stays relatively constant, Iterative Time increases at a constant rate.

# Thus:
# Binet's Formula = constant run time
# Iterative = linear run time


# In[115]:


# Graph of the Difference in Execution Time between all three formulas

fibonacci.select("n", "timeDelta Binet/Recursive", "timeDelta Binet/Iterative", "timeDelta Iterative/Recursive").scatter("n")


# In[116]:


# We can clearly tell that the time difference between Binet/Iterative functions is much smaller between either and the Recursive function.


# In[117]:


# Graph for the accuracy of the three functions

fibonacci.select("n", "Binet Calculation", "Recursive Calculation", "Iterative Calculation").scatter("n")


# In[118]:


# All three seem to be overlapping in this case. Let's see how accurate they are in relation to each other.


# In[119]:


# Graph of the Difference in Accuracy

fibonacci.select("n", "calculationDelta Binet/Recursive", "calculationDelta Binet/Iterative", "calculationDelta Iterative/Recursive").scatter("n")


# In[120]:


# Notice how fib_binet(0) evaluates to 0 because the numerator becomes (1 - 1), when it should be 1. 
# Therefore, Binet's Formula cannot be used for n = 0.

# Otherwise, the difference in accuracy is not that large. 
# Iterative/Recursive will always be zero difference in calculation, but since we are using a rounded version of Phi for Binet's Formula, there will always be a marginal error.
# At the same time, this error is not noticeable for numbers below 50 or so.


# In[121]:


##############################################################################################################
# Conclusion:

## Regarding Time:
# - Binet's Formula is significantly faster than the Recursive function and becomes the most efficient value by far as 'n' increases
# - Binet's Formula is NOT faster than the Iterative function before n = 18. This is because Binet's Formula must run through the entire 
#    formula for every calculation, while the Iterative function relies on the previous iteration

## Regarding Accuracy:
# - Binet's Formula is crazy accurate. The value for Phi is approximate, as only the first 15 decimal places were used, so the error will get larger as n increases.
# - However, a rounding function can be written to round the result to the nearest whole number. Even without it, the error is so marginal it doesn't particularly matter

## Regarding 'n':
# - The distinction between the three functions will only increase as n increases
# - However, I didn't want the notebook to run forever so I capped it at 35. 

## Regarding This Project:
# - THANK YOU if you've gotten to the end. This was a lot of fun to make and I learned a lot
# - One of those things being that I would rather do CS than study for chemistry.
# - Please feel free to play around with the numbers! But be conscious of how much time a large 'n' in fib_recursive will take to run

