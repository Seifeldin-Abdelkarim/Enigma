from typing import Counter
from dictsfile import *

countF = 0
countM = 0
countS = 0


def applyPlugboard(character):
    for j in range(len(plugboard)):
        if character == plugboard[j][0]:
            character = plugboard[j][1]
        elif character == plugboard[j][1]:
            character = plugboard[j][0]
    return character


def rotate(countF, countM, countS):
    countF += 1
    rotorslist[r3].append(rotorslist[r3].pop(0))
    if countF == 62:
        countM += countM
        rotorslist[r2].append(rotorslist[r2].pop(0))
        countF = 0
    if countM == 62:
        rotorslist[r1].append(rotorslist[r1].pop(0))
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

    while True:
        try:
            choice = str(
                input("Are you going to choose a specific ringsettings? y or n: ")
            )
            choice = choice.lower()
        except ValueError:
            print("you entered the wrong data type. ")
            continue
        if choice != "y" and choice != "n":
            print("please enter only the letters Y or N for your choice. ")
        else:
            break
    ringset1 = 0
    ringset2 = 0
    ringset3 = 0
    if choice == "y":
        ringset3 = input("Enter the ringsettings value for rotor 3: ")
        while ringset3 not in Alpha:
            print("you entered an invalid character.")
            ringset3 = input("please try again")
        ringset2 = input("Enter the ringsettings value for rotor 2: ")
        while ringset2 not in Alpha:
            print("you entered an invalid character.")
            ringset2 = input("please try again")
        ringset1 = input("Enter the ringsettings value for rotor 1: ")
        while ringset1 not in Alpha:
            print("you entered an invalid character.")
            ringset1 = input("please try again")
    while True:
        try:
            choice = str(input("Are you going to choose a specific offset? y or n: "))
            choice = choice.lower()
        except ValueError:
            print("you entered the wrong data type. ")
            continue
        if choice != "y" and choice != "n":
            print("please enter only the letters Y or N for your choice. ")
        else:
            break
    offset3 = 0
    offset2 = 0
    offset1 = 0
    if choice == "y":
        offset3 = input("Enter the offset value for rotor 3: ")
        while offset3 not in Alpha:
            print("you entered an invalid character.")
            offset3 = input("please try again")
        offset2 = input("Enter the offset value for rotor 2: ")
        while offset2 not in Alpha:
            print("you entered an invalid character.")
            offset2 = input("please try again")
        offset1 = input("Enter the offset value for rotor 1: ")
        while offset1 not in Alpha:
            print("you entered an invalid character.")
            offset1 = input("please try again")

    text = input("please enter the text: ")
    for char in text:
        while char not in Alpha:
            print("you entered an invalid character: ")
            text = input("please try again: ")  # keeps repeating

    return r3, r2, r1, text, offset1, offset2, offset3, ringset1, ringset2, ringset3


def encrypt(text, Alphabet, offset1, offset2, offset3, ringset1, ringset2, ringset3):
    character = ""
    global countF, countM, countS

    for offset, rotor in ((offset3, r3), (offset2, r2), (offset1, r1)):
        if offset != 0:
            index = Alphabet.index(offset)

            rotorslist[rotor].extend(rotorslist[rotor][:index])

            del rotorslist[rotor][:index]

    for rotor, ringset in ((r3, ringset3), (r2, ringset2), (r1, ringset1)):
        if ringset != 0:
            Index = Alphabet.index(ringset)
            for k in range(Index):
                for i in range(len(rotorslist[rotor])):
                    # asciiNum = ord(rotorslist[rotor][i])
                    if rotorslist[rotor][i] == "Z":
                        rotorslist[rotor][i] = chr(ord(rotorslist[rotor][i]) - 25)
                    elif rotorslist[rotor][i] == "z":
                        rotorslist[rotor][i] = chr(ord(rotorslist[rotor][i]) - 25)
                    elif rotorslist[rotor][i] == "9":
                        rotorslist[rotor][i] = chr(ord(rotorslist[rotor][i]) - 9)
                    elif rotorslist[rotor][i] == " ":
                        rotorslist[rotor][i] == " "
                    else:
                        rotorslist[rotor][i] = chr(ord(rotorslist[rotor][i]) + 1)

    for character in text:
        countF, countM, countS = rotate(countF, countM, countS)
        character = applyPlugboard(character)

        for rotor, count in ((r3, countF), (r2, countM), (r1, countS)):

            character = rotorslist[rotor][Alphabet.index(character)]

        character = refB[Alphabet.index(character)]

        for rotor, count in ((r1, countS), (r2, countM), (r3, countF)):
            charindex = rotorslist[rotor].index(character)
            character = Alphabet[charindex]

        character = applyPlugboard(character)
        Atext.append(character)
    s = "".join(Atext)
    print(s)
    return Atext


def mainmenu():
    pass


countF = 0
countM = 0
countS = 0
Atext = []

r3, r2, r1, text, offset1, offset2, offset3, ringset1, ringset2, ringset3 = options()


encrypt(text, Alpha, offset1, offset2, offset3, ringset1, ringset2, ringset3)
