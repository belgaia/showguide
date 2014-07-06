#!/Python34/python
import cgi
import mongodbConnector

print("Content-type: text/html")
print()

form = cgi.FieldStorage()
newSeries = form.getvalue("new_series")
mongodbConnector.addNewSeries(newSeries)

print("New Series: " + newSeries)
print()
print("<p>")
print("<a href='/showguide/showguide_insert.py'>Insert Formular</a><br>")
print("<a href='/showguide/showguide_addseries.py'>Add Series Formular</a><br>")
print("</p>")
