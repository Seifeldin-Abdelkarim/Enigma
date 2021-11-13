from dictsfile import *  # imports all the lines from another file called dictsfile
import os  # imports os for some functionality thats used in the code
from time import sleep  # imports time for some functionality thats used in the code


class Enigma:
    def __init__(  # initial values for every element
        self,
        R1=0,
        R2=0,
        R3=0,
        Of1=0,
        Of2=0,
        Of3=0,
        Atext=[],
    ):
        self.ringset1 = R1
        self.ringset2 = R2
        self.ringset3 = R3
        self.offset3 = Of1
        self.offset2 = Of2
        self.offset1 = Of3
        self.Atext = Atext
        self.rotorslist = rotorslist.copy()  # self.rotorslistB = rotorslist.copy()

        self.rotorslistB = [R1, R2, R3, Of1, Of2, Of3, Atext]

    def applyPlugboard(
        self, character  # applies the plugboard on the text entered by the user
    ):
        for j in range(len(plugboard)):
            if character == plugboard[j][0]:
                character = plugboard[j][1]
            elif character == plugboard[j][1]:
                character = plugboard[j][0]
        return character

    def rotate(
        self,
        r3,
        r2,
        r1,
        countF,
        countM,
        countS,  # the rotors lists shift for every letter thats entered
    ):
        countF += 1
        self.rotorslist[r3].append(self.rotorslist[r3].pop(0))
        if countF == 62:
            countM += countM
            self.rotorslist[r2].append(self.rotorslist[r2].pop(0))
            countF = 0
        if countM == 62:
            self.rotorslist[r1].append(self.rotorslist[r1].pop(0))
            countM = 0
            countS += 1
        if countS == 62:
            countS = 0

    def ringsettings(
        self,
        Alpha,
        r3,
        r2,
        r1,  # assigns the ring settings from the user with validation
    ):
        self.ringset3 = input("Enter the ringsettings value for rotor 3: ")
        while self.ringset3 not in Alpha:
            print("you entered an invalid character.")
            self.ringset3 = input("please try again")
        self.ringset2 = input("Enter the ringsettings value for rotor 2: ")
        while self.ringset2 not in Alpha:
            print("you entered an invalid character.")
            self.ringset2 = input("please try again")
        self.ringset1 = input("Enter the ringsettings value for rotor 1: ")
        while self.ringset1 not in Alpha:
            print("you entered an invalid character.")
            self.ringset1 = input("please try again")

        for rotor, ringset in (  # for every rotor with its own assigned ringsettings
            (r3, self.ringset3),
            (r2, self.ringset2),
            (r1, self.ringset1),
        ):
            if (
                ringset
                != 0  # if the user uses ringsettings, the rotors letters will characters will change accordingly
            ):
                Index = Alpha.index(ringset)
                for k in range(Index):
                    for i in range(len(self.rotorslist[rotor])):

                        if self.rotorslist[rotor][i] == "Z":
                            self.rotorslist[rotor][i] = chr(
                                ord(self.rotorslist[rotor][i]) - 25
                            )
                        elif self.rotorslist[rotor][i] == "z":
                            self.rotorslist[rotor][i] = chr(
                                ord(self.rotorslist[rotor][i]) - 25
                            )
                        elif self.rotorslist[rotor][i] == "9":
                            self.rotorslist[rotor][i] = chr(
                                ord(self.rotorslist[rotor][i]) - 9
                            )
                        elif self.rotorslist[rotor][i] == " ":
                            self.rotorslist[rotor][i] == " "
                        else:
                            self.rotorslist[rotor][i] = chr(
                                ord(self.rotorslist[rotor][i]) + 1
                            )

    def offsetsettings(self, Alpha, r3, r2, r1):
        self.offset3 = input(
            "Enter the offset value for rotor 3: "  # the offsets for every rotor are assigned with validation
        )
        while self.offset3 not in Alpha:

            self.offset3 = input("please try again: ")
        self.offset2 = input("Enter the offset value for rotor 2: ")
        while self.offset2 not in Alpha:

            self.offset2 = input("please try again: ")
        self.offset1 = input("Enter the offset value for rotor 1: ")
        while self.offset1 not in Alpha:

            self.offset1 = input("please try again: ")

        for offset, rotor in (  # for every rotor with its own assigned offset settings
            (self.offset3, r3),
            (self.offset2, r2),
            (self.offset1, r1),
        ):
            if (
                offset
                != 0  # if the user uses offsets, the rotors will rotate accordingly at the start
            ):
                index = Alpha.index(offset)

                self.rotorslist[rotor].extend(self.rotorslist[rotor][:index])

                del self.rotorslist[rotor][:index]

    def clear(self):  # clears the terminal to make the program more readable
        os.system("cls" if os.name == "nt" else "clear")

    def Rotors(self):  # assignment of the 5 Rotors in the program with validation
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

    def encrypt(self, Alphabet, r3, r2, r1):
        countF = 0
        countM = 0
        countS = 0
        text = input(
            "please enter the text: "  # takes the text from the user and validates it
        )
        for char in text:
            while char not in Alpha:
                print("you entered an invalid character: ")
                text = input("please try again: ")  # keeps repeating

        for (
            character
        ) in text:  # every character of the text goes into the machine for decryption
            self.rotate(
                r3,
                r2,
                r1,
                countF,
                countM,
                countS,  # the rotors rotate depending on how many characters were passed into it
            )
            character = self.applyPlugboard(character)

            for rotor in r3, r2, r1:
                character = self.rotorslist[rotor][
                    Alphabet.index(character)  # character passes through the rotors
                ]

            character = refB[
                Alphabet.index(character)  # character passes through the reflector
            ]

            for rotor in r1, r2, r3:
                charindex = self.rotorslist[
                    rotor
                ].index(  # character goes through rotors again
                    character
                )
                character = Alphabet[charindex]

            character = self.applyPlugboard(  # applies the plugboard on the character
                character
            )
            self.Atext.append(character)
        s = "".join(self.Atext)  # prints the encrypted/decrypted text
        print(s)
        self.Atext.clear()

    def reset(self):  # resets the rotors to their initial settings
        self.__init__(
            self.rotorslistB[0],
            self.rotorslistB[1],
            self.rotorslistB[2],
            self.rotorslistB[3],
            self.rotorslistB[4],
            self.rotorslistB[5],
            self.rotorslistB[6],
        )
        # self.rotorslist = self.rotorslistB

    def mainmenu(self, Alpha):  # the main menu that will appear infornt of the user
        flag = 0
        count = False
        self.clear()
        print(
            "Welcome to the Enigma machine, customize the settings of the machine before you start. "
        )
        while flag == 0:
            print("1) Rotors settings")
            print("2) Ring settings")
            print("3) Offset of the Rotors")
            print("4) Encrypt/Decrypt Text")
            print("5) Exit the machine")
            while True:
                try:
                    choice = int(input("What is your choice?: "))  # the user's choice
                except ValueError:
                    print("you entered the wrong data type. ")
                    continue
                if choice > 5 or choice < 1:
                    print("please enter choices between 1 and 5")
                else:
                    break
            if choice == 1:
                self.clear()
                r3, r2, r1 = self.Rotors()
                count = True
                sleep(0.5)  # sleep() is used to stop the process for 0.5 sec
                self.clear()  # clear() clears the terminal
            elif choice == 2 and count == True:
                self.clear()
                self.reset()
                self.ringsettings(Alpha, r3, r2, r1)
                sleep(0.5)
            elif choice == 3 and count == True:
                self.clear()
                self.reset()
                self.offsetsettings(Alpha, r3, r2, r1)
                sleep(0.5)
            elif choice == 4 and count == True:
                self.clear()
                self.encrypt(Alpha, r3, r2, r1)
                self.reset()
                sleep(0.5)
            elif choice == 5:
                self.clear()
                print("Come again next time :)")
                break
            else:
                self.clear()
                print(
                    "please enter the rotor settings first before other options to initialize the rotors you are going to use. "
                )


Enigma1 = Enigma()
Enigma1.mainmenu(Alpha)
# Enigma1() = Enigma.Rotors()
