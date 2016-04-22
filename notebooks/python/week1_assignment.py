
# coding: utf-8

# # Exercises -- Chapter 3
# 
# 
# 1.  Create an array of 9 evenly spaced numbers going from 0 to
#     29 (inclusive) and give it the variable name `r`. Find the square of
#     each element of the array (as simply as possible). Find twice the
#     value of each element of the array in two different ways: 
#     
#     (*i*)  using addition 
#     
#     (*ii*) using multiplication.

# In[5]:

import numpy as np
r=np.arange(0,29,2)
r2times=2.*r
r2plus = r + r
print('double by multiplying: {}'.format(r2times))
print('double by adding: {}'.format(r2plus))


# 2\.  Create the following arrays:
# 
#     (a) an array of 100 elements all equal to $e$, the base of the
#         natural logarithm;
#         
#     (b) an array in 1-degree increments of all the angles in degrees
#         from 0 to 360 degrees;
#         
#     (c) an array in 1-degree increments of all the angles in radians
#         from 0 to 360 degrees;
#         
#     (d) an array from 12 to 17, not including 17, in 0.2 increments;
#     
#     (e) an array from 12 to 17, including 17, in 0.2 increments.

# In[28]:

a=np.arange(10)
print(a[-12])


# In[26]:

#(a)
the_ones=np.ones([100])
out=np.exp(1)*the_ones
print('(2a) {}'.format(out))
help(np.exp)
dir(np)l


# In[11]:

#(b)
degrees=np.arange(0,361)
print('(2b) {}'.format(degrees))


# In[13]:

#(c)
radians=degrees*(2.*np.pi/360.)
print('(2c) {}'.format(radians))


# In[14]:

#(d)
out=np.arange(12,17,0.2)
print('(d) {}'.format(out))


# In[15]:

#(e)
out=np.arange(12,17.1,0.2)
print('(d) {}'.format(out))


# 3\. The position of a ball at time $t$ dropped with zero initial
# velocity from a height $h_0$ is given by
# 
# $$y = h_0 - \frac{1}{2}gt^2$$
#     
#     

# where $g=9.8~\mathrm{m/s}^2$. Suppose $h_0=10~\mathrm{m}$. Find the
# sequence of times when the ball passes each half meter assuming the
# ball is dropped at $t=0$. Hint: Create a NumPy array for $y$ that
# goes from 10 to 0 in increments of -0.5 using the `arange` function.
# Solving the above equation for $t$, show that
# 
# $$t = \sqrt{\frac{2(h_0-y)}{g}} \;.$$
# 
# Using this equation and the array you created, find the sequence of
# times when the ball passes each half meter.

# In[29]:

#(3)

def find_time(z,h_0):
    """
      find the time at which a ball dropped from h_0 (meters)
      passes height z (meters)
      input: z (height in meters)
            h_0 (starting height in meters)
       ourput: time (seconds)
    """
    g=9.8 #acceleration of gravity m/s/s
    the_times=np.sqrt(2*(h_0 - z)/g)
    return the_times

y=np.arange(10,0,-0.5)
h_0=10  #meters
the_times=find_time(y,h_0)
print('heights (m): {}'.format(y))
print('times (s): {}'.format(the_times))
   


# 4\.  Recalling that the average velocity over an interval $\Delta t$ is
#     defined as $\bar{v} = \Delta y/\Delta t$, find the average velocity
#     for each time interval in the previous problem using NumPy arrays.
#     Keep in mind that the number of time intervals is one less than the
#     number of times. Hint: What are the arrays `y[1:20]` and `y[0:19]`?
#     What does the array `y[1:20]-y[0:19]` represent? (Try printing out
#     the two arrays from the IPython shell.) Using this last array and a
#     similar one involving time, find the array of average velocities.
#     Bonus: Can you think of a more elegant way of representing
#     `y[1:20]-y[0:19]` that does not make explicit reference to the
#     number of elements in the `y` array---one that would work for any
#     length array?

# In[20]:

delta_y = y[1:] - y[:-1]
delta_t =the_times[1:] - the_times[:-1]
velocity = delta_y/delta_t
print('velocity (m/s): {}'.format(velocity))


# In[ ]:



