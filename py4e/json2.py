import json

input = '''[
    {"id" : "001",
     "x" : "2",
     "name" : "Chuck"
     },
    {"id" : "009",
     "x" : "7",
     "name" : "Chuck"
     }
]'''

info = json.loads(input)#这里得到的返回值是list，元素是字典
print('User count:',len(info))
for item in info:
    print('Name:',item['name'])
    print('Id:',item['id'])
    print('Attribute:',item['x'])
