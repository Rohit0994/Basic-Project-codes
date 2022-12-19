#!/usr/bin/env python
# coding: utf-8

# In[82]:


input_lists = [[5,5,5,8,10],[5,5,7,8],[5,5,8,9,11]]

def commonElements(l1, l2):
    list1 = l1.copy()
    list2 = l2.copy()
    
    common_elements = []
    # traverse the list 1
    for i  in list1:
        # Check if i is present in list2
        if i in list2:
            # remove the i from list2
            list2.remove(i)
            # Append it to a list
            common_elements.append(i)

    return common_elements


# In[83]:


c_list = commonElements(input_lists[0], input_lists[1])

for l in input_lists[2:]:
    c_list = commonElements(c_list, l)
    
print("Common Elements", c_list)


# In[ ]:





# In[ ]:




