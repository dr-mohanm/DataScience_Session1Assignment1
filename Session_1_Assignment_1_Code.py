
# coding: utf-8

# In[1]:


#1. Install Jupyter notebook and run the first program and share the screenshot of the output.  

print('hello world')


# In[17]:


#2. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
#between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line. 
l1=[]
#for x in range(2000, 3201):
for x in range(2000, 3201):
    if (x%7==0) and (x%5!=0):
        l1.append(str(x))
print (','.join(l1))


# In[2]:


#3. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order 
#with a space between first name and last name. 
fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)


# In[20]:


#4. Write a Python program to find the volume of a sphere with diameter 12 cm.  
#Formula: V=4/3 * π * r 3
import math
pi = math.pi
r = float(12/2)
V=4/3*pi*r**3
print(V)

