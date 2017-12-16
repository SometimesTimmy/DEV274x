
# coding: utf-8

# 
# #  Module 4 Required Coding Activity  
# Introduction to Python (Unit 2) Fundamentals  
# 
# **This Activity is intended to be completed in the jupyter notebook, Required_Code_MOD4_IntroPy.ipynb, and then pasted into the assessment page that follows.**   
#  
# All course .ipynb Jupyter Notebooks are available from the project files download topic in Module 1, Section 1.
# 
# This is an activity based on code similar to the Jupyter Notebook **`Practice_MOD04_IntroPy.ipynb`** which you may have completed.   
# 
# | **Assignment Requirements** |  
# |:-------------------------------|  
# | **NOTE:** This program requires **`print`** output and code syntax used in module 4 such as variable assignment,  **`while`**, **`open`** keywords,  **`.split()`**, **`.readline()`**, **`.seek()`**, **`.write()`**, **`.close()`** methods  |  
# 
# ## The Weather
# #### Create a program that:  
# - imports and opens a file  
# - appends additional data to a file  
# - reads from the file to displays each city name and month average high temperature in Celsius  
# 
# **Output:** The output should resemble the following
# ```
# City of Beijing month ave: highest high is 30.9 Celsius
# City of Cairo month ave: highest high is 34.7 Celsius
# City of London month ave: highest high is 23.5 Celsius
# City of Nairobi month ave: highest high is 26.3 Celsius
# City of New York City month ave: highest high is 28.9 Celsius
# City of Sydney month ave: highest high is 26.5 Celsius
# City of Tokyo month ave: highest high is 30.8 Celsius
# City of Rio De Janeiro month ave: highest high is 30.0 Celsius
# ```  
# all of the above text output is generated from the file  
# the only strings are *hard coded*:  
# - "is"  
# - "of"  
# - "Celsius"  
# 
# 
# 
# #### import the file into the Jupyter Notebook environment   
# - use `!curl` to download https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv as `mean_temp.txt`  
#   
# 
# ```python
# # [ ] The Weather: import world_mean_team.csv as mean_temp.txt into the Jupyter notebook
# 
# 
# ```  
# 
# #### Add the weather for Rio  
# 1. Open the file in append plus mode (**`'a+'`**)  
# 2. Write a new line for Rio de Janeiro `"Rio de Janeiro,Brazil,30.0,18.0\n"`  
# 
# 
# #### Grab the column headings  
# 1. use .seek() to move the pointer to the beginning of the file  
# 2. read the first line of text into a variable called: `headings`     
# 3. convert `headings` to a list using **`.split(',')`** which splits on each comma  
# 
# 
# ```python
# # [ ] The Weather: open file, read/print first line, convert line to list (splitting on comma)
# 
# 
# ```
# 
# #### Read the remaining lines from the file using a while loop
#   1. assign remaining lines to a **`city_temp`** variable  
#   2. convert the city_temp to a list using **`.split(',')`** for each **`.readline()`** in the loop  
#   3. print each city & the highest monthly average temperature   
#   4. close mean_temps
# 
# >Tips & Hints:   
# - print **`headings`** to determine indexes to use for the final output (what is in headings[0], [1], [2]..?)  
# - the city_temp data follows the order of the headings (city_temp[0] is described by headings[0]) 
# - The output should look like: **`"month ave: highest high" for Beijing is 30.9 Celsius`**  
# - convert `city_temp` to lists with `.split(',')`  
# 
# 
# ```python
# # [ ] The Weather: use while loop to print city and highest monthly average temp in celsius
# 
# 
# ```
# 
# ### Combine All Code into one cell, Copy and Submit on edX
# 

# In[8]:


# [] create The Weather
# [] copy and paste in edX assignment page
# note that mean_temp.txt contains
# city,country,month ave: highest high,month ave: lowest low
# Beijing,China,30.9,-8.4
# Cairo,Egypt,34.7,1.2
# London,UK,23.5,2.1
# Nairobi,Kenya,26.3,10.5
# New York City,USA,28.9,-2.8
# Sydney,Australia,26.5,8.7
# Tokyo,Japan,30.8,0.9

get_ipython().system(u' curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv -o mean_temp.txt')

mean_temps = open('mean_temp.txt','a+')
mean_temps.write("Rio de Janeiro,Brazil,30.0,18.0\n")
mean_temps.seek(0)
headings = mean_temps.readline()
headings = headings.split(',')
# print(headings[0]) will print only the word city
# heading = ['city', 'country', 'month ave: highest high', 'month ave: lowest low\n']

city_temp = mean_temps.readline()
while city_temp:
    city_temp = city_temp.split(',')
    # The output should look like: City of Beijing month ave: highest high is 30.9 Celsius
    # the only strings are hard coded: "is", "of", and "Celsius". Rest of the text output are generated from the file.
    print(headings[0].title(),"of",city_temp[0],headings[2],"is",city_temp[2],"Celsius")
    city_temp = mean_temps.readline()
    
mean_temps.close()


# ### Need assignment tips and clarification? 
# See the video on the "End of Module coding assignment > Module 4 Required Code Description" course page on [edX](https://courses.edx.org/courses/course-v1:Microsoft+DEV274x+4T2017/course)    
# 
# # Important:  [How to submit code by pasting](https://courses.edx.org/courses/course-v1:Microsoft+DEV274x+2T2017/wiki/Microsoft.DEV274x.2T2017/paste-code-end-module-coding-assignments/)
# 

# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
