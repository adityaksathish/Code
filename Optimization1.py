# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 11:18:34 2017

@author: adity
"""
###Linear Search

def linearSearch (F,target):
    for x in range(len(F)):
        if (F[x]==target):
            return x
    return False

#Testing Linear Search Function to look for the number 6
target = 6
F = range(40)

print "Example 1: Linear Search"
print "Searching for [{}] in {}".format(target,F)
print "The number {} has an index of".format(target), linearSearch (F, target), "in the list", F


###Exhaustive Enumeration
def linearSearch_sqrt(N):
    epsilon = 0.001
    x = 0.000
    while x*x < N - epsilon:
        x += epsilon
    return x

from math import sqrt 
N = 15
print "Example 2: Linear Search to find the Square Root"
print "Finding the sqaure root of {}".format(N)
print "The square root of {} using linear search is".format(N) 
print linearSearch_sqrt(N)
print "The square root of {} using the sqrt function in the math package is".format(N)
print sqrt(N)


####Binary Search 

def binarySearch(A, target):
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = low + (high - low) / 2
        print "LOW {} HI {} MID {}, comparing {} to {}".format(low,high,mid,target,A[mid])
        if A[mid] == target:
            return mid
        if A[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return False

F = range(32)
target = 4
print "Example 3: Binary Search"
print "Looking for [{}] in array {}".format(target,F)
print binarySearch (F,target)

###Code for Q5 Finding a Square Root
def bisection_search_kth_root(N,k):
    epsilon = 0.001
    low = 0.000
    high = 1000000.000
    while low <= high:
        mid = low + (high - low) / 2
        print "LOW {} HI {} MID {}, comparing {} to {}".format(low,high,mid,mid**k,N)
        if abs((mid**k) - N) <= epsilon:
            return mid
        if mid**k > N:
            high = mid - epsilon
        else:
            low = mid + epsilon
    return mid

N = 100
K = 2
print "Question 1: Finding a root using Bisection Search"
print "Looking for {} root of {}".format(K,N)
print bisection_search_kth_root(N,K), "is the {} root of {}".format(K,N)

###Finding Largest N!
from math import log

def bisection_search_lgN(N):
    epsilon = 0.001
    low = 0.000
    high = 0.001
    while (high*log(high,2)) - high + 1 <= N:
        high = high * 2
    while low <= high:
        mid = low + (high - low) / 2
        print "LOW {} HI {} MID {}, comparing {} to {}".format(low,high,mid,(mid*log(mid,2)),N)
        if abs(((mid*log(mid,2)) - mid + 1) - N) <= epsilon:
            return int(mid)
        if (mid*log(mid,2)) - mid + 1 > N:
            high = mid - epsilon
        else:
            low = mid + epsilon
    return int(mid)
       
N = pow(2,43)
print "Question 2: Largest N! that can be stored in 1TB of free space"
print bisection_search_lgN(N), "factorial can be stored in 1TB of free space"

###Newton Raphson
def newton_sqrt(k):
    epsilon = .001
    y = k / 2.0 #guess
    while abs(y*y-k) >= epsilon:
        y = y - (((y**2) - k)/(2*y))
    return y

print "Example 4: Newton Raphson"
k = 25
print "The square root of {} is".format(k)
print newton_sqrt(k)




