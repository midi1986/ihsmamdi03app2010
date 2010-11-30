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
    