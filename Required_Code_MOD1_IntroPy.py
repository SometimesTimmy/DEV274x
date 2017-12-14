
# coding: utf-8

# 
# #  Module 1 Required Coding Activity  
# 
# Introduction to Python (Unit 2) Fundamentals  
# 
# 
# 
# **This Activity is intended to be completed in the jupyter notebook, Required_Code_MOD1_IntroPy.ipynb, and then pasted into the assessment page on edX.**   
# 
# This is an activity from the Jupyter Notebook **`Practice_MOD01_IntroPy.ipynb`** which you may have already completed.
# 
# | Important Assignment Requirements |  
# |:-------------------------------|  
# |  **NOTE:** This program **requires** **`print`** output and using code syntax used in module 1 such as keywords **`for`**/**`in`** (iteration), **`input`**, **`if`**, **`else`**, **`.isalpha()`** method, **`.lower()`** or **`.upper()`** method |  
# 
# 
# ## Program: Words after "G"/"g"
# Create a program inputs a phrase (like a famous quotation) and prints all of the words that start with h-z
# 
# Sample input:  
# `enter a 1 sentence quote, non-alpha separate words:` **`Wheresoever you go, go with all your heart`**  
# 
# Sample output:
# ```
# WHERESOEVER
# YOU
# WITH
# YOUR
# HEART
# ```  
# ![words_after_g flowchart](https://ofl1zq-ch3302.files.1drv.com/y4msZuRt9FLMg2HrIVri9ozb5zM0Z9cwrgFg0OanRG3wThbKGRTjxf6vEmvDgiQzAthvLq4KDpiOfd5S74i-vsCDYha-Ea5B1d4MJD5tx6obEpFj3Slks3bCFbjltvV_BYQ8mlbmyoAhujPM6nHRbOxNeO2Lb6dvmW0EbS-D3QXR7lRb-whNWwquwwzO4znPMmQ4Jkf4ujqTlSpjGuaKzwTSQ?width=608&height=371&cropmode=none) 
# 
# - split the words by building a placeholder variable: **`word`**  
#   - loop each character in the input string  
#   - check if character is a letter  
#   - add a letter to **`word`** each loop until a non-alpha char is encountered  
# 
# - **if** character is alpha 
#   - add character to **`word`**    
#   - non-alpha detected (space, punctuation, digit,...) defines the end of a word and goes to **`else`**    
# - **`else`**  
#   - check **`if`** word is greater than "g" alphabetically
#       - print word 
#       - set word = empty string
#   - or **else** 
#     - set word = empty string and build the next word  
# 
# Hint: use `.lower()`
# 
# Consider how you will print the last word if it doesn't end with a non-alpha character like a space or punctuation?
# 
# 

# In[34]:


# [] create words after "G" following the Assignment requirements use of functions, menhods and kwyowrds
# sample quote "Wheresoever you go, go with all your heart" ~ Confucius (551 BC - 479 BC)
# [] copy and paste in edX assignment page

def test_words_after_g():
    sentence = input("enter a 1 sentence quote, non-alpha separated words: ").upper()+" "
    word = ""
    for letter in sentence:
        if letter.isalpha():
            word += letter
        if letter == " ":
            if word[0] >= "H":
                print(word)
                word = ""
            elif word[0] <= "G":
                word = ""
        
test_words_after_g()


# ### Need assignment tips and clarification? 
# See the video on the "End of Module coding assignment > Module 1 Required Code Description" course page on [edX](https://courses.edx.org/courses/course-v1:Microsoft+DEV274x+4T2017/course)    
# 
# # Important:  [How to submit code by pasting](https://courses.edx.org/courses/course-v1:Microsoft+DEV274x+2T2017/wiki/Microsoft.DEV274x.2T2017/paste-code-end-module-coding-assignments/)
# 

# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
