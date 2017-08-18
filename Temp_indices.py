# In[1]:

import pandas as pd
import matplotlib.pyplot as plt

get_ipython().magic('matplotlib notebook')


# In[2]:

data = pd.read_csv('CDODiv8652537413133.csv')
data.plot
df = data[['YearMonth', '   TAVG']]
df.head()


# In[3]:

df_20th = df[df['YearMonth'] < 200001]
df_21st = df[df['YearMonth'] >= 200001]

def ex_month(row):
    return str(row['YearMonth'])[4:6]

df_20th['Month'] = df_20th.apply(ex_month, axis=1)
df_20th = df_20th[['Month', '   TAVG']].set_index('Month')


df_21st['Month'] = df_21st.apply(ex_month, axis=1)
df_21st = df_21st[['Month', '   TAVG']].set_index('Month')


# In[4]:

#Dataset #1 - Temperature index for 20th Century
df_20th.head()


# In[5]:

#Dataset #2 - Temperature index for 21st Century
df_21st.head()


# In[6]:

df_20th_avg = df_20th.groupby(df_20th.index)['   TAVG'].mean()
df_20th_avg


# In[7]:

df_21st_avg = df_21st.groupby(df_21st.index)['   TAVG'].mean()
df_21st_avg


# In[80]:

fig = plt.figure(figsize=(8, 5))

months = range(1,13)
temps1 = df_20th_avg.values
temps2 = df_21st_avg.values
w1 = 0.9
w2 = 0.85

plt.bar(months, temps2, width=w2, label="21st Century Temp. Index", color="red", alpha=0.5)
plt.bar(months, temps1, width=w1, label="20th Century Temp. Index", color="gray", alpha=0.9)

legend = plt.legend(bbox_to_anchor=(0.08, -0.1, 0.84, .95), loc=3, ncol=2, mode='expand', handlelength=3, scatterpoints=3)    
legend.get_frame().set_alpha(0.)

ax = plt.gca()

plt.title('Monthly Average Temperature Indices - 21st Century vs 20th Century', size=11)
plt.tick_params(top='off', bottom='off', left='off', right='off', labelleft='off', labelbottom='off')

month_label = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
rects = ax.patches

temps = range(0, 90, 10)
plt.hlines(temps, *ax.get_xlim(), color='k', linestyles='--', lw=0.2, alpha=0.3)
temp_anno_label = list(map(lambda t: '{}$^{{\circ}}$ F'.format(int(t)), temps))
for pos, text in zip(temps, temp_anno_label):
    ax.annotate(s=text, xy =(0, pos), xycoords='data', alpha=0.8, size=8, verticalalignment='center', horizontalalignment='right' , rotation=0)
    
for rect, label in zip(rects, month_label):
    ax.text(rect.get_x() + rect.get_width()/2, 1, label, ha='center', va='bottom', color="w", size=9)
 
for spine in ax.spines.values():
    spine.set_visible(False)



