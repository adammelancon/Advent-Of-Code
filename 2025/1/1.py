
MIN = 0
START = 50
MAX = 99

math = START


with open("input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]
#print(data)

results = []

for i in data:
    direction = str(i[0])
    distance = int(i[1:])
    results.append((direction, distance))
    #print(f"Direction = {direction}")
    #
    #print(f"Distance = {distance}")

# print(results)
# print("----------------")
print(len(results))

zerolcount = 0
linesmathed = 0

for direction, distance in results:
    if direction == "R":
        math += distance
        
        
    elif direction == "L":
        math -= distance
    
    linesmathed += 1
    math = math % 100

    print(math, direction)

    if math == 0:
        print(direction, math)
        zerolcount += 1


print(len(results))
print(linesmathed)
print(zerolcount)



