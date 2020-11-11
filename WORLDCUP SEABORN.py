#!/usr/bin/env python
# coding: utf-8

# In[3]:


from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
WC=pd.read_csv("C:/Users/manut/Documents/Worldcup.csv")
#print(WC.head())
#nueva columna:TOTAL GOALS=>
WC["Total Goals"]=WC["Home Team Goals"]+WC["Away Team Goals"]
print(WC.head())
# Setting styles:
sns.set_style("darkgrid")
sns.set_context("poster", font_scale=0.4)
##figure and subplots
plt.figure(figsize=(25,7))
ax= plt.subplots()
plt.title("Average Number Of Goals Scored In World Cup Matches By Year")

sns.barplot(x="Year", y="Total Goals",data=WC)
plt.xticks(rotation='vertical')
plt.show()


# In[7]:


goals=pd.read_csv("C:/Users/manut/Documents/goals.csv")
#print(goals.head())
sns.set_context("notebook", font_scale=1.25)
f=plt.figure(figsize=(12,7))
ax2=plt.subplots()
plt.title("GOALS/YEAR")

sns.boxplot(x="year",y="goals",data=goals,palette="Spectral")
plt.xticks(rotation=100)
plt.show()
sns.violinplot(x="year",y="goals",data=goals,palette="Spectral")
plt.xticks(rotation='vertical')
plt.show()

