# form_test.py

import cgi

form = cgi.FieldStorage()
text =  form.getvalue('summarize')

print "You said " + text

