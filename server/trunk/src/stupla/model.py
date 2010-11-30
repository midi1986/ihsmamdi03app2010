class Option:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value      
        
    def asXML(self):
        xml  = "  <option>\n"
        xml += "    <key>" + self.key + "</key>\n"
        xml += "    <value>" + self.value + "</value>\n"
        xml += "  </option>\n"
        return xml           

class Options:
    
    def __init__(self, options):
        self.options = options
        
    def asXML(self):
        xml  = "<options>\n"
        for o in self.options:
            xml += o.asXML()
        xml  += "</options>\n"
        return xml     
    
class Stupla:
    def __init__(self, tage):
        self.tage = tage
    
    def asXML(self):
        xml  = "<stupla>\n"
        for t in self.tage:
            xml += t.asXML()
        xml  += "</stupla>\n"
        return xml  
    
class Tag:
    def __init__(self, name, stunden):
        self.name = name
        self.stunden = stunden
          
    def asXML(self):
        xml  = '  <tag name="' + self.name + '">' + "\n"
        for s in self.stunden:
            xml += s.asXML()
        xml += "  </tag>\n"
        return xml      
    
class Stunde:
    def __init__(self, name, vorlesungen):
        self.name = name
        self.vorlesungen = vorlesungen   
        
    def asXML(self):
        xml  = '    <stunde name="' + str(self.name) + '">' + "\n"
        for v in self.vorlesungen:
            xml += v.asXML()
        xml += "    </stunde>\n"
        return xml        
    
    
class Vorlesung:
    def __init__(self, name, kuerzel, raum, raumKuerzel, dozent, dozentKuerzel): 
        self.name = name
        self.kuerzel = kuerzel
        self.raum = raum
        self.raumKuerzel = raumKuerzel
        self.dozent = dozent
        self.dozentKuerzel = dozentKuerzel
        
    def tag(self, name, value):
        return "        <" + name + ">" + value + "</" + name + ">\n"
        
    def asXML(self):
        xml  = "      <vorlesung>\n"
        xml += self.tag("name", self.name)
        xml += self.tag("kuerzel", self.kuerzel)
        xml += self.tag("raum", self.raum)
        xml += self.tag("raumKuerzel", self.raumKuerzel)
        xml += self.tag("dozent", self.dozent)
        xml += self.tag("dozentKuerzel", self.dozentKuerzel)
        xml += "      </vorlesung>\n"
        return xml         

    