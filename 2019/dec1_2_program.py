#Take a value, divide by 3, round down, and then subtract 2
#Now we must calculate the fuel that is required by the additional fuel
import math
data = []
while 1:
    try:
        value = int(input())
        value = math.floor(value / 3) - 2
        while value > 0:
            data.append(value)
            value = math.floor(value / 3) - 2
    except EOFError as e:
        break
print(sum(data))
