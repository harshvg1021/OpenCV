
import cv2


# In[3]:


mountain = cv2.imread('m1.jpg')


# In[4]:


mountain.shape


# In[5]:


mountain = mountain[0:700, : ]


# In[6]:


cv2.imshow('mountain blue', mountain)
cv2.waitKey()
cv2.destroyAllWindows()


# In[7]:


desert = cv2.imread('desert.jpg')


# In[8]:


desert.shape


# In[9]:


cv2.imshow('desert blue', desert)
cv2.waitKey()
cv2.destroyAllWindows()


# In[10]:


import numpy as np


# In[11]:


superpower = np.concatenate((mountain,desert), axis=1)


# In[12]:


cv2.imshow('super blue', superpower)
cv2.waitKey()
cv2.destroyAllWindows()
