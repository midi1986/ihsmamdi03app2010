# -*- coding: utf-8 -*-

import re
from stupla.model import *

def parseSelect(varName, string):
    return re.search('<select.*name="' + varName + '\[\]"[^>]*>(.*)</select>', 
                     string).group(1)

def findOptions(optionsString):
    return re.findall("(<option[^>]*>[^<]*</option>)", optionsString)

def findTrs(trsString):
    return re.findall("(<tr[^>]*>.*?</tr>)", trsString, re.DOTALL)

def findTds(tdsString):
    return re.findall("(<td[^>]*>.*?</td>)", tdsString, re.DOTALL)

def findNobr(optionsString):
    return re.findall("<nobr>(.*?)</nobr>", optionsString)

def parseOption(option):
    return re.match('<option[^>]*>([^<]*)</option>', option).group(1)

def parseTd(td):
    return re.match('<td[^>]*>(.*?)</td>', td, re.DOTALL).group(1)

def parseStudiengaenge(xml):
    corrected = unicode(xml, "ISO-8859-1")
    optionsString = parseSelect("stdg", corrected)
    optionsStrings = findOptions(optionsString)
    options = []
    for option in optionsStrings:
        match = re.match('<option.*value="([^"]*)"[^>]*>([^<]*)</option>', option)
        options.append(Option(match.group(1), match.group(2)))
    return Options(options)

def parseSemester(xml):
    corrected = unicode(xml, "ISO-8859-1")
    optionsString = parseSelect("sem", corrected)
    optionsStrings = findOptions(optionsString)
    options = []        
    for option in optionsStrings:
        value = parseOption(option)
        if not value.startswith("&"):
            options.append(Option(value, value))
    return Options(options)        

def parseVorlesungen(xml):
    corrected = unicode(xml, "ISO-8859-1")
    optionsString = parseSelect("vorl", corrected)
    optionsStrings  = findOptions(optionsString)
    options = []        
    for option in optionsStrings:
        value = parseOption(option)
        options.append(Option(value, value))
    return Options(options)       
        
def parseStunde(s):
    m = re.match('<span title="(.*)">(.*)</span><span title="(.*)">(.*)</span><span title="(.*)">(.*)</span>', s)
    return Vorlesung(m.group(1), m.group(2), m.group(3), m.group(4), m.group(5), m.group(6))

tagNamen = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"]
        
def parseStupla(xml):
    corrected = unicode(xml, "ISO-8859-1")
    table = re.search(
            '<table bgcolor="#FFFFFF"[^>]*>(.*?)</table>',
            corrected, re.DOTALL).group(1)
    trs = findTrs(table)
    stundenNr = 1
    tagStunden = []
    for i in range(5):
        tagStunden.append([])
    for tr in trs[1:7]:
        tds = findTds(tr)
        tagNr = 0
        for td in tds[1:]:
            nobrs = findNobr(parseTd(td))
            vorlesungen = []
            for nobr in nobrs:
                nobr = nobr.replace("&nbsp;", "")
                if len(nobr) > 0:
                    vorlesungen.append(parseStunde(nobr))
            tagStunden[tagNr].append(Stunde(stundenNr, vorlesungen))
            tagNr += 1
        stundenNr += 1
    tagNr = 0
    tage = []
    for stunden in tagStunden:
        tage.append(Tag(tagNamen[tagNr], stunden))
        tagNr += 1
    return Stupla(tage)
