#!/Python34/python

print("Content-type: text/html; charset=utf8")
print()

print("<form action='showguide_newseriesresult.py' method='post'>")

print("<h1>Add new series</h1>")
print("<table width='50%'>")
print("<tr><td>Name:</td><td><input name='new_series' type='text'></td></tr>")
print("<tr><td>Beschreibung:</td><td><input name='description' type='text'></td></tr>")
print("</table>")

print("<input type='submit' value='Add Series'/>")
print("</form>")
