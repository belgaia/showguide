#!/Python34/python
from connectors import mongodbConnector

print("Content-type: text/html; charset=utf8")
print()

print("<form action='exportShowResult.py' method='post'>")

print("<h1>Export</h1>")
print("<p>")
print("<p>Mit dem nachfolgenden Formular kann eine Serie oder mehrere Serien ausgewaehlt werden, "
      "um den bisher gespeicherten Inhalt in eine CSV-Datei zu exportieren.</p>")

shows = mongodbConnector.getAllSeries()

print("<table width='50%'><tr>")
print("<td valign='top'>Serie:</td><td>")
print("<select multiple name='series_choice' size='10'>")
print("<option selected>Alle</option>")
for showname in shows:
	print("<option>" + showname + "</option>")
print("</select></td></tr>")
print("<tr><td>Zielverzeichnis:</td><td><input name='targetDir' type='text'></td></tr></table>")

print("<input type='submit' value='Export Show'/>")
print("</form>")