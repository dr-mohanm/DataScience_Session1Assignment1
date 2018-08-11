
# coding: utf-8

# In[4]:


#1. Install Jupyter notebook and run the first program and share the screenshot of the output.  

# Message displayed using print statement

print('hello world')


# In[2]:


#2. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
#between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line. 

#Iterate values from 2000 to 3201 to increment the value by 1 every time.
#Range doesn't include the last value, it used 3201 to include the value 3200 in iteration. 
# check if the number is divisible by 7 not a multiple of 5.
#if matches store in the list and append the values one by one using comma delimiter
# print the list of values from the list.

l1=[]
#for x in range(2000, 3201):
for x in range(2000, 3201):
    if (x%7==0) and (x%5!=0):
        l1.append(x)
print (l1)


# In[3]:


#3. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order 
#with a space between first name and last name.

# Accpet fname and lname from user.
# Print the names in reverse order, which means lname and then fname to print it in reverse order

fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)


# In[6]:


#4. Write a Python program to find the volume of a sphere with diameter 12 cm.  
#Formula: V=4/3 * π * r 3

# Import math function to get the default pi value
# calcukate the radius value by dividing diameter by half.
# calculate volume using the formula used in the code
# Print the volume value using print statement

import math
pi = math.pi
r = float(12/2)
V=4/3*pi*r**3
print(V)

