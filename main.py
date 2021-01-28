#!/usr/bin/python

import markdown

import xml.etree.ElementTree as ET

tree = ET.parse('overcast.opml')
root = tree.getroot()

def fromXMLtoMD():
    #for elem in root:
    #    print("tag: ", elem.tag)
    #    print("attrib: ", elem.attrib)
    #
    #    for subelem in elem:
    #        print("tag: ", subelem.tag)
    #        print("attrib: ", subelem.attrib)

    parsedXMLFile = open('overcast.md', 'w+')

    parsedXMLFile.write("# Podcasts from Overcast\n\n")

    for elem in root:            
        for subelem in elem.findall('outline'):
            for pod in subelem: 

                #print("Name: ", pod.get('text'))
                parsedXMLFile.write('[')
                parsedXMLFile.write(pod.get('text'))
                parsedXMLFile.write(']')
                #print("URL: " , pod.get('htmlUrl'))
                parsedXMLFile.write('(')
                parsedXMLFile.write(pod.get('htmlUrl'))
                parsedXMLFile.write(")\n")

                parsedXMLFile.write("\n")

def toMD():
    with open("overcast.md", "r", encoding="utf-8") as input_file:
        text = input_file.read()
    html = markdown.markdown(text)
    
    #print(html)

    with open("overcast.html", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
        output_file.write(html)


def main():
    fromXMLtoMD()
    toMD()

main()
