#!/usr/bin/env python
import cgi
form = cgi.FieldStorage()
print('Content-type: text/html\n')
print('<title>Reply Page</title>')
if not 'user' in form:
    print('<h1>Who are you?</h>')
else:
    print('<h1>Hello <i>%s</i>!</h>' % cgi.escape(form['user'].value))