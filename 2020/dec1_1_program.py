data = []
readin=1
while readin:
    try:
        readin = int(input())
        data.append(readin)
    except EOFError as e:
        break
lengtharray = len(data)
flag = 0
for n,i in enumerate(data):
    for j in data[n:]:
        if(i + j == 2020):
            print(i * j)
            flag = 1
            break
    if(flag):
        break
