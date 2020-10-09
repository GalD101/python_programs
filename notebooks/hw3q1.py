#!/usr/bin/env python
# coding: utf-8

# In[4]:



code = input()
updated_code = ''

i = 0
c_letter = 0
c_num = 0
c_other = 0

while i < len(code):
    if ord('a') <= ord(code[i]) <= ord('z') or ord('A') <= ord(code[i]) <= ord('Z'):
        c_letter += 1
        updated_code += code[i].lower()
    elif ord('1') <= ord(code[i]) <= ord('9'):
        c_num += 1
        if i == 0 or updated_code[-1] != '#':
            updated_code += '#'
    else:
        c_other += 1
        if i == 0 or updated_code[-1] != '@':
            updated_code += '@'
        
    i+=1

print(f"Letters: {c_letter}, Digits: {c_num}, Other: {c_other}")
print(updated_code)
    


# In[ ]:





# In[ ]:




