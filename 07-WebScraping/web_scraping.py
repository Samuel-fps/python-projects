#!/usr/bin/env python
# coding: utf-8

# In[83]:


import requests
from bs4 import BeautifulSoup

r = requests.get("https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c = r.content

soup = BeautifulSoup(c, "html.parser")

all = soup.find_all("div", {"class":"propertyRow"})

page_number = soup.find_all("a", {"class":"Page"})[-1].text


# In[84]:


l = []
for page in range(0, int(page_number)*10, 10):
    r = requests.get("https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s=" + str(page))
    # c = r.json()["list"]
    soup = BeautifulSoup(c, "html.parser")
    all = soup.find_all("div", {"class":"propertyRow"})
    for item in all:
        d = {}
        d["Address"] = item.find("h4", {"class":"propPrice"}).text.replace("\n", "").replace(" ", "")
        d["Locality"] = item.find_all("span", {"class":"propAddressCollapse"})[0].text
        d["Price"] = item.find_all("span", {"class":"propAddressCollapse"})[1].text
        try:
            d["Area"] = item.find("span", {"class":"infoBed"}).find("b").text
        except:
            d["Area"] = None
            
        try:
            d["Full Baths"] = item.find("span", {"class":"infoValueFullBath"}).find("b").text
        except:
            d["Full Baths"] =None
            
        try:
            d["Half Baths"] =item.find("span", {"class":"infoValueHalfBath"}).find("b").text
        except:
            d["Half Baths"] = None
    
        for column_group in item.find_all("div", {"class":"columnGroup"}):
            for feature_group, feature_name in zip(column_group.find_all("span", {"class":"featureGroup"}),
                                                   column_group.find_all("span", {"class":"featureName"})):
                if "Lot Size" in feature_group.text:
                    d["Lot Size"] = feature_name.text
        l.append(d)

        


# In[85]:


import pandas
df = pandas.DataFrame(l)


# In[86]:


df


# In[68]:


df.to_csv("Output.csv")

