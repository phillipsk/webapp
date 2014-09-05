import flask, flask.views
import os
import functools
import requests
import json

def compare_number_strings(string1, string2):
    
    return cmp(int(string1), int(string2))

search = raw_input("What are you searcing for? \n")

def user_bible(query):
    output = requests.get("http://getbible.net/json?passage={0}".format(query))
    json_dict_output = json.loads(output.text.strip("();"))

    before_for_loop_parse = json_dict_output[u'book'][0][u'chapter'] #[u'2'][u'verse']

    keys = before_for_loop_parse.keys()
    keys.sort(compare_number_strings)
    #print keys
    stored_list = []

    for k in keys:
        stored_list.append(before_for_loop_parse[k][u'verse'])

    print json_dict_output

user_bible(search)