#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import library yang dibutuhkan
import re
#function email_check
def email_check(input):
	match = re.search('(?=^((?!-).)*$)(?=[^0-9])((?=^((?!\.\d).)*$)|(?=.*_))',input )
	if match:
		print('Pass')
	else:
		print('Not Pass')
#Masukkan daftar email ke dalam list
emails = ['my-name@someemail.com', 'myname@someemail.com','my.name@someemail.com',
'my.name2019@someemail.com', 'my.name.2019@someemail.com',
'somename.201903@someemail.com','my_name.201903@someemail.com',
'201903myname@someemail.com', '201903.myname@someemail.com']
#Looping untuk pengecekan Pass atau Not Pass
for email in emails :
	email_check(email)


# In[ ]:




