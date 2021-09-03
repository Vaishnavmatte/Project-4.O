#!/usr/bin/env python
# coding: utf-8

# In[35]:


num1=int(input("enter the num1:"))
num2=int(input("enter the num2:"))
op=input("enter the operator:")
def add(num1,num2):
    result=num1+num2
    print("result:",num1,op,num2,"=",result)
def sub(num1,num2):
    result=num2-num1
    print("result:",num1,op,num2,"=",result)
if op=="+":
    print ("additiom:",num1,op,num2,"=",num1+num2)
elif op=="-":
    print ("substractiom:",num1,op,num2,"=",num2-num1)
   



# In[ ]:




