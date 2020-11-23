#!/usr/bin/env python
# coding: utf-8

# In[1]:


#SQL Challenge - BONUS round


# In[2]:


#Import tools to get & read database:
from sqlalchemy import create_engine
from config import password

#Standard tools for visualization:
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

#I added:
import scipy.stats as stats
import seaborn as sns


# In[3]:


#Connect to the database through an engine
engine = create_engine(f'postgresql://postgres:{password}@localhost:5432/SQL_Challenge')
connection = engine.connect()


# In[4]:


#Read the results of "Salaries"
salaries_db = pd.read_sql("SELECT * FROM salaries", connection)
salaries_db


# In[5]:


#BONUS PART 1: Visualize the range of salaries as a histogram
sns.set_style("whitegrid")
salary_graph = sns.displot(salaries_db, x="salary", bins=20, color = "purple") 
salary_graph.set(title = "Salary Distribution")
plt.show()


# In[6]:


# This histogram visualizes a significant slope to the left. It shows that the company 
# salary range bunches around $40,000, which is an interestingly high baseline salary.
# Most notably, this seems to be an extremely large company, with a signficant gap in the
# count of the two lower salaries (thousands more employees recieve a salary of 
# at $40K vs $42K). It seems strange to have such a high baseline but so few people 
# in the next tier above. 


# In[7]:


## Bonus Part Two: Create a bar chart of average salary by title

#  Step one = 
#        Join "Titles"[title_id] to "Employees"[on title_id = emp_title_id] 
#        Join new frame to "Salaries" [on emp_no = emp_no]
#  Step two = visualize



# In[8]:


employees_db = pd.read_sql("SELECT * FROM employees", connection)
employees_db


# In[9]:


employees_db_new = employees_db.rename(columns={"emp_title_id":"title_id"})
employees_db_new


# In[10]:


titles_db = pd.read_sql("SELECT * FROM titles", connection)
titles_db


# In[11]:


first_merge = pd.merge(employees_db_new, titles_db, on="title_id")
first_merge


# In[12]:


second_merge = pd.merge(first_merge, salaries_db, on="emp_no")
second_merge


# In[13]:


#Visulaize salaries using a seaborn Bar Chart

salary_barplot = sns.barplot(x="title", y="salary", data=second_merge, palette="colorblind")
plt.xticks(rotation=90)
plt.show()


# In[14]:


# This bar chart does not show the expected distribution of salaries by title.
# Instead, this visualization demonstrates that most salary ranges titles are within 
# $15,000 of each other. Additionally, senior staff and junior staff in the same 
# job titles make roughly the same salaries (ex. Staff and Senior Staff; 
# Engineer, Senior Engineer and Assistant Engineer)


# In[15]:


#Employee ID number 499942 is assigned to April Foolsday

employees_db_new[employees_db_new["emp_no"]==499942]


# In[ ]:




