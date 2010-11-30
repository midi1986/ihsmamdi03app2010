from mensa.client import get_from_server
from mensa.parser import parseMensa 

print "Content-Type: text/xml; charset=utf-8"
print ""
print parseMensa(get_from_server()).asXML().encode('utf-8')
