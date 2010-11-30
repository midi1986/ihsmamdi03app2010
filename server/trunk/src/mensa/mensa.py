'''
Created on 26.11.2010

@author: joachim
'''
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


from parser import parseMensa 



print parseMensa(read()).asXML()
