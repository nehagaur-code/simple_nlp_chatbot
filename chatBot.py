#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 11:48:42 2019

@author: neha
"""

from nltk.chat.util import Chat, reflections
#with open('DataSet.txt','r') as datafile:
#    pairs=datafile.read()
#    print(pairs)
import PairsData
pairs=PairsData.pairsData() 
#print(pairs)

def chatty():
        print("Hi, I'm Bot \n How can i Help You") #default message at the start
        chat = Chat(pairs)
        chat.converse()
       

        
if __name__ == "__main__":
    chatty()