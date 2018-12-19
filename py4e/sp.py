import xml.etree.ElementTree as ET

fhand = open('d:/naturo.txt')
fstr = fhand.read()
#print(fstr)

tree = ET.fromstring(fstr)
lst = tree.findall('body/div')
print(len(lst))
