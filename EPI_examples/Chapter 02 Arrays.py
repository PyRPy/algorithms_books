
# coding: utf-8

# # Chapter 2 Arrays

# ## Array boot camp

# In[2]:


def even_odd(A):
    next_even , next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[ next_even ] % 2 == 0:
            next_even += 1
        else:
            A[ next_even ], A[next_odd] = A[next_odd], A[ next_even ]
            next_odd -= 1


# In[3]:


A = [2, 3, 5, 7, 9, 11, 13, 17]


# In[4]:


even_odd(A)


# In[5]:


print(A)


# In[6]:


A = [2, 3, 5, 7, 11, 13, 17, 0]


# In[7]:


even_odd(A)
print(A)


# ## Know your array libraries

# In[10]:


[1] + [0] * 10


# In[12]:


list(range(10))


# In[ ]:


# basic operations


# In[13]:


len(A)


# In[14]:


A.append(42)


# In[15]:


A


# In[16]:


A.remove(2)


# In[17]:


A


# In[18]:


A.insert(3, 28)


# In[19]:


A


# In[ ]:


# instantiate a 2D array


# In[20]:


[[1, 2, 4], [3, 5, 7, 9], [13]]


# In[21]:


# if a value in an array
11 in A


# In[22]:


B = A


# In[23]:


B


# In[24]:


B = list(A)


# In[25]:


B


# In[27]:


A.copy()


# In[29]:


# deep copy
import copy
C = copy.deepcopy(A)


# In[30]:


C


# In[31]:


A[1] = 8


# In[32]:


A


# In[33]:


B


# In[34]:


C


# In[35]:


# try it again
B = A
C = copy.deepcopy(A)


# In[36]:


B, C


# In[37]:


A[2] = 18


# In[38]:


A


# In[39]:


B, C


# In[40]:


# C is not changed


# In[41]:


# key methods in list
min(A)


# In[42]:


max(A)


# In[43]:


# bisection search
import bisect
bisect.bisect(A, 3)


# In[46]:


bisect.bisect(A, 5)


# In[47]:


A.reverse()


# In[48]:


A


# In[49]:


A.sort()
A


# In[50]:


del A[2]


# In[51]:


A


# In[53]:


del A[0:1] # not include A[1]


# In[54]:


A


# In[55]:


# slicing of arrays
A = [1, 6, 3, 4, 5, 2, 7]


# In[56]:


A[2:4]


# In[57]:


A[2:]


# In[58]:


A[4:]


# In[59]:


A[-1]


# In[60]:


A[-3]


# In[61]:


A[-3:-1] # not include -1


# In[62]:


A[1:5:2]


# In[64]:


A[5:1:-2]


# In[66]:


A[5]


# In[67]:


A[::-1]


# In[68]:


# rotate
A[2:] + A[:2]


# In[70]:


# shallow copy
B = A[:]


# In[72]:


# list comprehension
[x**2 for x in range(6)]


# In[73]:


[x**2 for x in range(6) if x % 2 == 0]


# In[75]:


# multiple levels of looping
A = [1, 3, 5]
B = ['a', 'b']

[(x, y) for x in A for y in B]


# In[77]:


M = [['a', 'b', 'c'], ['d', 'e', 'f']]
[x for row in M for x in row]


# In[79]:


A = [[1, 2, 3], [4, 5, 6]]
[[x**2 for x in row] for row in A]


# ## 2.1 Dutch national flog problem

# In[84]:


A = [0, 1, 2, 0, 2, 1, 1]


# In[85]:


RED , WHITE , BLUE = range(3)
def dutch_flag_partition (pivot_index , A):
    pivot = A[ pivot_index ]
    # First pass: group elements smaller than pivot.
    for i in range(len(A)):
        # Look for a smaller element.
        for j in range(i + 1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break

    # Second pass: group elements larger than pivot.
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        # Look for a larger element. Stop when we reach an element less than
        # pivot , since first pass has moved them to the start of A.
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break


# In[86]:


dutch_flag_partition(3, A)


# In[87]:


A


# In[ ]:


# http://elementsofprogramminginterviews.com/sample/epilight_python_new.pdf

