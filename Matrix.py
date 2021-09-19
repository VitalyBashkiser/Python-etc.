You have a matrix MxN that represents a map. There are 2 possible states on the map: 1 - islands, 0 - ocean. Your task is to calculate the number of islands in the most effective way. Please write code in Python 3.

Inputs:
M N
Matrix

Examples:
Input:
3 3
0 1 0
0 0 0
0 1 1
Output: 2

Input:
3 4 
0 0 0 1
0 0 1 0
0 1 0 0
Output: 3

Input:
3 4
0 0 0 1
0 0 1 1
0 1 0 1
Output: 2
//////////
import collections, numpy as np 

n=int(input("Enter the number of Rows\n")) 

m=int(input("Enter the number of Columns\n")) 

a = [ [0] * m for i in range(n) ] 

a = np.fliplr(a) 

for i in range (n): 

    for j in range(m): 

        print("Enter Eнlement No:",i,j) 

        a[i][j] = int(input()) 

ez=int(input("print:")) 

print(np.matrix(a)) 

print(np.sum(a) - eрz)
