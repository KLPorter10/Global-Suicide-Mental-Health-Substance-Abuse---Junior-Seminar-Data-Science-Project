#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

#use pandas to load our csv into a data frame
suicecide_data_frame = pd.read_csv('crude suicide rates.csv')
suicecide_data_frame.head()


# In[32]:


suicecide_data_frame.columns.values 


# In[35]:


suicecide_data_frame.info()


# In[29]:


suicecide_data_frame.shape
suicecide_data_frame.describe


# In[39]:


import seaborn as sns
sns.heatmap(suicecide_data_frame.isnull(),cbar=False,yticklabels=False,cmap = 'viridis')


# In[27]:


drug_data_frame = pd.read_csv('share-with-alcohol-and-substance-use-disorders 1990-2016.csv')
drug_data_frame.head()



# In[33]:


drug_data_frame.columns.values


# In[34]:


drug_data_frame.info()


# In[30]:


drug_data_frame.shape
drug_data_frame.describe


# In[40]:


import seaborn as sns
sns.heatmap(drug_data_frame.isnull(),cbar=False,yticklabels=False,cmap = 'viridis')


# In[ ]:




