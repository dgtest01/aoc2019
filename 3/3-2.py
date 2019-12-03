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

intersectionDistances = []
for intersection in intersections:
    xCoordinate = 0
    yCoordinate = 0
    steps = 0
    for line in bluewire:
        distance = int(line[1:])
        if line[0] == "L":
            while distance > 0:
                xCoordinate -= 1
                distance -= 1
                steps += 1
                if [xCoordinate,yCoordinate] == intersection:
                    intersectionDistances.append([[xCoordinate,yCoordinate],steps])
        if line[0] == "R":
            while distance > 0:
                xCoordinate += 1
                distance -= 1
                steps += 1
                if [xCoordinate,yCoordinate] == intersection:
                    intersectionDistances.append([[xCoordinate,yCoordinate],steps])            
        if line[0] == "U":
            while distance > 0:
                yCoordinate += 1
                distance -= 1
                steps += 1
                if [xCoordinate,yCoordinate] == intersection:
                    intersectionDistances.append([[xCoordinate,yCoordinate],steps])
        if line[0] == "D":
            while distance > 0:
                yCoordinate -= 1
                distance -= 1
                steps += 1
                if [xCoordinate,yCoordinate] == intersection:
                    intersectionDistances.append([[xCoordinate,yCoordinate],steps])
    xCoordinate = 0
    yCoordinate = 0
    steps = 0
    for line in redwire:
        distance = int(line[1:])
        if line[0] == "L":
            while distance > 0:
                xCoordinate -= 1
                distance -= 1
                steps += 1
                if [xCoordinate,yCoordinate] == intersection:
                    for eachIntersection in intersectionDistances:
                        if eachIntersection[0] == [xCoordinate,yCoordinate]:
                            eachIntersection[1] += steps
        if line[0] == "R":
            while distance > 0:
                xCoordinate += 1
                distance -= 1
                steps += 1
                if [xCoordinate,yCoordinate] == intersection:
                    for eachIntersection in intersectionDistances:
                        if eachIntersection[0] == [xCoordinate,yCoordinate]:
                            eachIntersection[1] += steps         
        if line[0] == "U":
            while distance > 0:
                yCoordinate += 1
                distance -= 1
                steps += 1
                if [xCoordinate,yCoordinate] == intersection:
                    for eachIntersection in intersectionDistances:
                        if eachIntersection[0] == [xCoordinate,yCoordinate]:
                            eachIntersection[1] += steps
        if line[0] == "D":
            while distance > 0:
                yCoordinate -= 1
                distance -= 1
                steps += 1
                if [xCoordinate,yCoordinate] == intersection:
                    for eachIntersection in intersectionDistances:
                        if eachIntersection[0] == [xCoordinate,yCoordinate]:
                            eachIntersection[1] += steps

intersectionDistances.sort(key = lambda intersectionDistances: intersectionDistances[1]) 
print(f"The shortest signal distance intersection is {intersectionDistances[0]}")