from __future__ import with_statement

if __name__ == '__main__':
    pass

def write(data):   
    f = open('test/data/wo_hs.normal.php.html', 'w')
    f.write(data)
    f.close()

def read():
    with open('../test/data/wo_hs.normal.php.html', 'r') as f:
        return f.read() 


from mensa.parser import parseMensa 
from mensa.client import get_from_server

print parseMensa(get_from_server()).asXML()
