
# coding: utf-8

# In[1]:


# Primitive types boot camp


# In[2]:


def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits


# In[3]:


x = 1100
count_bits(x)


# In[4]:


x = 11001
count_bits(x)


# ## Know your primitive types

# In[6]:


import sys
sys.float_info


# In[7]:


2**63 - 1


# In[8]:


6&4


# In[9]:


8 >> 1


# In[10]:


1 << 10


# In[13]:


-16 >> 2


# In[14]:


# key methods


# In[15]:


abs(-34.5)


# In[17]:


import math
math.ceil(2.17)


# In[18]:


math.floor(2.17)


# In[19]:


min(8, -4)


# In[20]:


max(8, -4)


# In[21]:


pow(2.71, 3.14)


# In[22]:


math.sqrt(225)


# In[23]:


# interconvert integers and strings


# In[24]:


str(42)


# In[25]:


int('42')


# In[26]:


str(3.14)


# In[27]:


float('3.14')


# In[28]:


float('inf')


# In[29]:


float('-inf')


# In[31]:


math.isclose(10.1, 10.0)


# In[33]:


import random
random.randrange(28)


# In[35]:


random.randint(8, 16)


# In[37]:


random.random()


# In[39]:


A = [1, 2, 3, 4, 5]
random.shuffle(A)
A


# In[40]:


random.choice(A)


# ## 1.1 Computing the parity of a word

# In[41]:


def parity(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result


# In[43]:


x = 101100


# In[44]:


parity(x)


# In[45]:


# https://www.datacamp.com/community/tutorials/python-data-type-conversion

