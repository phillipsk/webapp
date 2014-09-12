import pprint
import flask, flask.views
import os
import functools
import requests
import json

def parse_rough_draft(json_dict_output):
    books = json_dict_output[u'book']
    result_dict={}
    for i in books:
        book_name_variable = i[u'book_name']
        current_book_value = result_dict.setdefault(book_name_variable, {})
        chapter_variable = i[u'chapter_nr']
        chapter_value = current_book_value.setdefault(chapter_variable, {})
        all_chapter_verses_variable = i[u'chapter']
        for m in all_chapter_verses_variable.keys():
            verse = all_chapter_verses_variable[m]
            chapter_value[m] = verse[u'verse']
    print result_dict







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

    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(json_dict_output)

    parse_rough_draft(json_dict_output)

user_bible(search)

