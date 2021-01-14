import xml.etree.ElementTree as ET
import re
# root = ET.parse("/home/devasc/labs/devnet-src/parsing/AAC2.xml").getroot()

class SearchXML:
    def __init__(self, file):
        self.root = ET.parse(file).getroot()

    def _reqursion_search(self, main_tag):
        for child in main_tag:
            resp = child.find(self.tag_name)
            if resp is None  :
                #if not found tag_name -> search in child of current child tag
                if self._reqursion_search(child):
                    #if found return true, otherwise continue
                    return True
                else: continue
            #if found -> print value and return true
            print(f"Value for tag '{self.tag_name}' is {resp.text}")
            self.found = resp.text
            return True
        #return false if no children in main_tag
        return False

    def search(self,tag_name):
        self.tag_name = tag_name
        if not self._reqursion_search(self.root):
            print(f"Not found tag: '{tag_name}'")

    def get(self,tag_name):
        self.found = None
        self.tag_name = tag_name
        self._reqursion_search(self.root)
        return self.found    

if __name__ == "__main__":
    searchXML = SearchXML("F:\python\labs\AAC2.xml")
    searchXML.search('stopSourceIpAddress')
    searchXML.search('stopSourceIpAddress_1')
    
    print(SearchXML("F:\python\labs\AAC2.xml").get('stopSourceIpAddress'))
    print(SearchXML("F:\python\labs\AAC2.xml").get('stopSourceIpAddress_1'))
    # search('stopSourceIpAddress_1',root)
    # search('stopSourceIpAddress',root)