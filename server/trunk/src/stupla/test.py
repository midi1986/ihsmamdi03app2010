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
print parseStudiengaenge(read("studiengaenge")).asXML()

#write(get_semester_from_server("stdg[]=IB&stdg[]=IM"), "semester")
#print parseSemester(read("semester"))

#write(get_query_from_server("sem[]=1IB&sem[]=1IM"), "vorlesungen")
#print parseVorlesungen(read("vorlesungen"))


#write(get_query_from_server("vorl%5B%5D=ADS+1IB&vorl%5B%5D=ADSL+1IB&vorl%5B%5D=AMR+1IM&vorl%5B%5D=BGL+1IB&vorl%5B%5D=COM+1IM&vorl%5B%5D=DIM+1IB&vorl%5B%5D=DIM%DC+1IB&vorl%5B%5D=EBK+1IM&vorl%5B%5D=GDI+1IB&vorl%5B%5D=GDIL+1IB&vorl%5B%5D=KDM+1IM&vorl%5B%5D=KRY+1IM&vorl%5B%5D=MA+1IB&vorl%5B%5D=NNW+1IM&vorl%5B%5D=PPR+1IM&vorl%5B%5D=TGI+1IB&vorl%5B%5D=TLM+1IM"), "stupla2")
#print parseStupla(read("stupla2"))
