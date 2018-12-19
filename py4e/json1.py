
import json
data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)#load 函数将字符串转换为json文本，并返回python字典
print(len(info))
print('Name:',info['name'])
print('Hide:',info["email"]["hide"])
print('Phnum:',info["phone"]["number"])
