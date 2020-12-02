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
        pos1 = read[0]-1
        pos2 = read[1]-1
        if(read[4][pos1] != read[4][pos2] and (read[4][pos1] == read[2] or read[4][pos2] == read[2])):
            validpasswd += 1
    except EOFError:
        print(validpasswd)
        break
