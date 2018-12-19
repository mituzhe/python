import re
'''
hand = open('d:/test.txt')
for line in hand:
    line = line.rstrip()
    if re.search('my',line):
        print(line)
'''
'''
x = 'My 2 favorite numbers are 19 and 42 eeeaioou aajee'
y = re.findall('[0-9]+',x)
print(y)
y = re.findall('[aeiou]+',x)
print(y)
'''
x = 'From stephen.marquard@uct.ac.za Sat Jan    5  09:14:16  2008'
y = re.findall('^From .*@([^ ]*)',x)
print(y)
