from typing import Counter
from dictsfile import *

countF = 0
countM = 0
countS = 0


def rotate(countF, countM, countS):
    countF += 1
    insert = rotorslist[r3][0]
    rotorslist[r3].append(rotorslist[r3].pop(0))
    if countF == 62:
        countM += countM
        insert = rotorslist[r2][0]
        rotorslist[r2].insert(-1, insert)
        rotorslist[r2].pop(0)
        countF = 0
    if countM == 62:
        insert = rotorslist[r1][0]
        rotorslist[r1].insert(-1, insert)
        rotorslist[r1].pop(0)
        countM = 0
        countS += 1
    if countS == 62:
        countS = 0
    return countF, countM, countS


def options():
    print(
        "Please Enter the Rotors you are going to use for Fast, middle and slow rotors. "
    )
    while True:
        try:
            r3 = int(input("Fast Rotor: "))
        except ValueError:
            print("you entered the wrong data type. ")
            continue
        if r3 > 5:
            print("please enter the correct number from 1 to 5. ")
        elif r3 < 1:
            print("please enter the correct number from 1 to 5. ")
        else:
            break

    while True:
        try:
            r2 = int(input("Middle Rotor: "))
        except ValueError:
            print("you entered the wrong data type. ")
            continue
        if r2 > 5:
            print("please enter the correct number from 1 to 5. ")
        elif r2 < 1:
            print("please enter the correct number from 1 to 5. ")
        elif r2 == r3:
            print("please don't repeat the same Rotor. ")
        else:
            break

    while True:
        try:
            r1 = int(input("Slow Rotor: "))
        except ValueError:
            print("you entered the wrong data type. ")
            continue
        if r1 > 5:
            print("please enter the correct number from 1 to 5. ")
        elif r1 < 1:
            print("please enter the correct number from 1 to 5. ")
        elif r1 == r2 or r1 == r3:
            print("please don't repeat the same Rotor. ")
        else:
            break
    return r3, r2, r1


def encrypt(text, Alphabet):
    character = ""
    global countF, countM, countS
    for c in text:
        countF, countM, countS = rotate(countF, countM, countS)
        character = applyPlugboard(c)

        for rotor, count in ((r3, countF), (r2, countM), (r1, countS)):
            character = rotorslist[rotor][Alphabet.index(character) + count]
            print(character)

        character = refB[Alphabet.index(character)]
        print(character)

        for rotor, count in ((r1, countS), (r2, countM), (r3, countF)):
            charindex = rotorslist[rotor].index(character)
            character = Alphabet[charindex - count]
            print(character + " 1")

        character = applyPlugboard(character)

        # rotate(countF, countM)
        Atext.append(character)
    s = "".join(Atext)
    print(s)
    return Atext


def applyPlugboard(character):
    for j in range(len(plugboard)):
        if character == plugboard[j][0]:
            character = plugboard[j][1]
        elif character == plugboard[j][1]:
            character = plugboard[j][0]
    return character


countF = 0
countM = 0
countS = 0
Atext = []

r3, r2, r1 = options()

# text = "A"

text = input("here: ")
encrypt(text, Alpha)
