
# coding: utf-8

# In[1]:

import seaborn as sns
from matplotlib import pyplot as plt


# In[2]:

from IPython.display import Image
picwidth=900


# ### Go over the plots produced by [plot_palettes.py](https://github.com/phaustin/e582/blob/master/cloudmask/plot_palettes.py)

# 1. Read the data in using [get_channels](https://github.com/phaustin/e582/blob/plot_palette/cloudmask/plot_palettes.py#L88-L124)
# 2. Change all the model6 category 6 pixels to category 4 so I can use a [5 color palette](https://github.com/phaustin/e582/blob/plot_palette/cloudmask/plot_palettes.py#L171-L176):
# 3. Use color names https://xkcd.com/color/rgb/ to [mark the 5 cloud categories](https://github.com/phaustin/e582/blob/plot_palette/cloudmask/plot_palettes.py#L182-L188)
# 4. Now look at an ungridded image to check the categories -- note that we need to rotate this particular
# granule by [180 degrees](https://github.com/phaustin/e582/blob/plot_palette/cloudmask/plot_palettes.py#L193-L204). Also note how I position the labels in the middle of the colorbar

# In[ ]:

Image('../cloudmask/plots/ungridded_phase_map.png',width=picwidth)


# ###Here is a [histogram of the raw phase values](https://github.com/phaustin/e582/blob/plot_palette/cloudmask/plot_palettes.py#L205-L211)

# In[ ]:

Image('../cloudmask/plots/ungridded_phase_hist.png',width=picwidth)


# ###Here is the gridded phase map -- [lcc projection](https://github.com/phaustin/e582/blob/plot_palette/cloudmask/plot_palettes.py#L215-L237)

# In[ ]:

Image('../cloudmask/plots/gridded_phase_map.png',width=picwidth)


# ###Here is the histogram of the [gridded phase values](https://github.com/phaustin/e582/blob/plot_palette/cloudmask/plot_palettes.py#L241-L244).  Note that I use the compressed method for masked array to get the good pixels

# In[ ]:

Image('../cloudmask/plots/gridded_phase_hist.png',width=picwidth)


# ###Now map the 8-11 [brightness temperature difference](https://github.com/phaustin/e582/blob/master/cloudmask/plot_palettes.py#L245-L265) using a linear segmented palette with 256 colors

# In[ ]:

Image('../cloudmask/plots/gridded_TBdiff_map.png',width=picwidth)


# ###Next, look at the MYD35 cloud mask using a [discrete four color palette](https://github.com/phaustin/e582/blob/plot_palette/cloudmask/plot_palettes.py#L269-L289) constructed by choosing 4 colors from the coolwarm_r palette.  You can edit this to instead [use four shades of blue](https://github.com/phaustin/e582/blob/plot_palette/cloudmask/plot_palettes.py#L272)

# In[ ]:

Image('../cloudmask/plots/mapped_cloudmask.png',width=picwidth)


# ###Last, I've added a new cython function: [get_bit](https://github.com/phaustin/e582/blob/plot_palette/cloudmask/bitmap.pyx#L87-L108) which calls [readbit](https://github.com/phaustin/e582/blob/plot_palette/cloudmask/bitmask.cpp#L115-L120) to read an arbitrary bit from a byte.  I use it to read [the high cloud 6.7 micron flag](https://github.com/phaustin/e582/blob/plot_palette/cloudmask/plot_palettes.py#L296-L300) from the [Model 35 cloud mask](http://modis-atmos.gsfc.nasa.gov/_specs/MOD35_L2.CDL.fs)

# In[ ]:

Image('../cloudmask/plots/map_gridded_bit.png',width=picwidth)


# ###[and here is the histogram](https://github.com/phaustin/e582/blob/plot_palette/cloudmask/plot_palettes.py#L309-L312)

# In[ ]:

Image('../cloudmask/plots/hist_gridded_bit.png',width=picwidth)


# In[ ]:



