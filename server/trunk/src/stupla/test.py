from __future__ import with_statement

from stupla.client import get_studiengaenge_from_server, get_query_from_server
from stupla.parser import parseStudiengaenge, parseSemester, parseVorlesungen, parseStupla

def write(data, type):   
    with open('../test/data/' + type + '.html', 'w') as f:
        f.write(data)

def read(type):
    with open('../test/data/' + type + '.html', 'r') as f:
        return f.read() 

#write(get_studiengaenge_from_server(), "studiengaenge")
#parseStudiengaenge(read("studiengaenge"))

#write(get_semester_from_server("stdg[]=IB&stdg[]=IM"), "semester")
#print parseSemester(read("semester"))

#write(get_query_from_server("sem[]=1IB&sem[]=1IM"), "vorlesungen")
#print parseVorlesungen(read("vorlesungen"))


#write(get_query_from_server("vorl[]=GDI+1IB&vorl[]=KRY+1IM"), "stupla")
print parseStupla(read("stupla"))
