#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[36]:


data = pd.read_excel(r'C:\Users\Admin\Downloads\Test_File.xlsx')


# In[17]:


data.head()


# In[18]:


data.info()


# In[19]:


df = data[["SW","PL"]]


# In[20]:


df.head()


# In[37]:


body_table = df.to_html(table_id = "Your Table", index=False)


# In[38]:


with open("C:/Users/Admin/Downloads/before table html.txt") as body_file:
    body_html = body_file.read()
    
final_html = body_html+body_table


# In[39]:


with open("C:/Users/Admin/Downloads/new_html_file.html","w") as html_file:
    html_file.write(final_html)


# In[40]:


SW1 = df['SW'].loc[df.index[0]]


# In[41]:


print(SW1)


# In[ ]:




