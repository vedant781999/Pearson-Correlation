
import pandas as pd
import numpy as np
import math
from math import sqrt

file_1 = pd.read_csv('1.csv')
file_2 = pd.read_csv('2.csv')
file_3 = pd.read_csv('3.csv')
file_4 = pd.read_csv('4.csv')
file_5 = pd.read_csv('5.csv')

#Drop the unnecessary columns
file_1.drop(file_1.columns[[0,1,2]], axis=1, inplace=True)
file_2.drop(file_2.columns[[0,1,2]], axis=1, inplace=True)
file_3.drop(file_3.columns[[0,1,2]], axis=1, inplace=True)
file_4.drop(file_4.columns[[0,1,2]], axis=1, inplace=True)
file_5.drop(file_5.columns[[0,1,2]], axis=1, inplace=True)

#Convert to numpy 
file_1 = file_1.values
file_2 = file_2.values
file_3 = file_3.values
file_4 = file_4.values
file_5 = file_5.values

def cal_relevant_attributes(file):
  corr_matrix = [[0 for x in range(len(file[0])-1)] for x in range(len(file[0])-1)]

  for i in range(len(file[0])-1):
    for j in range(len(file[0])-1):
      temp = np.corrcoef(file[:,i], file[:,j])
      corr_matrix[i][j]=temp[0][1]
  relevant_array = [1 for x in range(len(file[0])-1)]

  for i in range(len(file[0])-1):
    for j in range(i+1,len(file[0])-1):
      if relevant_array[i] == 0:
        break
      else:
        if corr_matrix[i][j]>=0.7 or corr_matrix[i][j]<=-0.7:
          relevant_array[j] = 0
  
  final_relevant_attr = []
  for i in range(len(file[0])-1):
    if relevant_array[i]==1:
      final_relevant_attr.append(i)
  #final_relevant_attr gives the set of non-correlated attributes.

cal_relevant_attributes(file_1)

