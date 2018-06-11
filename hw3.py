
# coding: utf-8

# In[6]:


x=input('Please type anything:\n')

a=dict()
a={}
for letter in x:
        if letter in a:
            a[letter] += 1
        else:
            a[letter] = 1
    


for letter, count in a.items():
    print("\""+letter+"\":",count)
