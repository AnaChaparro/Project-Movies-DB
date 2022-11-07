#!/usr/bin/env python
# coding: utf-8

# ## Funciones de limpieza.

# In[1]:


get_ipython().run_line_magic('pip', 'install ipython')
get_ipython().run_line_magic('pip', 'install seaborn')

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import sys
import re


# In[2]:


#Funciones para limpiar columna sapecial_features:


# In[3]:


def deleted(e):
    
    if 'Deleted' in e:
            
        return 'Yes'
        
    else:
            
        return 'No'


# In[4]:


def behind(e):
    
    if 'Behind' in e:
            
        return 'Yes'
        
    else:
            
        return 'No'


# In[5]:


def comentarios(e):
    
    if 'Commentaries' in e:
            
        return 'Yes'
        
    else:
            
        return 'No'


# In[6]:


def trailer(e):
    
    if 'Trailers' in e:
            
        return 'Yes'
        
    else:
            
        return 'No'


# In[ ]:




