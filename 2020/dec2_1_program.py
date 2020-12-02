import re
read = 1
validpasswd = 0
while read:
    try:
        read = input()
        read = re.split('-|:| ',read)
        # read = ['1', '3', 'a', '', 'abcde']
        read[0] = int(read[0])
        read[1] = int(read[1])
        # read = [1, 3, 'a', '', 'abcde']
        lbound = read[0]
        ubound = read[1]
        count = 0
        for i in read[4]:
            if(i == read[2]):
                count += 1
        if(lbound <= count <= ubound):
            validpasswd += 1
    except EOFError:
        print(validpasswd)
        break
