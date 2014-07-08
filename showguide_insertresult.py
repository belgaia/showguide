#!/Python34/python
import cgi
import mongodbConnector
from series import Series

print("Content-type: text/html; charset=utf8")
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
print("<p><table width=50% border=0><tr>")
print("<td>Serie:</td><td>" + entry.name + "</td></tr>")
print("<td>Staffel:</td><td>" + entry.season + "</td></tr>")
print("<td>Folgennummer:</td><td>" + entry.episodenumber + "</td></tr>")
print("<td>Gesamtfolgennummer:</td><td>" + entry.generalepisodenumber + "</td></tr>")
print("<td>DVD Nummer:</td><td>" + entry.dvdnumber + "</td></tr>")
print("<td>DVD Folgennummer:</td><td>" + entry.dvdepisodenumber + "</td></tr>")
print("<td>Folgenname (Deutsch):</td><td>" + entry.episodename_de + "</td></tr>")
print("<td>Folgenname (Englisch):</td><td>" + entry.episodename_en + "</td></tr>")
print("<td>Darsteller:</td><td>" + entry.actors + "</td></tr>")
print("<td>Inhalt:</td><td>" + entry.content.encode(encoding='utf8') + "</td></tr>")
print("<td>Regie:</td><td>" + entry.director + "</td></tr>")
print("</table>")
print("</p>")


print("<p>")
print("<a href='/showguide/showguide_insert.py'>Insert Formular</a><br>")
print("<a href='/showguide/showguide_addseries.py'>Add Series Formular</a><br>")
print("</p>")
