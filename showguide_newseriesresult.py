#!/Python34/python
import cgi

import mongodbConnector
from show import Show

print("Content-type: text/html; charset=utf8")
print()

form = cgi.FieldStorage()
show = Show()
show.name = form.getvalue("new_series")
show.description = form.getvalue("description")
showId = mongodbConnector.addNewShow(show)

print("New Series: " + show.name + " with ID '" + str(showId))
print()
print("<p>")
print("<a href='index.html'>Main Page</a><br>")
print("<a href='showguide_insert.py'>Insert Formular</a><br>")
print("<a href='showguide_addseries.py'>Add Series Formular</a><br>")
print("</p>")
