
MIN = 0
START = 50
MAX = 99

math = START

# Get Data
with open("input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]


# Create a list of tuples of the data
results = []

for i in data:
    direction = str(i[0])
    distance = int(i[1:])
    results.append((direction, distance))


# Set fresh counters
zerolcount = 0
linesmathed = 0
zerocross = 0


for direction, distance in results:
    print("------------------------------")
    print(f"Math Before -- {math}")
    print(f"Math Todo: {direction}, {distance}")
    # Handle if direction is greater than 100
    if distance >= 100:
        highclicks = distance // 100
        zerolcount += highclicks

        distance = distance % 100

    # Handle Addition
    if direction == "R":
        math += distance
        if math > 100:
            zerocross += 1 # Crossed 100 for zerocross
        elif math == 100:
            zerolcount += 1 # Landed back at 0 for zerolcount
    
    # Handle Subtraction
    elif direction == "L":
        math -= distance
        if math < 0:
            zerocross += 1 # Crossed 0 for zerocross
        elif math == 0:
            zerolcount += 1 # Landed back at 0 for zerolcount
        

    print(f"Math After -- {math}")
    linesmathed += 1

    # Keep between 0-99
    math = math % 100

    print(f"Math After Mod {math}")
    print(math, direction)







print("------------------------------")
print("------------------------------")
print("------------------------------")
#print(len(results))
print(f"Total Lines = {len(results)}")
print(f"Total Lines Mathed = {linesmathed}")
print("")
print(f"Zero Crosses = {zerocross}")
print(f"Zero Counts = {zerolcount}")
print("")
print(f"Total Zeros + Zero Crosses = {zerolcount + zerocross}")



