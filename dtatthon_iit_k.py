# -*- coding: utf-8 -*-
"""dtatthon-iit-k.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/yd776/9274c0269cce3b709e06f5128af6640e/dtatthon-iit-k.ipynb
"""

import pandas as pd
import numpy as np
import seaborn as sns
import os
from google.colab import files
import datetime

df=pd.read_csv('Book2.csv')



df=df.drop(['Unnamed: 9', 'Unnamed: 10','Unnamed: 11','Unnamed: 12'], axis=1)

df

final_score=[]

for i in range(2,3):
  #a1=[];b1=[];c1=[]
  #a=[];b=[];c=[]
  df2=df.iloc[(57*(i-1)):i*57]
df2

for i in range(1,10001):
  a1=[];b1=[];c1=[]
  #a=[];b=[];c=[]
  df2=df.iloc[(57*(i-1)):i*57]
  k=df2['Sum of Brand_Rx'].tolist()
  a=df2['Sum of YD Email'].tolist()
  b=df2['Sum of YD Sample'].tolist()
  c=df2['Sum of Sales_Rep_Calls'].tolist()
  for j in range(len(k)):
    
    if(a[j]==0):
      a1.append(0)
    else:
      a1.append(k[j])

    if(b[j]==0):
      b1.append(0)
    else:
      b1.append(k[j])
    
    if(c[j]==0):
      c1.append(0)
    else:
      c1.append(k[j])
  total1=sum(a1)
  total2=sum(b1)
  total3=sum(c1)
  
  temp=[total1,total2,total3]
  maxpos = temp.index(max(temp))
  if(sum(temp)==0):
    maxpos=0
  final_score.append(maxpos+1)





df2

df3 = pd.DataFrame(final_score)

print(len(final_score))

final_score[0]

df3.to_csv('file3.csv')

df.iloc[113]

k=[]
l=df['Physician_ID'].tolist()
for i in range(10000):
  k.append(l[57*i])

print(len(k))

df4 = pd.DataFrame(k)

df4.to_csv('file2.csv')

l