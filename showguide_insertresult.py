#!/Python34/python
import cgi
import mongodbConnector
from series import Series

print("Content-type: text/html")
print()

form = cgi.FieldStorage()

# create series object with the values from html form
entry = Series()
entry.name = form.getvalue("series_choice")
entry.season = form.getvalue("season")
entry.episodenumber = form.getvalue("episodenumber")
entry.generalepisodenumber = form.getvalue("generalepisodenumber")
entry.dvdnumber = form.getvalue("dvdnumber")
entry.dvdepisodenumber = form.getvalue("dvdepisodenumber")
entry.episodename_de = form.getvalue("episodename_de")
entry.episodename_en = form.getvalue("episodename_en")
entry.actors = form.getvalue("actors")
entry.content = form.getvalue("content")
entry.director = form.getvalue("director")

mongodbConnector.createInfo(entry)

print()
print("<p>")
print("<a href='/showguide/showguide_insert.py'>Insert Formular</a><br>")
print("<a href='/showguide/showguide_addseries.py'>Add Series Formular</a><br>")
print("</p>")
