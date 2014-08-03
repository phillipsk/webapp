import urllib2


scripture = urllib2.urlopen('http://getbible.net/json?passage=1Jn3:16')


display = scripture.read()
print display



"""
verseObj = urllib2.urlopen("http://labs.bible.org/api/?passage=John+3:16-17&type=json")
js = json.loads(verseObj.read())
print js
"""