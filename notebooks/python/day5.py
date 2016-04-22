
# coding: utf-8

# ### 6.1 factorial using while and for 

# In[2]:

import numpy
origfac=10
fac=origfac
accum=1
while fac > 1:
    accum=accum*fac
    fac-=1
print('factorial of {}'.format(origfac))
print('my factorial= ',accum)
print('numpy factorial= ',np.math.factorial(origfac))

accum=1
vals = numpy.arange(origfac,0,-1)
for item in vals:
    accum=accum*item
print('for loop factorial: ',accum)


# ### 6.2a smallest prime factor

# In[3]:

n = int(input("Input an integer > 1: "))
i = 2

while (n % i) != 0:
    i += 1

print("The smallest factor of n is:", i )


# ### 6.2b is integer prime

# In[4]:

n = int(input("Input an integer > 1: "))
def find_prime(n):
    i = 2
    while (n % i) != 0:
        i += 1
    if i == n:
        out='prime'
    else:
        out=i
    return out

print('Is {} prime? Smallest factor is {}'.format(n,find_prime(n)))
        



# ### 6.3 list comprehensions

# In[13]:

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
last_col = [x[i][-1] for i in range(len(x))]
print(last_col)
square2 = [2.*(x[i][1])**2. for i in range(len(x))]
print(square2)


# In[ ]:



