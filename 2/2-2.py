#!/usr/bin/python3.6
from numpy import loadtxt

def executeInstruction(noun,verb):
    memoryValues = loadtxt("input.txt", delimiter = ",", dtype = "int", unpack=False)
    instructionPointer = 0
    memoryValues[instructionPointer + 1] = noun
    memoryValues[instructionPointer + 2] = verb

    continueExecution = True
    while continueExecution:
        if int(memoryValues[instructionPointer]) == 1:
            newValue = int(memoryValues[memoryValues[instructionPointer + 1]] + memoryValues[memoryValues[instructionPointer + 2]])
            newValuePosition = int(memoryValues[instructionPointer + 3])
            memoryValues[newValuePosition] = newValue
            instructionPointer += 4
        elif int(memoryValues[instructionPointer]) == 2:
            newValue = int(memoryValues[memoryValues[instructionPointer + 1]] * memoryValues[memoryValues[instructionPointer + 2]])
            newValuePosition = int(memoryValues[instructionPointer + 3])
            memoryValues[newValuePosition] = newValue
            instructionPointer += 4
        elif int(memoryValues[instructionPointer]) == 99:
            continueExecution = False
            return(memoryValues[0])
        else:
            print(f"Unknown Opcode: {memoryValues[instructionPointer]}")
            continueExecution = False

output = -1
targetOutput = 19690720
noun = 1
verb = 1
while output != targetOutput:
    while noun < 100:
        while verb < 100:
            output = executeInstruction(noun,verb)
            if output == targetOutput:
                break
            else:
                verb += 1
        if output == targetOutput:
            break
        else:
            noun += 1
            verb = 1
    if output == targetOutput:
        break

print(f"The correct noun is {noun} and correct verb is {verb}")
print(f"The answer is {(noun * 100) + verb}")