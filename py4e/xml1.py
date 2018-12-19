import xml.etree.ElementTree as ET
data = '''
<person>
    <name>Chuck</name>
    <phone type="intl">
    +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)#从字符串得到一个树表
print('Name:',tree.find('name').text)#find找到标签节点，text获取节点的文本值
print('Attr:',tree.find('email').get('hide'))#find找到email节点，获取hide标签的值
