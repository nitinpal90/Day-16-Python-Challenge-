#!/usr/bin/env python
# coding: utf-8

# # Day-16 Python Challenge

# # Matplotlib Library

# In[12]:


import matplotlib as plt


# # Linear Graph

# In[54]:


x = [1, 2, 3, 4]
y = [5, 6, 7, 8]

plt.plot(x, y)
plt.show()


# In[17]:


x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
z = 'r'  ## Change the colour
plt.plot(x, y, z)
plt.show()


# # Colour Function

# In[21]:


x = [1, 2, 5, 8, 10]
y = [10, 30, 40, 50, 80]
z = 'g'
plt.plot(x,y, z)
plt.show()


# # Marker function

# In[25]:


x = [1, 2, 5, 8, 10]
y = [10, 30, 40, 50, 80]
z = 'g'
plt.plot(x,y, z, marker = 'o')
plt.show()


# In[27]:


x = [1, 2, 5, 8, 10]
y = [10, 30, 40, 50, 80]
z = 'g'
plt.plot(x,y, z,)
plt.plot(y, marker = '<')
plt.show()


# # Bar Graph

# In[38]:


x = [1,2,3,4]
y = [5,6,7,8]
z = ['r','g','y','b'] ## Use multiple colors 
plt.bar(x,y, color = z)
plt.show()


# # Bar Graph on Horizontal shape

# In[39]:


import numpy as np


# In[41]:


x = np.array(["A", "B", "C", "D"])
y = np.array([2,4,5,6])
z = ['r', 'g', 'y', 'b']
plt.barh(x,y, color = z)
plt.show()


# # Scatter Plot

# In[42]:


import matplotlib.pyplot as plt


# In[47]:


x = [1,2,3,4,5]
y = [10,20,30,40,50]
plt.title("Scatter Plot")
plt.xlabel("Month")
plt.ylabel("Day")
plt.scatter(x,y)
plt.show()


# In[50]:


x = [1,2,3,4,5]
y = [10,20,30,40,50]
plt.title("Scatter Plot")
plt.xlabel("Month")
plt.ylabel("Day")
z = ['red', 'green', 'magenta', 'black', 'pink']
plt.scatter(x,y, color = z)
plt.show()

