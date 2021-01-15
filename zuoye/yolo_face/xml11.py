import xml.dom.minidom
dom = xml.dom.minidom.parse("C:\\Users\\Administrator\\Desktop\\yolo_face\\datasets\\face\\outputs\\01.xml")
print(dom)
root = dom.documentElement

print(root.getElementsByTagName('width')[0].firstChild.data)
print(root.getElementsByTagName('xmin')[0].firstChild.data)
objects = root.getElementsByTagName('object')
for obj in objects:
    name = root.getElementsByTagName('name')[0].firstChild.data
    xmin = root.getElementsByTagName('xmin')[0].firstChild.data
    ymin = root.getElementsByTagName('ymin')[0].firstChild.data
    xmax = root.getElementsByTagName('xmax')[0].firstChild.data
    ymax = root.getElementsByTagName('ymax')[0].firstChild.data
    print(name,xmin,ymin)