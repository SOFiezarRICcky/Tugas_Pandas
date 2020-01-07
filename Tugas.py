#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt


# In[45]:


import numpy as np

theta = np.linspace(0, 2*np.pi,30)

fig, ax = plt.subplots(1)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Tugas")


r = np.sqrt(19.0)
x1 = r*np.cos(theta)
x2 = r*np.sin(theta)
ax.plot(x1, x2, "g--")


r2 = np.sqrt(10.0)
x3 = r2*np.cos(theta)
x4 = r2*np.sin(theta)
ax.plot(x3,x4, "r*-")

r3 = np.sqrt(5.0)
x5 = r3*np.cos(theta)
x6 = r3*np.sin(theta)
ax.plot(x5, x6, "y")



plt.xlim(-4.95, 4.95)
plt.ylim(-4.95, 4.95)

plt.show()


# In[46]:


theta = np.linspace(0, 2*np.pi,30)
theta


# In[ ]:




