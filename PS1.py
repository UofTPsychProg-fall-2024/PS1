#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem Set 1
@author: katherineduncan
"""

#%% Part 1: pass the error forward ____________________________________________
# this should be completed one at a time to get practice using GitHub


# there's an error in the definition of coder1 below
# first group member (coder 1), your job is to first correct it 
# and make a new variable with an error for the next group member to fix
# after competing both steps, commit and push your changes to GitHub
coder1 = 'hello world! python line " + 1 
print(coder1)

# second group member's error to fix
coder2 =

# now the second group member should define a variable with an error
# and then commit and push changes to GitHub
coder3 =

# etc. until all group members have fixed and made 1 error



#%%  Part 2  find and remove the invalid response______________________________

# imagine these are a list of reaction times that you recorded 
rt = [400, 450, 500, 440, -1, 400, 570]

# use slicing to create two new variables, one that contains rts from even
# trials and the other odd trials

event_rt =
odd_rt =

# the -1 indicates missing data. Your job is to remove it
# first use the "in" operator to check if there is missing data in rt
# add a comment that notes what data type is returned when you use the "in" operator


# lists have a nifty method called "index" which returns the index 
# of a value within the list. 
# use this method to find the index that contains missing data in rt
# hint, this method is mentioned on a lecture slide but you may need to 
# use google/stack exchange to work out how to use it

missing_rt = ...

# and then use missing_rt to remove the trial from rt
clean_rt = rt
del(...)

# how would this approach work if you had multiple missing values in RT? 
# use indexing to replace the value 450 with -1
rt = [400, 450, 500, 440, -1, 400, 570]
rt...

# now rt should hve two missing values
# try using the index method and the del function to remove them


# what happened? What would you have to do to ensure that there are no missing values left? 

