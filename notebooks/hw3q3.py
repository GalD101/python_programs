#!/usr/bin/env python
# coding: utf-8

# In[ ]:


length = int(input())
all_names = []
all_years = []
good_years = 0
bad_years = 0

for i in range(length):
    all_names.append(input())
    
for name in all_names:
    if int(name.split(' ')[2]) not in all_years:
        all_years.append(int(name.split(' ')[2]))

for year in all_years:
    c_women = 0
    c_men = 0
    
    for name in all_names:
        if int(name.split(' ')[2]) == year:
            if name.lower().startswith('mr'):
                c_men += 1
            elif name.lower().startswith('ms'):
                c_women += 1

    if c_men == c_women:
        good_years += 1
    else:
        bad_years += 1

print(f"Good: {good_years}, Bad: {bad_years}")

    


# 

# In[ ]:





# In[ ]:




