#!/Python34/python
import mongodbConnector

print("Content-type: text/html; charset=utf8")
print()
print("<h1>Show Guide Overview</h1>")
print("<h2>Informationen anzeigen</h2>")
print("<h3>Allgemein</h3>")
print()
print("<form action='showguide_showresult.py' method='post'>")
print("<p><table width=50% border=0><tr>")
series = mongodbConnector.getAllSeries()
print("<td>Serie:</td><td>")
print("<select name='series_choice' size='1'>")
for showname in series:
	print("<option>" + showname + "</option>")
print("</select>")
print("</td></tr>")
print("</table>")
print("<input type='submit' value='Show Series Infos'>")
print("</p>")