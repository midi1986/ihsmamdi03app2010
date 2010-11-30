

ns = "{http://www.w3.org/1999/xhtml}"

from xml.etree.ElementTree import fromstring, dump
from string import strip
from model import Essen, MensaKategorie, MensaTag, MensaPlan

def trim(string):
    return strip(string).replace("\n", " ").replace("\t", "")

def essenMitSuppe(sorte, tds):
    h4 = tds[0].find(ns + "h4")
    return Essen(sorte, trim(h4.tail), trim(h4.text), tds[1].text)

def vegetarisch(tds):
    return essenMitSuppe("Vegetarisch", tds)

def menu1(tds):
    return essenMitSuppe("Menue 1", tds)

def menu2(tds):
    return essenMitSuppe("Menue 2", tds)

def dessert(tds):
    br = tds[1].find(ns + "br")
    return Essen("DESSERT", trim(tds[0].text), "", trim(br.tail))    

def essenOhneSuppe(sorte, tds):
    return Essen(sorte, trim(tds[0].text), "", trim(tds[1].text))

def aktionstheke(tds):
    return essenOhneSuppe("AKTIONSTHEKE", tds)

def wok(tds):
    return essenOhneSuppe("WOK", tds)

def parseMensa(xml):
    corrected = xml.replace("&nbsp;", " ").replace("&auml;", "&#228;")
    tree = fromstring(corrected)  
    divWoTab_hs = [x for x in tree.findall(
            ".//{http://www.w3.org/1999/xhtml}div") 
            if 'id' in x.attrib and x.attrib["id"] == 'WoTab_hs'][0]
    table = divWoTab_hs.find(ns + "table")
    trs = table.findall(ns + "tr")
    #printHeadLines(trs[0])
    
    tage = []
    for tr in trs[1:]:
        tds = tr.findall(ns + "td")
        tagesspez = MensaKategorie(
            "Tagesspezialitaeten", 
            [vegetarisch(tds[1:3]), 
             menu1(tds[3:5]), 
             menu2(tds[5:7])])
        spezial = MensaKategorie(
            "Spezialangebote",
            [dessert(tds[7:9]),
             aktionstheke(tds[9:11]),
             wok(tds[11:13])])
        tage.append(MensaTag(tds[0].find(ns + "h1").text, [tagesspez, spezial]))
    plan = MensaPlan(tage)
    return plan

                