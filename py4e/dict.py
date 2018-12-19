'''
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['thissues'] = 75
print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 2
print(purse)
'''
hand = open('d:/test.txt','r')

fhand = hand.read()
flist = fhand.split()
fdict = dict()
for word in flist:
    fdict[word] = fdict.get(word, 0) + 1
for lab,value in fdict.items():
    print(lab,'\t',value)

bigcount = None
bigword = None
for word,count in fdict.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, '\t', bigcount)
