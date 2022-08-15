#!/usr/bin/env python
# coding: utf-8

# # Flag of India

# In[46]:


import numpy as np
import matplotlib.pyplot as py
import matplotlib.patches as patch

#India Flag Color Codes, India saffron #FF9933, white #FFFFFF, India green #138808, navy blue #000080.
a=patch.Rectangle((0,1), width=9, height=2, facecolor='#138808', edgecolor='grey')
b=patch.Rectangle((0,3), width=9, height=2, facecolor='#FFFFFF', edgecolor='grey')
c=patch.Rectangle((0,5), width=9, height=2, facecolor='#ff9933', edgecolor='grey')
m,n=py.subplots()
n.add_patch(a)
n.add_patch(b)
n.add_patch(c)

#Ashock chakra
radius=0.8
py.plot(4.5,4,marker='o', markerfacecolor= '#000088', markersize=9.5)
chakra = py.Circle((4.5,4), radius, color='#000088', fill=False, linewidth=7)
n.add_artist(chakra)

#24-spoke wheel
for i in range(0,24):
    p = 4.5+radius/2 * np.cos(np.pi*i/12+np.pi/48)
    q = 4.5+radius/2 * np.cos(np.pi*i/12-np.pi/48)
    r = 4+radius/2 * np.sin(np.pi*i/12+np.pi/48)
    s = 4+radius/2 * np.sin(np.pi*i/12-np.pi/48)
    t = 4.5+radius * np.cos(np.pi*i/12)
    u = 4+radius * np.sin(np.pi*i/12)
    n.add_patch(patch.Polygon([[4.5,4], [p,r], [t,u],[q,s]], fill=True, closed=True, color='#000088'))
py.axis('equal')
py.show() 
print("Happy Independence Day!")
#Refence- clcoding.com, wikipedia, LinkedIn, github


# In[ ]:




