#!/Python34/python
import cgi

import mongodbConnector


print("Content-type: text/html; charset=utf8")
print()

form = cgi.FieldStorage()
newSeries = form.getvalue("new_series")
description = form.getvalue("description")
mongodbConnector.addNewSeries(newSeries, description)

print("New Series: " + newSeries)
print()
print("<p>")
print("<a href='index.html'>Main Page</a><br>")
print("<a href='showguide_insert.py'>Insert Formular</a><br>")
print("<a href='showguide_addseries.py'>Add Series Formular</a><br>")
print("</p>")
