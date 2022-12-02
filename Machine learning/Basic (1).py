#!/usr/bin/env python
# coding: utf-8

# In[2]:


def ex1(A):
    Even=[]
    Odd=[]
    for i in A:
        if i%2==0:
            Even.append(i)
        else:
            Odd.append(i)
    print('Even:',Even)
    print('Odd:',Odd)
    
B=[4,2,1,5,12,512]
ex1(B)


# In[17]:


def ex2(A): # check type 
    Num=[]
    Str=[]
    for i in A:
        if isinstance(i,int):
            Num.append(i)
        else:
            Str.append(i)
    print('Num:',Num)
    print('String:',Str)
    
C=[234,'asdasd31',4124,'2131dsad']
ex2(C)


# In[39]:


def ex3(A,B): # multiply matrices example matrix(3,2) * matric(2,3) = matrix(3,3)
    result=[[0 for x in range(len(A))] for y in range(len(B[0]))]
    for i in range(len(A)): # Rows of matrix A
        for j in range(len(B[0])): # columns of matrix B
            for k in range(len(B)): # rows of matrix B
                result[i][j]+= A[i][k]*B[k][j]
    for i in result:
        print(i)

A=[[1,2],[3,4],[4,5]]
B=[[1,2,3,],[4,5,6]]
ex3(A,B)
    
    


# In[ ]:





# In[ ]:





# In[ ]:




