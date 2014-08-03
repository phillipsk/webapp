#!/usr/bin/python -tt
# -*- coding: utf-8 -*-  



# working with API

import requests
import re  # regexes
# requests (pip install requests)

# option A (dictactorial)
#book = raw_input("Name of book")
#chapter = raw_input("Chapter")
#verse_range= raw_input("Verse range, e.g. 1 - 5, 16")

# option B
search = raw_input("What are you searcing for? \n")
scripture = requests.get("http://getbible.net/json?passage={0}".format(search))

#Jn3:16

# assignment
# parse "search"
# usecase of 2 verses
# use regexes to parse user input
# example of user input
# 
"""
Jn3:16 >>> pattern <alphabet character><digit>:<digit>
James  >>> <alphabet>
ps119  >>> <alphabet><digit>
3:17-4;2:1 >> <alpah>:<alpha> etc.
119:4-16;23:1-6&v=amp
Acts 15:1-5, 10, 15&version=aov
"""



# get text
x = scripture.text # method provided by requests
print x
