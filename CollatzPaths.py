# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:57:32 2019

@author: anish

Currently not working on bad computers

@Description: 'Adecous' Collatz paths
"""
from operator import itemgetter
from itertools import *
import csv
import time
import pdb


#pdb.set_trace()

adecousPaths=set([1,2,4,8])                                 #Give some initial numbers for easy computations
adecousSeq=set()
adecousList=[]
adecousSeqList=[]
decousPaths=set([3,6,7,9,10,20])                            #Make both sets, as "in" is O(1) for sets
currentPath=[]
currentlyAdecous=False
SeqList=[]
#totTime=0
start_time=time.clock()
def AdecousSequences():
    global adecousList
    global adecousSeqList
    
   
    size_of_list=len(adecousList)
    for number in range(size_of_list):
        if (number+1)!=size_of_list:
            if (adecousList[number]+1==adecousList[number+1]) or (adecousList[number-1]==adecousList[number]-1):
                adecousSeqList.append(adecousList[number])
            else:
                continue
        elif adecousList[number-1]==adecousList[number]-1:
            adecousSeqList.append(adecousList[number])
    
    adecousSeqList.sort()
    
def SeqLen():
    global SeqList
    global adecousSeqList
    for k, g in groupby(enumerate(adecousSeqList), lambda x: x[0]-x[1]):    #groupby groups by the given list, and break instructions at whenever the 
        SeqList.append(list(map(itemgetter(1),g)))                          #difference in elements is not the difference in their respective indices
        
def CollatzPath(number):
    global adecousPaths
    global decousPaths
    global currentPath
    #global totTime
    
    if (number<=1):                                         #Base Case for ending of Collatz
        if (number==1):
            #totTime=totTime+time.clock() - start_time
            #print(totTime)
            return True
            
        if number in currentPath:
            return False                                    #Win a medal if I can return this
        if (number<1):
            return True
    if number in adecousPaths:                              #Check now if number is part of known seq of adecous                       
        adecousPaths|=set(currentPath)                      #Same as set.update()
        #totTime=totTime+time.clock() - start_time
        #print(totTime)
        return True
              
    if number in decousPaths:                               #Same thing for decous paths
        decousPaths|=set(currentPath)           
        #totTime=totTime+time.clock() - start_time
        #print(totTime)
        return True

    currentPath.append(number)  
                        
    if (number%2==0):
        CollatzPath(number/2)
    else:
        CollatzPath(3*number+1)


for i in range(100000001):
    #start_time=time.clock()
    print(i)
    currentPath.clear()
    CollatzPath(i)   
print("Done with adecous paths under one million")
#start_time=time.clock()
#print(start_time)
adecousList=sorted(adecousPaths)
with open("adecous_nums.csv", "w") as outfile:
    writer=csv.writer(outfile)
    for number in adecousList:
        writer.writerow([number])
AdecousSequences()

SeqLen()      
final_set_lengths=set()
for sequence in SeqList:
    final_set_lengths.add(len(sequence))
    
listLengths=sorted(final_set_lengths)

for i in listLengths:
    print(i)

print(start_time)
print(time.clock())


    