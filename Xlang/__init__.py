import xml.etree.ElementTree as ET

class XLang:
    def __init__(self, filename):
        self.filename = filename
        self.tree = ET.parse(filename)
        self.root = self.tree.getroot()
    
    def get_meta(self):
        return self.root.find('meta')
    
    def get_string(self, name, lang):
        return self.root.find('strings').find('string[@name="'+name+'"]').find(lang).text

