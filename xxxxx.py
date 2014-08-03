#!/usr/bin/python -tt
# -*- coding: utf-8 -*-  
  
  
x = u'({"book":[{"book_name":"1 John","book_nr":"62","chapter_nr":"3","chapter":{"16":{"verse_nr":"16","verse":"Hereby perceive we the love of God, because he laid down his life for us: and we ought to lay down our lives for the brethren."},"17":{"verse_nr":17,"verse":"But whoso hath this world\'s good, and seeth his brother have need, and shutteth up his bowels of compassion from him, how dwelleth the love of God in him?"}}}],"direction":"LTR","type":"verse"});'

# save to variable

split_text = x.split('"verse_nr":"16","verse":')

# pick the second element
first_verse = split_text[1].split("},")[0]  # << first verse in the search
print first_verse  # clean

last_text_unsanitized = first_verse[1]