class Essen(object):
    indent = "        "
    tag_indent = "      "


    def __init__(self, sorte, name, suppe, preis):
        self.sorte = sorte
        self.name = name
        self.suppe = suppe
        self.preis = preis
        
    def toString(self):
        return self.sorte + ": " + self.name + "; Suppe: " + self.suppe + "; Preis: " + self.preis

    def tag(self, name, value):
        return self.indent + "<" + name + ">" + value + "</" + name + ">\n"

    def asXML(self):
        xml  = self.tag_indent + "<essen>\n"
        xml += self.tag("sorte", self.sorte)
        xml += self.tag("name", self.name)
        xml += self.tag("suppe", self.suppe)
        xml += self.tag("preis", self.preis)
        xml += self.tag_indent + "</essen>\n"
        return xml
            
class MensaKategorie:
    tag_indent = "    "
    
    def __init__(self, name, essen):
        self.name = name
        self.essen = essen
        
    def asXML(self):
        xml  = self.tag_indent + '<mensaKategorie name="' + self.name + "\">\n"
        for e in self.essen:
            xml += e.asXML()
        xml  += self.tag_indent + "</mensaKategorie>\n"
        return xml

class MensaTag:
    tag_indent = "  "
    
    def __init__(self, name, kategorien):
        self.name = name
        self.kategorien = kategorien
        
    def asXML(self):
        xml  = self.tag_indent + '<mensaTag name="' + self.name + "\">\n"
        for k in self.kategorien:
            xml += k.asXML()
        xml  += self.tag_indent + "</mensaTag>\n"
        return xml
    
class MensaPlan:
    def __init__(self, tage):
        self.tage = tage     

    def asXML(self):
        xml  = "<mensaPlan>\n"
        for t in self.tage:
            xml += t.asXML()
        xml  += "</mensaTag>\n"
        return xml
        