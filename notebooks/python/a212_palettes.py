
# coding: utf-8

# ### Assignment for March 23

# 1. Read these for six blog posts for background:
# 
# http://earthobservatory.nasa.gov/blogs/elegantfigures/2013/08/05/subtleties-of-color-part-1-of-6/
# 
# 2. Make sure seaborn is installed:
# 
# ```
# conda install seaborn
# conda install pillow
# ```
# 
# and use it to do the color palette tutorial here:
# 
# http://stanford.edu/~mwaskom/software/seaborn/tutorial/color_palettes.html
# 
# 3.  Transfer this image tutorial to a notebook:
# 
# http://matplotlib.org/users/image_tutorial.html#importing-image-data-into-numpy-arrays
# 
# and add three new cells, each showing the stinkbug image with a different colormap
# you've generated with seaborn light_palette, dark_palette and cube_helix, respectively.
# Include a colorbar for each image.
# 
# The cell below shows how to import the stinkbug.

# In[1]:

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from pathlib import Path
import a212data
get_ipython().magic('matplotlib inline')
datadir = a212data.__path__[0]
stinkpath = Path(datadir).joinpath('stinkbug.png')
img=mpimg.imread(str(stinkpath))
imgplot = plt.imshow(img)
lum_img = img[:,:,0]
imgplot = plt.imshow(lum_img)
imgplot.set_cmap('hot')
plt.show()

