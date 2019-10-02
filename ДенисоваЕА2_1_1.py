#!/usr/bin/env python
# coding: utf-8

# In[24]:


def funk1(m):
    if len(m)==len(set(m)):
        return('нет повторов')
    else:
        return('есть повторы')


# In[25]:


funk1([1, 2, 3, 4])


# In[26]:


funk1([1, 2, 3, 3, 4, 4])


# In[ ]:




