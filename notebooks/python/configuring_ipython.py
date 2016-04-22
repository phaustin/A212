
# coding: utf-8

# # Configuring IPython
# 
# Here is my howto on setting up a standard environment.  I'm assuming that
# you have cloned A405 into a folder in your home directory called
# ~/repos/A405.  The two startup files are in
# ~/repos/A405/utils/ipython_startup: 
# 
# * [ipython_config.py](https://github.com/phaustin/A405/blob/master/utils/ipython_startup/ipython_config.py)
# 
#   which sets c.InlineBackend.close_figures=False  so figures stay open between cells
#   
#   
# * [00startup.py](https://github.com/phaustin/A405/blob/master/utils/ipython_startup/00startup.py)
# 
#   which adds ```~/repos/A405``` to sys.path and imports standard modules like numpy, scipy and pyplot

# ### Making the startup files available to ipython notebook
# 
# 1.  Launch a terminal (osx) or git-bash (windows) and cd to
#     home:
#     
#     ```
#       cd ~
#     ```
# 
# 1.  move any previous .ipython folder out of the way
# 
#     ```
#       mv .ipython .ipython_safe
#     ```
# 
# 1.  Create a fresh profile
# 
#     ```
#       ipython profile create  
#     ```
# 
# 1.  Confirm that the profile is in the right place with
# 
#     ```
#       ipython locate  #(this should print something like c:\Users\phil\.ipython on windows)
#     ```
#     
# 1.  Copy the class 00startup.py file into the profile/startup folder
# 
#     ```
#       cd ~/.ipython/profile_default/startup
#       cp ~/repos/A405/utils/ipython_startup/00startup.py .    # the "." means copy to current directory
#     ```
# 
# 1.  Copy the class ipython_config.py file into the profile folder
#   
#     ```
#       cd ~/.ipython/profile_default
#       cp ~/repos/A405/utils/ipython_startup/ipython_config.py .
#     ```

# ### Testing the installation

# In[16]:

#make sure these are imported by 00startup.py

print(display)
print(np)
print(sp)
print(plt)


# In[10]:

#get the config and print it

ip = get_ipython()


# typing ```ip.config```  should print something like this showing close_figures is false:
# 
# ```
# {'IPKernelApp': {'connection_file': '/Users/phil/Library/Jupyter/runtime/kernel-35ff1ca9-1a6b-4703-8ea7-9cd7597ac8e2.json'},
#  'InlineBackend': {'close_figures': False}}
# ```

# In[11]:

ip.config


# ### Now see if plot stays open between cells

# In[12]:

get_ipython().magic('matplotlib inline')
fig,ax=plt.subplots(1,1)
ax.plot([0,1],[0,1])


# In[13]:

ax.set(title='title here')
display(fig)


# In[14]:

ax.set(title='wait I like this better')
display(fig)


# In[15]:

#
# and to get rid of it
#
del fig
display(fig)


# In[ ]:



