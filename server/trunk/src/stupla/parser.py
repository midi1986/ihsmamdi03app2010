# -*- coding: utf-8 -*-

import re


def findOptions(optionsString):
    return re.findall("(<option[^>]*>[^<]*</option>)", optionsString)

def findTrs(trsString):
    return re.findall("(<tr[^>]*>.*?</tr>)", trsString, re.DOTALL)

def findTds(tdsString):
    return re.findall("(<td[^>]*>.*?</td>)", tdsString, re.DOTALL)

def parseOption(option):
    return re.match('<option[^>]*>([^<]*)</option>', option).group(1)

def parseTd(td):
    return re.match('<td[^>]*>(.*?)</td>', td, re.DOTALL).group(1)

def parseStudiengaenge(xml):
    corrected = unicode(xml, "ISO-8859-1")
    optionsString = re.search(
                        '<select.*name="stdg\[\]"[^>]*>(.*)</select>', 
                        corrected).group(1)
    options  = findOptions(optionsString)
    for option in options:
        match = re.match('<option.*value="([^"]*)"[^>]*>([^<]*)</option>', option)
        print match.group(1), match.group(2) 

def parseSemester(xml):
    corrected = unicode(xml, "ISO-8859-1")
    optionsString = re.search(
                    '<select.*name="sem\[\]"[^>]*>(.*)</select>', 
                    corrected).group(1)
    
    options  = findOptions(optionsString)
    for option in options:
        print parseOption(option)

def parseVorlesungen(xml):
    corrected = unicode(xml, "ISO-8859-1")
    optionsString = re.search(
                    '<select.*name="vorl\[\]"[^>]*>(.*)</select>', 
                    corrected).group(1)
    options  = findOptions(optionsString)
    for option in options:
        print parseOption(option)
        
def parseStupla(xml):
    corrected = unicode(xml, "ISO-8859-1")
    table = re.search(
            '<table bgcolor="#FFFFFF"[^>]*>(.*?)</table>',
            corrected, re.DOTALL).group(1)
    trs = findTrs(table)
    for tr in trs[1:7]:
        print "-------------------------------"
        tds = findTds(tr)
        for td in tds[1:]:
            print parseTd(td)
