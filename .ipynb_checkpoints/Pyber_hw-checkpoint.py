#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

city_data_to_load = "city_data.csv"
ride_data_to_load = "ride_data.csv"

city= pd.read_csv("city_data.csv")
ride= pd.read_csv("ride_data.csv") 

city_ride= pd.merge(city, ride, how='outer', on='city')
city_ride.head()


# In[33]:


city_ride_group= city_ride.groupby(["city"]).agg({'fare':'mean', 'ride_id':'count', "driver_count":"mean", "type":"first"})
city_ride_group.head()


# In[34]:


city_r= city_ride_group.loc[city_ride_group["type"]=="Rural",:]
city_r.head()


# In[36]:


city_u= city_ride_group.loc[city_ride_group["type"]=="Urban",:]
city_u.head()


# In[37]:


city_s= city_ride_group.loc[city_ride_group["type"]=="Suburban",:]
city_s.head()


# In[72]:


plt.rcParams['figure.figsize']=(15,5)


# In[77]:


fig, axes = plt.subplots(nrows=1, ncols=2)
ax1 = axes[0]
ax1.scatter(city_r["ride_id"],city_r["fare"], s=city_r["driver_count"]*10,facecolors="red", alpha= 0.4, edgecolors="black", label= "Rural")
ax1.scatter(city_u["ride_id"],city_u["fare"], s=city_u["driver_count"]*10,marker="o", facecolors="blue",alpha= 0.4, edgecolors="black", label="Urban")
ax1.scatter(city_s["ride_id"],city_s["fare"], s=city_s["driver_count"]*10,marker="o", facecolors="yellow",alpha= 0.4, edgecolors="black",label= "Suburban")            
ax2=axes[1]
ax2.axis("off")
ax2.text(0,0.6,"Note:\nCircle size correlate with driver count per city")
ax1.set_title("Pyber Ride Sharing Data (2016)")
ax1.set_ylabel("Average fare($)")
ax1.set_xlabel("Total Number of Rides (Per city)")
ax1.legend( loc="best")
ax1.grid()
ax1.set_ylim(19, 43)
ax1.set_xlim(0, 45)
fig.tight_layout()
plt.show()


# In[13]:


city_ride_type_uf= city_ride.loc[city_ride["type"]=="Urban",:].groupby(["type"])
ufp= city_ride_type_uf["fare"].sum()
ufp


# In[14]:


city_ride_type_rf= city_ride.loc[city_ride["type"]=="Rural",:].groupby(["type"])
rfp= city_ride_type_rf["fare"].sum()
rfp


# In[15]:


city_ride_type_sf= city_ride.loc[city_ride["type"]=="Suburban",:].groupby(["type"])
sfp= city_ride_type_sf["fare"].sum()
sfp


# In[16]:



labels = ["Rural", "Urban", "Suburban"]

sizes = [4327.93, 39854.38,19356.33 ]

colors = ["red", "orange", "lightskyblue"]

explode = (0, 0, 0)
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct="%1.1f%%", shadow=True, startangle=270)
plt.title("% Total Fares by City Type")
plt.axis("equal")
plt.show()


# In[17]:


city_ride_type_ud= city_ride.loc[city_ride["type"]=="Urban",:].groupby(["type"])
udr= city_ride_type_ud["ride_id"].count()
udr


# In[18]:


city_ride_type_rd= city_ride.loc[city_ride["type"]=="Rural",:].groupby(["type"])
rdr= city_ride_type_rd["ride_id"].count()
rdr


# In[19]:


city_ride_type_sd= city_ride.loc[city_ride["type"]=="Suburban",:].groupby(["type"])
sdr= city_ride_type_sd["ride_id"].count()
sdr


# In[20]:


labels = ["Rural", "Urban", "Suburban"]

sizes = [125, 1625, 625]

colors = ["red", "orange", "lightskyblue"]

explode = (0., 0.1, 0)
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct="%1.1f%%", shadow=True, startangle=270)
plt.title("%Total Rides by City Type")
plt.axis("equal")
plt.show()


# In[21]:


city_ride_type_rdv= city_ride.loc[city_ride["type"]=="Rural",:].groupby(["type"])
rdv= city_ride_type_rdv["driver_count"].sum()
rdv


# In[22]:


city_ride_type_udv= city_ride.loc[city_ride["type"]=="Urban",:].groupby(["type"])
udv= city_ride_type_udv["driver_count"].sum()
udv


# In[23]:


city_ride_type_sdv= city_ride.loc[city_ride["type"]=="Suburban",:].groupby(["type"])
sdv= city_ride_type_sdv["driver_count"].sum()
sdv


# In[24]:


labels = ["Rural", "Urban", "Suburban"]

sizes = [537, 59602, 8570]

colors = ["red", "orange", "lightskyblue"]

explode = (0.1, 0.1, 0.1)
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct="%1.1f%%", shadow=True, startangle=270)
plt.title("%Total Drivers by City Type")
plt.axis("equal")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




