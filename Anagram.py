#!/usr/bin/env python
# coding: utf-8

# In[2]:


a='cde'
b='dcf'

def makeAnagram(a,b):
    dict1={char:a.count(char) for char in set(a)}
    dict2={char:b.count(char) for char in set(b)}
    delete_count=0
    
    for char in dict1:
        if char in dict2:
            delete_count += abs(dict1[char]-dict2[char])
        else:
            delete_count +=dict1[char]
            
    for char in dict2:
        if char not in dict1:
            delet_count +=dict2[char]
            
        return delete_count


# In[3]:


makeAnagram('cde',"dcf")


# In[4]:


makeAnagram('adcvgt',"cdfvrt")


# In[5]:


makeAnagram('cdetrevg',"dcf")


# In[ ]:




