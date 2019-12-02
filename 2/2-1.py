#!/usr/bin/python3.6
from numpy import loadtxt
values = loadtxt("input.txt", delimiter = ",", dtype = "int", unpack=False)

opcodeIndicator = 0
continueExecution = True
while continueExecution:
    if int(values[opcodeIndicator]) == 1:
        newValue = int(values[values[opcodeIndicator + 1]] + values[values[opcodeIndicator + 2]])
        newValuePosition = int(values[opcodeIndicator + 3])
        values[newValuePosition] = newValue
        opcodeIndicator += 4
    elif int(values[opcodeIndicator]) == 2:
        newValue = int(values[values[opcodeIndicator + 1]] * values[values[opcodeIndicator + 2]])
        newValuePosition = int(values[opcodeIndicator + 3])
        values[newValuePosition] = newValue
        opcodeIndicator += 4
    elif int(values[opcodeIndicator]) == 99:
        continueExecution = False
    else:
        print(f"Unknown Opcode: {values[opcodeIndicator]}")
        continueExecution = False
print(f"The final value at position 0 is: {values[0]}")

