import urllib2
import json
"""
url = urllib2.urlopen('http://labs.bible.org/api/?passage=John+3:16-17')
verse = url.read()
#print verse

"""
#verseObj = urllib2.urlopen("http://labs.bible.org/api/?passage=John+3:16-17&type=json")
#verseObj.read()
#print verseObj

verseObj = urllib2.urlopen("http://labs.bible.org/api/?passage=John+3:16-17&type=json")
js = json.loads(verseObj.read())
print js

print "-"*66



"""
json.loads(verseObj.read())

def get_passage_parameters(passage_string):
	return urllib.urlencode([("passage", passage_string)])

get_passage_parameters("John 3:16")

#'passage=John+3%3A16'
def get_passage_parameters("Mark 3:16")


def get_bible_verse(passage):
	argument = get_passage_parameters(passage)
	verseObj = urllib2.urlopen("http://labs.bible.org/api/?" + argument + "&type=json"
	return json.loads(verseObj.read())

"""