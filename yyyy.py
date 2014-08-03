#!/usr/bin/python -tt
# -*- coding: utf-8 -*-  
  
  
x = u'({"book":[{"book_name":"1 John","book_nr":"62","chapter_nr":"3","chapter":{"16":{"verse_nr":"16","verse":"Hereby perceive we the love of God, because he laid down his life for us: and we ought to lay down our lives for the brethren."},"17":{"verse_nr":17,"verse":"But whoso hath this world\'s good, and seeth his brother have need, and shutteth up his bowels of compassion from him, how dwelleth the love of God in him?"}}}],"direction":"LTR","type":"verse"});'

# save to variable

split_text = x.split('"verse_nr":"16","verse":')

verses = split_text[1].split("},")

first_verse = verses[0]  # << first verse in the search

#to omit first verse comment out this following line
#print first_verse

second_verse = verses[1]
"""
Work on the remaining text (second_verse)
second verse looks like this:
>>> while stepping through the algorithm it will look like this

"17":{"verse_nr":17,"verse":"But whoso hath this world\'s good, and seeth his brother have need, and shutteth up his bowels of compassion from him, how dwelleth the love of God in him?"}}}],"direction":"LTR","type":"verse"});'

"""

split_second = second_verse.split('"verse_nr":17,"verse":')

print split_second[1].split('}}}],"direction":"LTR","type":"verse"});')[0]