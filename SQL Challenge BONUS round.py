#!/usr/bin/env python
# coding: utf-8

# In[11]:


from sqlalchemy import create_engine
get_ipython().system('pip install psycopg2-binary')
#from config import user_name, password
engine = create_engine('postgresql://postgres:Str3ngth1805@localhost:5432/SQL_Challenge')
#engine = create_engine(f'postgresql://{user_name}:{password}@localhost:5432/SQL_Challenge')
connection = engine.connect()


# In[12]:


import pandas as pd
results = pd.read_sql("SELECT * FROM employees", connection)
results


# In[ ]:




