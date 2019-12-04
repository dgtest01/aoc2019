#!/usr/bin/python3.6

password = 356261
passwordMax = 846303
viablePasswords = 0

while password < passwordMax:
    characterIndex = 0
    doubleAdjacentDigits = False
    while characterIndex < 5:
        if str(password)[characterIndex] == str(password)[characterIndex + 1]:
            if characterIndex == 0 or str(password)[characterIndex] != str(password)[characterIndex - 1]:
                if characterIndex == 4 or str(password)[characterIndex] != str(password)[characterIndex + 2]:
                    doubleAdjacentDigits = True
        characterIndex += 1
    
    if doubleAdjacentDigits == True:
        characterIndex = 0
        neverDecreases = True
        while characterIndex < 5:
            if int(str(password)[characterIndex]) > int(str(password)[characterIndex + 1]):
                neverDecreases = False
            characterIndex += 1
        if neverDecreases == True:
            viablePasswords += 1
    password += 1
print(f"The number of viable passwords is {viablePasswords}")
