"""
import requests
# requests (pip install requests)
scripture = requests.get('http://getbible.net/json?passage=1Jn3:16')

# get text
return_value = scripture.text # method provided by requests

print scripture.text
"""

#!/usr/bin/python -tt
# -*- coding: utf-8 -*-  
  

x = u'({"book":[{"book_name":"1 John","book_nr":"62","chapter_nr":"3","chapter":{"16":{"verse_nr":"16","verse":"Hereby perceive we the love of God, because he laid down his life for us: and we ought to lay down our lives for the brethren."},"17":{"verse_nr":17,"verse":"But whoso hath this world\'s good, and seeth his brother have need, and shutteth up his bowels of compassion from him, how dwelleth the love of God in him?"}}}],"direction":"LTR","type":"verse"});'

# save to variable

#split = x.split('"verse_nr":"16"')[1]
split = x.split('"verse_nr":"16","verse":')
split2 = split.split("}")[0]
#print split
print split[1]+split2

print len(split)