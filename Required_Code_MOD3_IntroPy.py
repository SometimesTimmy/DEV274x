
# coding: utf-8

# 
# #  Module 3 Required Coding Activity  
# Introduction to Python (Unit 2) Fundamentals  
# 
# **This Activity is intended to be completed in the jupyter notebook, Required_Code_MOD3_IntroPy.ipynb, and then pasted into the assessment page that follows.**   
#  
# All course .ipynb Jupyter Notebooks are available from the project files download topic in Module 1, Section 1.
# 
# This is an activity from the Jupyter Notebook **`Practice_MOD03_IntroPy.ipynb`** which you may have already completed.
# 
# |  Assignment Requirements |  
# |:-------------------------------|  
# | **NOTE:** This program requires **`print`** output and using code syntax used in module 3: **`if`**, **`input`**, **`def`**, **`return`**, **`for`**/**`in`** keywords, **`.lower()`** and **`.upper()`** method, **`.append`**, **`.pop`**, **`.split`** methods, **`range`** and **`len`** functions  |  
# 
# ## Program: poem mixer  
# This program takes string input and then prints out a mixed order version of the string    
# 
# 
# **Program Parts**  
# - **program flow** gathers the word list, modifies the case and order, and prints      
#   - get string input, input like a poem, verse or saying 
#   - split the string into a list of individual words  
#   - determine the length of the list
#   - Loop the length of the list by index number and for each list index:  
#     - if a word is short (3 letters or less) make the word in the list lowercase 
#     - if a word is long (7 letters or more) make the word in the list uppercase   
#   - **call the word_mixer** function with the modified list  
#   - print the return value from the word_mixer function  
# 
# - **word_mixer** Function has 1 argument: an original list of string words, containing greater than 5 words and the function returns a new list.   
#   - sort the original list  
#   - create a new list  
#   - Loop while the list is longer than 5 words:  
#     - *in each loop pop a word from the sorted original list and append to the new list*  
#     - pop the word 5th from the end of the list and append to the new list  
#     - pop the first word in the list and append to the new list  
#     - pop the last word in the list and append to the new list  
#   - **return** the new list on exiting the loop
# 
# 
# 
# ![TODO: upload image to blob](https://qitcyg-ch3302.files.1drv.com/y4mtK8FJlu7bvNCw_NFrJNnMEX05-bGQKZ-ljIB7ofo8jg14zZKLdYrjXQfPcL1PnNKqaBc_v85pd-47J8BBRN3Eg5LXSmxbhZG99zHmQwVTSQBd6n3S1IXgcG0lqjA8PGW1NVMQyPtX-_m_sGry5j1iCJzjiZmUrFmGckPrEYxvjPIHHelgxQ4oVYG32S32otj0cdV8f9aDv3cnvb9AvDKqg?width=727&height=586&cropmode=none)
# 
# 
#  **input example**  *(beginning of William Blake poem, "The Fly")*
# 
#  >enter a saying or poem: `Little fly, Thy summer’s play My thoughtless hand Has brushed away. Am not I A fly like thee? Or art not thou A man like me?`  
# 
# 
# **output example**   
# >`or BRUSHED thy not Little thou me? SUMMER’S thee? like THOUGHTLESS play i a not hand a my fly am man`
# 
# 
# **alternative output** in each loop in the function that creates the new list add a "\\n" to the list   
# ```
#  or BRUSHED thy 
#  not Little thou 
#  me? SUMMER’S thee? 
#  like THOUGHTLESS play 
#  i a not 
#  hand a my 
#  fly am man
# ```
# 
# 

# In[21]:


# [] create poem mixer
# [] copy and paste in edX assignment page

def run_word_mixer():
    words = input("enter a saying or poem: ")
    words_list = words.split()
    L = len(words_list)
    for word in range(L):
        if len(words_list[word]) <= 3:
            words_list[word] = words_list[word].lower()
        elif len(words_list[word]) >= 7:
            words_list[word] = words_list[word].upper()
    new_words = word_mixer(words_list)
    print(" ".join(new_words))
    
def word_mixer(words_list):
    words_list.sort()
    new_words = [ ]
    while len(words_list) > 5:
        new_words.append(words_list.pop(-5))
        new_words.append(words_list.pop(0))
        new_words.append(words_list.pop(-1))
    return new_words

run_word_mixer()


# ### Need assignment tips and clarification? 
# See the video on the "End of Module coding assignment > Module 3 Required Code Description" course page on [edX](https://courses.edx.org/courses/course-v1:Microsoft+DEV274x+4T2017/course)    
# 
# # Important:  [How to submit code by pasting](https://courses.edx.org/courses/course-v1:Microsoft+DEV274x+2T2017/wiki/Microsoft.DEV274x.2T2017/paste-code-end-module-coding-assignments/)
# 

# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
