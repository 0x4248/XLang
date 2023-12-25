# XLang
# XLang is a format for storing language strings in XML files.
# GitHub: https://www.github.com/lewisevans2007/XLang
# Licence: GNU General Public Licence v3.0
# By: Lewis Evans

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

