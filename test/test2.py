input = "Hello welcome to Cathay 60th year anniversary"

input = input.upper()
tmp = dict()
for char in input:
    if tmp.get(char) != None:
        tmp[char] = tmp[char] + 1
    else:
        tmp[char] = 1

tmp.pop(' ')
sortedDict = dict( sorted(tmp.items(), key = lambda x: x[0].lower()) )

for item in sortedDict:
    print(item + " " + str(sortedDict[item]))