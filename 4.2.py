
import cv2


# In[3]:


mountain = cv2.imread('m1.jpg')


# In[4]:


cv2.imshow('mountain blue', mountain)
cv2.waitKey()
cv2.destroyAllWindows()


# In[5]:


cmountain = mountain[250:495, 140:470]


# In[6]:


cv2.imshow('mountain blue', cmountain)
cv2.waitKey()
cv2.destroyAllWindows()


# In[7]:


desert = cv2.imread('desert.jpg')


# In[8]:


cv2.imshow('desert blue', desert)
cv2.waitKey()
cv2.destroyAllWindows()


# In[9]:


cdesert = desert[0:245, 200:530]


# In[10]:


cdesert.shape


# In[11]:


cv2.imshow('desert blue', cdesert)
cv2.waitKey()
cv2.destroyAllWindows()


# In[12]:


mountain[200:445, 140:470] = cdesert


# In[13]:


cv2.imshow('mountain blue', mountain)
cv2.waitKey()
cv2.destroyAllWindows()


# In[14]:


mountain = cv2.imread('m1.jpg')


# In[15]:


smountain = mountain[250:495, 140:470]


# In[16]:


desert[0:245, 200:530] = smountain


# In[17]:


cv2.imshow('desert blue', desert)
cv2.waitKey()
cv2.destroyAllWindows()
