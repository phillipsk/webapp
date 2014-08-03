import urllib2
import json
scripture = urllib2.urlopen('http://getbible.net/json?passage=1Jn3:16')
display = scripture.read()
print display