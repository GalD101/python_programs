
# coding: utf-8

# In[11]:


n = int(input())

for i in range(n):
    if i%2==0:
        start = i*n + 1
        end = (i+1)*n + 1
        step = 1
    else:
        start = (i+1)*n 
        end = i*n 
        step = -1

    for j, val in enumerate(range(start,end,step)):
        if i == j:
            val = 0
        my_end = '' if j == n-1 else ' '
            
        print(f"{val:4.0f}", end=my_end)
  
    print()

