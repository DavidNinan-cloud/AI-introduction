#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Write a program to demonstrate conditional statements
# Example of if...else
# Program checks if the number is positive or negative
# And displays an appropriate message

num = 3

# Try these two variations as well. 
# num = -5
# num = 0

if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")


# In[2]:


#Example of if...elif...else
#In this program, we check if the number is positive or negative or zero and display an appropriate message

num = 3.4

# Try these two variations as well:
# num = 0
# num = -4.5

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


# In[4]:


# Python Nested if Example
#In this program, we input a number check if the number is positive or
# negative or zero and display an appropriate message This time we use nested if statement

num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")


# In[ ]:




