#!/Python34/python
__author__ = 'Agile Developers'
import mongodbConnector

print("Content-type: text/html; charset=utf8")
print()

print("<form action='exportShowResult.py' method='post'>")

print("<h1>Export</h1>")
print("<p>")
print("<p>Mit dem nachfolgenden Formular kann eine Serie ausgewaehlt werden, um diese in eine CSV-Datei zu exportieren.</p>")

shows = mongodbConnector.getAllSeries()

print("<table width='50%'><tr>")
print("<td>Serie:")
print("<select name='series_choice' size='1'>")
for showname in shows:
	print("<option>" + showname + "</option>")
print("</select></td></tr>")
print("<tr><td>Zielverzeichnis: <input name='targetDir' type='text'></td></tr></table>")

print("<input type='submit' value='Export Show'/>")
print("</form>")