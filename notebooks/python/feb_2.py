
# coding: utf-8

# In[4]:

import numpy as np
import calendar


# In[ ]:

#test:   balance 118.39, day 17, monthlength 30, daily 8.46
balance=input('How much money (in dollars) in your lunch account? ')
day=input('What day of the month is today? ')
monthlength=input('How many days in this month? ')
balance,day,monthlength = [float(item) for item in (balance,day,monthlength)]
remaining = monthlength -day + 1
daily = balance/remaining
text='You can spend ${:4.2f} each day for the rest of the month.'.format(daily)
print(text)


# In[ ]:

text = ('aaaaa', 
        'bbbbbbb')
print(text)
a=5
b=2
b,a = a,b
print(b)
a, = b,
a=('abb',)
print(a)


# In[2]:


#Optional: make a dictionary holding the length of the month for 2016

monthdict = {}
for month in np.arange(1,13):
    startday,length =calendar.monthrange(2016,month)
    monthdict[month] = length
print(monthdict)

#test:   balance 118.39, day 17, month=2 , daily 9.87

balance=input('How much money (in dollars) in your lunch account? ')
day=input('What day of the month is today? ')
monthnum=input('What is the month number (Jan=1,Dec=12) ')
try:
    balance,day,monthnum = [float(item) for item in (balance,day,monthnum)]
except:
    print("didn't understand input, using defaults")
    balance=118.39
    day=17
    monthnum=2
monthlength=monthdict[monthnum]
remaining = monthlength -day + 1
daily = balance/remaining
text='You can spend ${:4.2f} each day for the rest of the month.'.format(daily)
print(text)


# In[3]:

the_data =    """
        Date: 2013-09-16
        Data taken by Liam and Selena
        frequency (Hz) amplitude (mm)  amp error (mm)
          0.7500        13.52         0.32
          1.7885        12.11         0.92
          2.8269        14.27         0.73
          3.8654        16.60         2.06
          4.9038        22.91         1.75
          5.9423        35.28         0.91
          6.9808        60.99         0.99
          8.0192        33.38         0.36
          9.0577        17.78         2.32
         10.0962        10.99         0.21
         11.1346         7.47         0.48
         12.1731         6.72         0.51
         13.2115         4.40         0.58
         14.2500         4.07         0.63
    """
filename = 'freq_data.txt'
the_data = the_data.strip()
with open(filename,'w') as f:
    f.write(the_data)


# In[5]:

f,a,da =np.loadtxt(filename,skiprows=3,unpack=True)
print('f= \n{}'.format(f))
print('a= \n{}'.format(a))
print('da= \n{}'.format(da))


# In[7]:

out=np.loadtxt(filename,skiprows=3)
print(out)
print(out.shape, out.dtype)


# In[ ]:



