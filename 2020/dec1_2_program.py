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
    for m,j in enumerate(data[n:]):
        for k in data[m:]:
            if(i + j + k == 2020):
                print(i * j * k)
                flag = 1
                break
        if(flag): break
    if(flag): break
