#!/Python34/python
from connectors import mongodbConnector

print("Content-type: text/html; charset=utf8")
print()

series = mongodbConnector.getAllSeries()

print("<h1>Show Guide Insert Form</h1>")
print("<h2>Informationen erfassen</h2>")
print("<h3>Allgemein</h3>")
print()

print("<a href='showguide_addseries.py'>Add new Series</a>")

print("<form action='showguide_insertresult.py' method='post'>")
print("<p><table width=50% border=0><tr>")

print("<td>Serie:</td><td>")
print("<select name='series_choice' size='1'>")
for showname in series:
	print("<option>" + showname + "</option>")
print("</select>")
print("</td></tr>")

print("<td>Staffel:</td><td><input name='season' type='text'></td></tr>")
print("<td>Folgennummer:</td><td><input name='episodenumber' type='text'></td></tr>")
print("<td>Gesamtfolgennummer:</td><td><input name='generalepisodenumber' type='text'></td></tr>")
print("<td>DVD Nummer:</td><td><input name='dvdnumber' type='text'></td></tr>")
print("<td>DVD Folgennummer:</td><td><input name='dvdepisodenumber' type='text'></td></tr>")
print("<td>Folgenname (Deutsch):</td><td><input name='episodename_de' type='text'></td></tr>")
print("<td>Folgenname (Englisch):</td><td><input name='episodename_en' type='text'></td></tr>")
print("<td>Darsteller:</td><td><input name='actors' type='text'></td></tr>")
print("<td valign='top'>Inhalt:</td><td><textarea name='content' cols='50' rows='10'></textarea></td></tr>")
print("<td>Regie:</td><td><input name='director' type='text'></td></tr>")
print("</table>")
print("<input type='submit' value='Add Information'/>")
print("</form>")
print("</p>")

print("<h3>H&C</h3>")
print("<p>")
print("Darsteller:<br>")
print("Wertung:<br>")
print("Beschreibung:<br>")
print("Weitere hinzufuegen")
print("</p>")