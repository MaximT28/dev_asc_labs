import xml.etree.ElementTree as ET
import re
root = ET.parse("/home/devasc/labs/devnet-src/parsing/AAC2.xml").getroot()

def reqursion_search(tag_name, main_tag):
    for child in main_tag:
        resp = child.find(tag_name)
        if resp is None  :
            #if not found tag_name -> search in child of current child tag
            if reqursion_search(tag_name, child):
                #if found return true, otherwise continue
                return True
            else: continue
        #if found -> print value and return true
        print(f"Value for tag '{tag_name}' is {resp.text}")
        return True
    #return false if no children in main_tag
    return False

def search(tag_name, main_tag):
    if not reqursion_search(tag_name,main_tag):
        print(f"Not found tag: '{tag_name}'")

if __name__ == "__main__":
    search('stopSourceIpAddress_1',root)
    search('stopSourceIpAddress',root)

#shorter version:
"""
def reqursion_search(tag_name, main_tag):
    for child in main_tag:
        resp = child.find(tag_name)
        if resp is None  :
            reqursion_search(tag_name, child)
        else:
            print(f"Value for tag '{tag_name}' is {resp.text}")

if __name__ == "__main__":
    reqursion_search('stopSourceIpAddress_1',root)
    reqursion_search('stopSourceIpAddress',root)
"""
