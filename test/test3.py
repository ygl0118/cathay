input = 100

tmp = list()
for i in range(input):
    tmp.append(i+1)
while len(tmp) > 1:
    tmp.append(tmp.pop(0))
    tmp.append(tmp.pop(0))
    tmp.pop(0)
if input == 0:
    print(0)
else:
    print(tmp.pop())