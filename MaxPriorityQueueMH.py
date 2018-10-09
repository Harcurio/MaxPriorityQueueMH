# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 23:18:10 2018

@author: johor
"""
import random
import math

class MaxPriorityQueue:
       
    def __init__(self, maxN):       
        self.n = 0       
        self.pq = [-1] * maxN
        
    def isEmpty(self):
        return self.n == 0
    
    def size(self):
        return self.n
    
    def insert(self, key):
        self.n = self.n + 1
        self.pq[self.n] = key
        self.swim(self.n)
        
    def delMax(self):   
        kmax = self.pq[1]
        self.exch(1, self.n)
        self.n = self.n - 1
        self.pq[self.n+1] = -1
        self.sink(1)
        return kmax
        
    def less(self,i,j):
        return self.pq[i] < self.pq[j]
    
    def exch(self,i,j):
        self.pq[i] ^= self.pq[j]
        self.pq[j] ^= self.pq[i]
        self.pq[i] ^= self.pq[j]
     
    def swim(self, k):
        while(k > 1 and self.less(math.floor(k/2),k)):
            self.exch(math.floor(k/2),k)
            k = math.floor(k/2)
            
            
    def sink(self, k):
        while(2*k <= self.n):
            j = 2*k
            if(j < self.n and self.less(j, j+1)):
                j = j +1
            if(not self.less(k,j)):
                break
            self.exch(k,j)
            k = j
        

test = MaxPriorityQueue(10)
for i in range(9):
    test.insert(random.randint(0,100))
print(test.pq)
for i in range(10):
    print (test.pq)
    test.delMax()
        
    
       
       
       