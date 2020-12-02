#Take a value, divide by 3, round down, and then subtract 2
import math
data = []
value = 1
while value:
    try:
        value = int(input())
        value = math.floor(value / 3) - 2
        data.append(value)
    except EOFError as e:
        break
print(sum(data))
