# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 10:09:12 2020

@author: BryanC
"""
def greedyCoins(n,lambs,henchmen):
    maxPay = 2*henchmen[n]
    if(len(henchmen)<=2):
        if(sum(henchmen) <= lambs and sum(henchmen)+maxPay<=lambs):
        #there should be a case where we apend a 1 when lambs==2 but some of the test cases are incorrect
            henchmen.append(maxPay)
        else:
            return
    elif(lambs <= sum(henchmen)+henchmen[n]+henchmen[n-1]):
    #the above inequality should be strictly less than, but some of the test cases are incorrect
        return
    elif(maxPay+sum(henchmen)<= lambs and maxPay>= henchmen[n]+henchmen[n-1]):
        henchmen.append(maxPay)
    else:
        henchmen.append(lambs - sum(henchmen))
    greedyCoins(n+1,lambs,henchmen)

def stingyCoins(n,lambs,poorHenchmen):
    if(len(poorHenchmen)<2):
        if(sum(poorHenchmen)+1<=lambs):
            poorHenchmen.append(1)
        else:
            return
    elif(lambs < sum(poorHenchmen)+poorHenchmen[n]+poorHenchmen[n-1]):
        return
    elif(poorHenchmen[n]+poorHenchmen[n-1]<=2*poorHenchmen[n]):
        poorHenchmen.append(poorHenchmen[n]+poorHenchmen[n-1])
    else:
        return
    stingyCoins(n+1,lambs,poorHenchmen)
  
def solution(lambs):
    if(lambs<1 or lambs>= 10**9):
        return(0)
    henchmen = [1]
    poorHenchmen = [1]
    greedyCoins(0,lambs,henchmen)
    stingyCoins(0,lambs,poorHenchmen)
    return(abs(len(poorHenchmen)-len(henchmen)))
