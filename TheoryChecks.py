# -*- coding: utf-8 -*-
"""
Created on Mon May 20 17:39:59 2019

@author: anish
"""
import time
import pdb

start_time=time.clock()
adecousPaths=set([1,2,4,8])                                 #Give some initial numbers for easy computations
decousPaths=set([3,6,7,9,10,20])                            #Make both sets, as "in" is O(1) for sets
currentPath=[]
totTime=0
print("hello")
def CollatzPath(number):  
    global totTime
    if (number<=1):                                         #Base Case for ending of Collatz
        if (number==1):
            totTime=totTime+time.clock() - start_time
            print(totTime)
            return True
        if number in currentPath:
            return False                                    #Win a medal if I can return this
        if (number<1):
            return True
              
    currentPath.append(number)                         
    if (number%2==0):
        CollatzPath(number/2)
    else:
        CollatzPath(3*number+1)
        
#pdb.set_trace()
for i in range(1000001):
    start_time=time.clock()
    CollatzPath(i)
print("finale")
