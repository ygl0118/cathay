input = [35, 46, 57, 91, 29]
output = []

for i in range(len(input)):
    tmp = input[i]
    if tmp < 10:
        output.insert(len(output), tmp)
    elif tmp < 100:
        ten = tmp % 10
        one = tmp / 10
        tmp = ten * 10 + int(one)
        output.insert(len(output), tmp)
    else:
        output.insert(len(output), tmp)

print(output)
