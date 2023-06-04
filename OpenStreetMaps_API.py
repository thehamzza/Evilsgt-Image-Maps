#!/usr/bin/env python
# coding: utf-8

# ## Import Libraries

# In[1]:


import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings("ignore")
import ast


# ## OpenStreetMaps API

# #### Get Island Data
# 
# use  https://overpass-turbo.eu/ . a tool for testing queries. Send an HTTP GET request to the API using the query. P.S. API has usae limit - be sure to cache results

# In[2]:


# overpass_url = "https://overpass-api.de/api/interpreter"
# query = '''
# [out:json][timeout:25];
# area["name"="Isle of Man"]["place"="island"]->.searchArea;
# (
#   node(area.searchArea);
#   way(area.searchArea);
#   relation(area.searchArea);
# );
# out body;
# >;
# out skel qt;
# '''

# response = requests.get(overpass_url, params={'data': query})
# data = response.json()

# #JSON to dataframe, save DF to reduce API usage
# isleOfMan = pd.DataFrame(data['elements'])
# isleOfMan.to_csv('isleOfMan.csv')

isleOfMan = pd.read_csv('isleOfMan.csv', index_col=0, dtype='unicode')


# In[3]:


isleOfMan['tags'] = isleOfMan.tags.apply(
    lambda x: ast.literal_eval(x) if pd.notnull(x) else None)

isleOfMan['nodes'] = isleOfMan.nodes.apply(
    lambda x: ast.literal_eval(x) if pd.notnull(x) else None)

isleOfMan['members'] = isleOfMan.members.apply(
    lambda x: ast.literal_eval(x) if pd.notnull(x) else None)


isleOfMan['lon'] = pd.to_numeric(isleOfMan['lon'], errors='coerce')
isleOfMan['lat'] = pd.to_numeric(isleOfMan['lat'], errors='coerce')

isleOfMan['id'] = isleOfMan['id'].apply(lambda x: int(x))


# In[ ]:





# #### Plot points

# In[4]:


plt.figure(figsize=(40,24))

plt.scatter(isleOfMan['lon'], isleOfMan['lat'], s=1, alpha=0.1)
plt.xlim([-5.0,-4.0])
plt.ylim([54.0,54.5])

plt.show()


# #### Analyze tags

# Plot 'nodes' that are described by the type 'way' that includes 'boundary' in its tags.
# 
# The tag 'natural' = coastline. does not exist

# In[5]:


# boundary_indexes = []

# for i in range(len(isleOfMan)):
#     if isleOfMan.iloc[i].tags:
#         tags = isleOfMan.iloc[i].tags
#         if 'boundary' in tags:
#             boundary_indexes.append(i)
            
boundary_indexes = [501677,502487,504089,504495,504630,505784,505787,
 505799, 505800, 507713, 507714, 507715, 507716, 507717, 507718, 507719,
 507743, 507744, 507745, 507746, 507747, 507752, 507753, 507754, 507755,
 507757, 507758, 507759, 507760, 507761, 507763, 507764, 507765, 507766,
 507767, 507768, 507769, 507772, 507773, 507774, 507775, 507776, 507777,
 507778, 507779, 507780, 507781, 507783, 507784, 507785, 507787, 507788,
 518560, 518562, 518568, 518570, 518573, 518577, 518580, 525234, 527922,
 527924, 544295, 544298, 564133, 564173, 564174, 564175, 564176, 564177,
 564178, 564179, 564180, 564181, 564182, 564183, 564184, 564185, 564186,
 564187, 564188, 564189, 564190, 564191, 564192, 564193, 564194, 564195,
 564196, 564197, 564198, 564199, 564200, 564201, 564202, 564440, 564553]

boundary_nodes_ids = []
for node_list in isleOfMan.iloc[boundary_indexes]['nodes']:
    if node_list is not None: 
        for node in node_list:
            boundary_nodes_ids.append(node)        
boundary_nodes_ids = list(set(boundary_nodes_ids))


# In[13]:


lon = isleOfMan[isleOfMan['id'].isin(boundary_nodes_ids)]['lon']
lat = isleOfMan[isleOfMan['id'].isin(boundary_nodes_ids)]['lat']

plt.figure(figsize=(40,24))

plt.scatter(lon, lat, s=15, alpha=0.1)
plt.xlim([-5.0,-4.0])
plt.ylim([54.0,54.5])

plt.show()


# What type of tags do we have ?

# Create a DF that has columns as keys and rows as unique key values for the 'tags' column

# In[48]:


# #Convert dict values in column tags into list of dict 
# all_tags = np.array(isleOfMan['tags'])
# # remove None values in list
# all_tags = all_tags[all_tags != np.array(None)]

# # #Convert to DF
# # tags_df = pd.DataFrame(all_tags).apply(lambda x: pd.Series(x.unique()).dropna()).fillna('')
# # #move empty values to bottom
# # tags_df = tags_df.apply(lambda x: x[x != ''].append(x[x == '']).reset_index(drop=True))


# In[ ]:





# In[ ]:




