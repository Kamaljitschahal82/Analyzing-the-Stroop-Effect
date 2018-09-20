
# coding: utf-8

# ### Analyzing the Stroop Effect
# Perform the analysis in the space below. Remember to follow [the instructions](https://docs.google.com/document/d/1-OkpZLjG_kX9J6LIQ5IltsqMzVWjh36QpnP2RYpVdPU/pub?embedded=True) and review the [project rubric](https://review.udacity.com/#!/rubrics/71/view) before submitting. Once you've completed the analysis and write-up, download this file as a PDF or HTML file, upload that PDF/HTML into the workspace here (click on the orange Jupyter icon in the upper left then Upload), then use the Submit Project button at the bottom of this page. This will create a zip file containing both this .ipynb doc and the PDF/HTML doc that will be submitted for your project.
# 
# 
# (1) What is the independent variable? What is the dependent variable?

# # Independent variable : is the congruency of the pair of words & dependent variable is the reaction time in seconds to name the colours with which the words are written.

# (2) What is an appropriate set of hypotheses for this task? Specify your null and alternative hypotheses, and clearly define any notation used. Justify your choices.

# # to test the relationship between the reaction times for the two conditions (congruent and incongruent).
# 
# Two conditions are : 
# we are assuming there is no difference between population means.
# 
# H0(null): The population means for response times for congruent and incongruent are the same.
# µ_congruent = µ_incongruent ( no difference in response time between  congruent  & incongrudent)
# 
# 
# HA(alternative): The population means for response times for congruent and incongruent are not the same.
# µ_congruent != µ_incongruent ( there is extreme response time difference between  congruent & incongrudent)
# 
# 
# 
# An appropriate statistical test to perform in an attempt to determine the likelihood of each these hypotheses is a dependent measures t-test.
# The selection of T-test is due to the fact that, we are comparing reaction time of a sample from same population in two different conditions and hence coming to a conclusion about the population.
# Also, presence of outliers as shown by part 4 figure . use of t-test ensures the robustness even if the data is not normally distributed. This ensures the violation of assumptions without any significant errors being introduced.
# our sample size less than 30 and we don't know the population standard deviations.

# (3) Report some descriptive statistics regarding this dataset. Include at least one measure of central tendency and at least one measure of variability. The name of the data file is 'stroopdata.csv'.

# In[31]:


import os
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

df = pd.read_csv('stroopdata.csv')
df.head()


# In[32]:


print("Count=")
print(df.count())
print("\n")
print("Max=")
print(df.max())
print("\n")
print("Min=")
print(df.min())
print("\n")
print("Mean=")
print(df.mean())
print("\n")
print("Std=")
print(df.std())
print("\n")
print("decsribe=")
print(df.describe())
print("\n")
print("median=")
print(df.median())
print("\n")
print("correlation=")
print(df.corr())
print("\n")


# In[33]:


df.info()


# (4) Provide one or two visualizations that show the distribution of the sample data. Write one or two sentences noting what you observe about the plot or plots.

# In[34]:


df['Index']=df.index.values


# In[35]:



x = df['Index']
y = df['Congruent']
colors = 'orange'
area = np.pi * 20 

fig = plt.figure()

ax = fig.add_subplot(111)
fig.subplots_adjust(top=1)
ax.set_title('Congruent Words:Samples Reaction time',fontsize=16)
ax.set_xlabel('Index')
ax.set_ylabel('Time in seconds')
fig.subplots_adjust(top=0.85)
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.yticks(np.arange(0, 24, 2))
plt.scatter(x, y, s=area, c=colors, alpha=0.8)
plt.ylim([5,24])
plt.xlim([0,23])
plt.show()


x = df['Index']
y = df['Incongruent']
colors = 'red'
area = np.pi * 20 

fig = plt.figure()

ax = fig.add_subplot(111)
fig.subplots_adjust(top=1)
ax.set_title('InCongruent Words:Samples Reaction time',fontsize=16)
ax.set_xlabel('Index')
ax.set_ylabel('Time in seconds')

plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.yticks(np.arange(13, 36, 2))
plt.scatter(x, y, s=area, c=colors, alpha=0.8)
plt.ylim([13,36])
plt.xlim([0,23])
plt.show()


# # The congruent words distribution which is between 8 and 20 seconds and lower average completion time compared to the incongruent words. There is one outlier in congruent words at 22 seconds.For Incongruent words distibtuion is between 15 to about 27 seconds & 2  outliers appears at 34 & 35 seconds. higher average completion time as described by mean value(22.015917)

# (5)  Now, perform the statistical test and report your results. What is your confidence level or Type I error associated with your test? What is your conclusion regarding the hypotheses you set up? Did the results match up with your expectations? **Hint:**  Think about what is being measured on each individual, and what statistic best captures how an individual reacts in each environment.

# In[36]:


from scipy.stats import t
t.ppf(.95, 23)


# # For a confidence level of 95% and 23 degrees of freedom with alpha level =0.05, our t-critical value = 1.7138715277470473
# # for a confidence level of 95% and 23 degrees with two tail test & alpha level =0.0250 , t critical value = 2.069
# # (based on https://s3.amazonaws.com/udacity-hosted-downloads/t-table.jpg).

# # difference between mean of congruent & incongruent is ( 22.015917 -14.051125)= 7.9

# In[37]:


print("Std=")
print(df.std())
print("\n")


# In[38]:


print("standard deviation of the differences of two conditions=")
df['differ']=df['Congruent'] - df['Incongruent']
print("STD_diff = {0:.4f} ".format( df['differ'].std(axis=0)))


# In[39]:


(df['Incongruent'].mean()- df['Congruent'].mean())/(4.8648/math.sqrt(24))


# # t-statistic results =  (8.0207513118339637) which is greater than t-critical value (1.7138715277470473),So we can reject the null hypothesis.
# this matches with our expectation, as it takes less response time for  congruent words than incongruent words.
# 

# # references : 
# 
# https://en.wikipedia.org/wiki/Stroop_effect
#     
# 
# Formula used for t-test :
#     
# However, t-scores are used when you don’t know the population standard deviation; You make an estimate by using your sample.
# T = (X – μ) / [ s/√(n) ].
# 
# Where:
# 
#     s is the standard deviation of the sample.
#    

# (6) Optional: What do you think is responsible for the effects observed? Can you think of an alternative or similar task that would result in a similar effect? Some research about the problem will be helpful for thinking about these two questions!

# --write answer here--
