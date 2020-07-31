import os
import random
import re
import sys

def hg(x,y):
    ind=((x,y),(x,y+1),(x,y+2),(x+1,y+1),(x+2,y),(x+2,y+1),(x+2,y+2))
    return ind


if __name__ == '__main__':
    arr = []
    total=[]
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    for i in range(4):
        for j in range(4):
            ind=hg(i,j)
            hour_glass=[]
            for x,y in ind:
                hour_glass.append(arr[x][y])
            #print(hour_glass)
            total.append(sum(hour_glass))        
    
    print(max(total))
