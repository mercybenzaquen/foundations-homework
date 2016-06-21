
# coding: utf-8

# In[23]:

get_ipython().system('pip install pandas ')


# In[2]:

import pandas as pd


# In[14]:

df = pd.read_csv("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_month.csv")
df.head()


# In[15]:

earthquakes_df = pd.read_csv("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_month.csv")
earthquakes = earthquakes_df.to_dict('records')


# In[16]:

earthquakes


# In[17]:


earthquake = earthquakes[0]
  


# # PART 1

# # variable for depth

# In[18]:

def depth_to_words(earth_dict):
    depth = earth_dict['depth']
    
    if depth < 70:
        depth_description = "shallow"
    elif (depth > 70) & (depth < 300):
        depth_description = "intermediate"
    elif (depth >300): 
        depth_description = "deep"
    else: 
        depth_description = "no depth recorded"
    return(depth_description)


# call the function
depth_to_words(earthquake)


# # variable for magnitude

# In[19]:

def magnitude_to_words(earth_dict):
    magnitude = earth_dict['mag']
#     mag_words = ""

    if (magnitude >= 0) & (magnitude <= 2):
        mag_words = "micro"
    elif(magnitude > 2) & (magnitude <= 4):
        mag_words = "minor"
    elif (magnitude > 4) & (magnitude <= 6):
        mag_words = "light"
    elif (magnitude > 6) & (magnitude <= 7):
        mag_words = "moderate"
    elif (magnitude > 7) & (magnitude <= 9):
        mag_words = "strong"
    elif magnitude == 10:
        mag_words = "major"
    else:
        mag_words = "no magnitud recorded"
    return mag_words

magnitude_to_words(earthquake)


# # variable for day in words

# In[20]:

import dateutil.parser

def day_in_words(earth_dict):
    time = earthquake['time']

    day_of_the_week = dateutil.parser.parse(time)
    return(day_of_the_week.strftime("%A"))

day_in_words(earthquake)    




# # variable for time in words
# 
# 

# In[21]:

def time_in_words(earth_dict):
    time = earthquake['time']
    python_time = dateutil.parser.parse(time)
    python_time.strftime("%-H")
    if (python_time.hour >= 00) & (python_time.hour < 12):
        time_of_the_day = "morning"
    elif (python_time.hour == 12) & (python_time.hour <= 13):
        time_of_the_day = "noon"
    elif (python_time.hour >= 14) & (python_time.hour < 18):
        time_of_the_day = "afternoon"
    elif (python_time.hour >= 18) & (python_time.hour < 24):
        time_of_the_day = "night"   

        
    return(time_of_the_day)

time_in_words(earthquake)  


# In[22]:

python_time = dateutil.parser.parse('2016-06-14T23:57:34.000Z')


# In[23]:

python_time.hour


# # variable for date in words
# 
# 

# In[24]:

#variable for date in words

def date_in_words(earth_dict):
    date = earthquake['time']
    month_day = dateutil.parser.parse(date)
    return(month_day.strftime("%b %d"))
date_in_words(earthquake)  


# # PART 2

# # eq_to_sentence function

# In[25]:

def eq_to_sentence(earth_dict):
    depth = depth_to_words(earth_dict)
    mag = magnitude_to_words(earth_dict)
    day= day_in_words(earth_dict)
    daytime= time_in_words(earth_dict)
    date= date_in_words(earth_dict)  
    place = earth_dict['place'] 
       
    return("A" + " " +  depth + " " + mag + " " + "earthquake was reported" + " " +day + " " + daytime + " " + "on" + " " + date + " " +place)

print(eq_to_sentence(earthquake))



# # PART 3

# # Doing it in bulk

# In[26]:

for item in earthquakes:
    if item['mag'] >= 4.0:
        print(eq_to_sentence(item))


# # PART 4

# # For non-earthquake types

# In[27]:

def not_eq_to_sentence(earth_dict):
    mag = earth_dict['mag']
    date= date_in_words(earth_dict)  
    place = earth_dict['place'] 
    type_of_event = earth_dict['type']
       
    return("There was also a magnitude" + " " + str(mag)  + " " + type_of_event + " " + "on" + " " + date + " "+ place)

print(not_eq_to_sentence(earthquake))



# In[28]:

for item in earthquakes:
    if item['mag'] >= 4.0:
        print(eq_to_sentence(item))
    if item['type'] != 'earthquake':
        print(not_eq_to_sentence(item))
        
#There was also a magnitude MAGNITUDE TYPE_OF_EVENT on DATE LOCATION.


# In[ ]:




# In[ ]:



