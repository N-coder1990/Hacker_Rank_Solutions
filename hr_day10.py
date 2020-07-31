import math
import os
import random
import re
import sys

if __name__ == '__main__':

    n = int(input())
    result = bin(n)
    br=result[2:]
    #print(br)
    k=1
    m=[]
    for i in range(len(br)-1):

        if int(br[i])==1:
            
            if int(br[i+1])==1:
                k=k+1
            
            else:
                
                k=1
        m.append(k)
        
seq=max(m)
#print(m)
        
print(seq)
    
#Alternate one line solution
#print(len(max(bin(int(input().strip()))[2:].split('0'))))
    
    




