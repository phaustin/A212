#
#  create a default profile if it doesn't exist with
#  ipython profile create
#
# find your profile folder  by typing
# ipython locate
# at a git-bash prompt
#
# if the folder is /Users/phil/.ipython then put this file in
# /Users/phil/.ipython/profile_default/startup/
#
# put your cloned repository in /Users/phil/repos/A405
# and it will be automatically added to sys.path
#
import site, os
#
# find ip.home_dir
#
ip = get_ipython()
#
# os.path.sep is '/' on unix and '\' on windows
#
a405_repo = r'{0:}{1:}repos{1:}A405'.format(ip.home_dir,os.path.sep)
site.addsitedir(a405_repo)
print('added {} to the path'.format(a405_repo))
from IPython.core.display import display
from IPython.display import Image
from matplotlib import pyplot as plt
import numpy as np
import scipy as sp
print("ran {}".format(__file__))
