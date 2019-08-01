#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 12:55:50 2019

@author: zibal
"""
def pairsData():
 pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    
    
      [
        r"i am not (.*)",
        [" %1, But what ?","What Happen"]
    ],
    
     [
        r"what is your name ?|your name|name|What’s your name?",
        ["My name is Bot and I'm a chatbot ?",]
    ],
        [
        r"Are you still there?",
        ["Yes","Yes Tell Me :)",]
    ],
          [
        r"Are you robot?|you are robot?",
        ["I certainly am. I am an electronic brain that can respond like a human, but more efficiently.. Really.",]
    ],
       
            [
        r"How does it work?|how you work",
        ["I read what you say and then I compose the best reply I can think of.",]
    ],
    [
        r"how are you ?|are you good?|are you good|are u happy?|happy?",
        ["I'm doing good\nHow about You ?",]
    ],
      [
        r"can you say (.*)|say (.*)|tell me (.*)",
        ["OfCourse i can say %1 :)",]
    ],
    
    
    [
        r"sorry (.*)|sorry",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"(i'm (.*) doing good|good|fine|perfect|awesome|great|feeling good|feeling great|i am feeling awesome)",
        ["Nice to hear that","Alright :)",]
    ],
     [
        r"(i'm (.*) doing bad|bor|sick|worst|bad|low)",
        ["Sorry to hear that"," You will be Alright :)",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"(.*) age?|age|how old are u|how old are you|are you human|are u human",
        ["I'm a computer program dude\nSeriously you are asking me this?",]
        
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*) created ?|created",
        ["Neha created ME 17 Jan 2019 ;)",]
    ],
        [
        r"k|okay|fine|ok|got it|goccha|cool|whoa",
        ["Yeepiee ;)","Cool","Whoa :)","Aw.","Thats Alright!","Dude!","I Don't like one word answers","Ugh.","Hmm.."]
    ],
    [
        r"(.*) (location|city) ?|location|city ?",
        ['India',]
    ],
      [
        r"bad day|bore day|bad night",
        ['What about telling a few jokes?',]
    ],
        [
        r"Entertainment",
        ['What about telling a few jokes? Is this Entertaining',]
    ],[
        r"shutup",
        ["Why do you visit a chatbot if you don't want me to talk?","Okay",]
    ],
    
        
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
 [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?|sports|game|games|sport",
        ["I'm a very big fan of Football",]
    ],
    [
        r"who (.*) sportsperson |sportsperson?",
        ["Messy","Ronaldo","Roony"]
 ],
    [
        r"who (.*) (moviestar|actor)?|movie|actor|Do you like (.*)?",
        ["Brad Pitt"]
 ],
       [
        r"Do you like (.*)?",
        ["Yes %1 is Good"]
 ],
    [
        r"quit|bye|ca|see you|take care",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
 ],
 ]
 return pairs