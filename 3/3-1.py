#!/usr/bin/python3.6

f = open("input.txt")
bluewire = f.readline().split(",")
bluewire = [i.strip() for i in bluewire]

redwire = f.readline().split(",")
redwire = [i.strip() for i in redwire]
f.close()

xCoordinate = 0
yCoordinate = 0
bluePath = []

for line in bluewire:
    distance = int(line[1:])
    if line[0] == "L":
        while distance > 0:
            xCoordinate -= 1
            bluePath.append([xCoordinate,yCoordinate])
            distance -= 1
    if line[0] == "R":
        while distance > 0:
            xCoordinate += 1
            bluePath.append([xCoordinate,yCoordinate])
            distance -= 1
    if line[0] == "U":
        while distance > 0:
            yCoordinate += 1
            bluePath.append([xCoordinate,yCoordinate])
            distance -= 1
    if line[0] == "D":
        while distance > 0:
            yCoordinate -= 1
            bluePath.append([xCoordinate,yCoordinate])
            distance -= 1

xCoordinate = 0
yCoordinate = 0
redPath = []

for line in redwire:
    distance = int(line[1:])
    if line[0] == "L":
        while distance > 0:
            xCoordinate -= 1
            redPath.append([xCoordinate,yCoordinate])
            distance -= 1
    if line[0] == "R":
        while distance > 0:
            xCoordinate += 1
            redPath.append([xCoordinate,yCoordinate])
            distance -= 1
    if line[0] == "U":
        while distance > 0:
            yCoordinate += 1
            redPath.append([xCoordinate,yCoordinate])
            distance -= 1
    if line[0] == "D":
        while distance > 0:
            yCoordinate -= 1
            redPath.append([xCoordinate,yCoordinate])
            distance -= 1

intersections = list(map(list, set(map(tuple, bluePath)) & set(map(tuple, redPath))))
closestIntersectionDistance = 0
for point in intersections:
    if point == intersections[0]:
        closestIntersectionDistance = (abs(point[0]) + abs(point[1]))
    if (abs(point[0]) + abs(point[1])) < closestIntersectionDistance:
        closestIntersectionDistance = (abs(point[0]) + abs(point[1]))

print(f"The closest intersection distance is {closestIntersectionDistance}")