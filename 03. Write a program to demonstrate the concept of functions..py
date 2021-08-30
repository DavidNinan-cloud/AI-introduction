#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Example of a function
def greet(name):
# This function greets to the person passed in as a parameter
    
    print("Hello, " + name + ". Good morning!")
#To call a function in python
greet('Paul')


# In[2]:


#Example of return
def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""

    if num >= 0:
        return num
    else:
        return -num


print(absolute_value(2))

print(absolute_value(-4))


# In[3]:


#example to illustrate the scope of a variable inside a function
def my_func():
	x = 10
	print("Value inside function:",x)

x = 20
my_func()
print("Value outside function:",x)


# In[ ]:




