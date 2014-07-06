#!/Python34/python
import mongodbConnector
import cgi

print("Content-type: text/html")
print()

print("<form action='showguide_newseriesresult.py' method='post'>")
print("Add new series: <input name='new_series' type='text'>")
print("<input type='submit' value='Add Series'/>")
