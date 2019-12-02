#!/usr/bin/python3.6

with open('input.txt') as f:
    lines = f.readlines()

fuelTotal = 0
for line in lines:
    currentModuleFuel = int(line)
    while currentModuleFuel > 0:
        currentModuleFuel = (currentModuleFuel // 3) - 2
        if currentModuleFuel > 0:
            fuelTotal += currentModuleFuel

print(f"The total amount of fuel required is {fuelTotal}.")
