import flask, flask.views
import os
import functools
import requests
import json

def compare_number_strings(string1, string2):
    #print "Hello, world!"
    return cmp(int(string1), int(string2))


def user_bible(query):
    print query
    output = requests.get("http://getbible.net/json?passage={0}".format(query))
    json_dict_output = json.loads(output.text.strip("();"))

    before_for_loop_parse = json_dict_output[u'book'][0][u'chapter'] #[u'2'][u'verse']

    keys = before_for_loop_parse.keys()
    keys.sort(compare_number_strings)
    print keys
    stored_list = []

    for k in keys:
        stored_list.append(before_for_loop_parse[k][u'verse'])

    return stored_list


app = flask.Flask(__name__)
# Don't do this!
app.secret_key = "password"

users = {'admin':'password'}

class Main(flask.views.MethodView):
    def get(self):
        return flask.render_template('index.html')
    
    def post(self):
        if 'logout' in flask.request.form:
            flask.session.pop('username', None)
            return flask.redirect(flask.url_for('index'))
        required = ['username', 'passwd']
        for r in required:
            if r not in flask.request.form:
                flask.flash("Error: {0} is required.".format(r))
                return flask.redirect(flask.url_for('index'))
        username = flask.request.form['username']
        passwd = flask.request.form['passwd']
        if username in users and users[username] == passwd:
            flask.session['username'] = username
        else:
            flask.flash("Username doesn't exist or incorrect password")
        return flask.redirect(flask.url_for('index'))

def login_required(method):
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        if 'username' in flask.session:
            return method(*args, **kwargs)
        else:
            flask.flash("A login is required to see the page!")
            return flask.redirect(flask.url_for('index'))
    return wrapper

class Remote(flask.views.MethodView):
    @login_required
    def get(self):
        return flask.render_template('remote.html')
        
    @login_required
    def post(self):
        result = eval(flask.request.form['expression'])
        flask.flash(result)
        return flask.redirect(flask.url_for('remote'))

class Music(flask.views.MethodView):
    @login_required
    def get(self):
        songs = os.listdir('static/music')
        return flask.render_template("music.html", songs=songs)

class Bible(flask.views.MethodView):
    #@login_required
    def get(self):
        return flask.render_template('bible.html')
    def post(self):
        result = (flask.request.form['expression'])
        flask.flash("\n".join(user_bible(result)))
        return flask.redirect(flask.url_for('Bible'))

    
app.add_url_rule('/',
                 view_func=Main.as_view('index'),
                 methods=["GET", "POST"])
app.add_url_rule('/remote/',
                 view_func=Remote.as_view('remote'),
                 methods=['GET', 'POST'])
app.add_url_rule('/music/',
                 view_func=Music.as_view('music'),
                 methods=['GET'])
app.add_url_rule('/Bible/',
                 view_func=Bible.as_view('Bible'),
                 methods=['GET', 'POST'])

if __name__ == "__main__":
    app.debug = True
    app.run()
