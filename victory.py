#!/usr/bin/python -tt
# -*- coding: utf-8 -*-  



# working with API

import requests
import re  # regexes
import json
# requests (pip install requests)

# option A (dictactorial)
#book = raw_input("Name of book")
#chapter = raw_input("Chapter")
#verse_range= raw_input("Verse range, e.g. 1 - 5, 16")

# option B
search = raw_input("What are you searcing for? \n")
scripture = requests.get("http://getbible.net/json?passage={0}".format(search))
print "http://getbible.net/json?passage={0}".format(search)
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
#x = [scripture.text] # method provided by requests
#print scripture.text
json_dict_output = json.loads(scripture.text.strip("();"))

before_for_loop_parse = json_dict_output[u'book'][0][u'chapter'] #[u'2'][u'verse']

keys = before_for_loop_parse.keys()
keys.sort()

stored_list = []

for k in keys:
	#before_for_loop_parse[k]
	#before_for_loop_parse[k][u'verse']
	stored_list.append(before_for_loop_parse[k][u'verse'])
	#print k

#print stored_list
#print string
for v in stored_list:
	print v
"""
def user_bible(query):
	output = requests.get("http://getbible.net/json?passage={0}".format(query))
	json_dict_output = json.loads(output.text.strip("();"))

	before_for_loop_parse = json_dict_output[u'book'][0][u'chapter'] #[u'2'][u'verse']

	keys = before_for_loop_parse.keys()
	keys.sort()

	stored_list = []

	for k in keys:
		stored_list.append(before_for_loop_parse[k][u'verse']

	return stored_list
"""
#x = u'({"book":[{"book_name":"1 John","book_nr":"62","chapter_nr":"3","chapter":{"16":{"verse_nr":"16","verse":"Hereby perceive we the love of God, because he laid down his life for us: and we ought to lay down our lives for the brethren."},"17":{"verse_nr":17,"verse":"But whoso hath this world\'s good, and seeth his brother have need, and shutteth up his bowels of compassion from him, how dwelleth the love of God in him?"}}}],"direction":"LTR","type":"verse"});'
#print x
#parsing the unicode
"""
split_text = x.split('"verse_nr":"16","verse":')
print split_text
verses = split_text[1].split("},")

first_verse = verses[0] 

second_verse = verses[1]

split_second = second_verse.split('"verse_nr":17,"verse":')

print split_second[1].split('}}}],"direction":"LTR","type":"verse"});')[0]

#print x
"""