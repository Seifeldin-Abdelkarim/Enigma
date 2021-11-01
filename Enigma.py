def rotate(countF, countM):
    insert = ''
    countF += 1
    insert = rotors[r3][0]
    rotors[r3].insert(-1,insert)
    rotors[r3].pop(0)
    if countF == 62:
        countM += countM
        insert = rotors[r2][0]
        rotors[r2].insert(-1,insert)
        rotors[r2].pop(0)
        countF = 0
    if countM == 62:
        insert = rotors[r1][0]
        rotors[r1].insert(-1,insert)
        rotors[r1].pop(0)
        countM = 0
    return countF, countM

def options():
    print("Please Enter the Rotors you are going to use for Fast, middle and slow rotors. ")
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

def encrypt(text, Alpha):
    temp = ''
    for i in text:
        rotate(countF, countM)
        for j in range(len(plugboard)):
            if i == plugboard[j][0]:
                temp = plugboard[j][1]
            elif i == plugboard[j][1]:
                temp = plugboard[j][0]
        
        for j in range(62):
            if Alpha[temp] == j:
                temp = rotors[r3][j]
                print(temp + "1")
                break
        
        for k in range(62):
            if Alpha[temp] == k:
                temp = rotors[r2][k]
                print(temp + "2")
                break
            
        for l in range(62):
            if Alpha[temp] == l:
                temp = rotors[r1][l]
                print(temp + "3")
                break
            
        for m in range(62):
            if Alpha[temp] == m:
                temp = refB[m]
                print(temp + "4")
                break
            
        for n in range(62):
            if Alpha[temp] == n:
                temp = rotors[r1][n]
                print(temp + "5")
                break
            
        for o in range(62):
            if Alpha[temp] == o:
                temp = rotors[r2][o]
                print(temp + "6")
                break
            
        for p in range(62):
            if Alpha[temp] == p:
                temp = rotors[r3][p]
                print(temp + "7")
                break
            
        for j in range(len(plugboard)):
            if temp == plugboard[j][0]:
                temp = plugboard[j][1]
            elif temp == plugboard[j][1]:
                temp = plugboard[j][0]
            
        
        
        # rotate(countF, countM)
        Atext.append(temp)
    s = ''.join(Atext)
    print(s)
    return Atext


rotors = {1 : ["E","K","M","F", "L", "G", "D", "Q", "V", "Z", "N", "T", "O", "W", "Y", "H", "X", "U", "S", "P", "A", "I", "B", "R", "C", "J", 'q', 'w', 'u', 'e', 's', 'b', 'd', 'h', 'x', 'a', 'z', 'v', 'm', 'k', 'i', 'n', 'p', 'g', 'l', 'c', 't', 'y', 'o', 'f', 'r', 'j','4', '2', '6', '0', '8', '1', '9', '3', '7', '5'], 2 : ["A","J","D","K","S","I","R","U","X","B","L","H","W","T","M","C","Q","G","Z","N","P","Y","F","V","O","E",'f', 'q', 'e', 'r', 's', 'u', 'h', 'k', 'i', 'w', 'p', 'a', 'c', 'y', 'l', 'o', 'n', 'x', 'm', 'j', 'z', 't', 'g', 'v', 'd', 'b', '8', '1', '4', '6', '3', '5', '2', '0', '7', '9'], 3 : ["B","D","F","H","J","L","C","P","R","T","X","V","Z","N","Y","E","I","W","G","A","K","M","U","S","Q","O",'a', 'g', 'o', 'w', 'y', 'k', 'j', 'q', 'r', 'i', 'f', 'p', 'u', 'n', 'v', 'l', 'c', 'd', 't', 'h', 'm', 'z', 'e', 'x', 'b', 's', '5', '9', '7', '8', '2', '4', '3', '0', '6', '1'], 4 : ["E","S","O","V","P","Z","J","A","Y","Q","U","I","R","H","X","L","N","F","T","G","K","D","C","M","W","B",'z', 'a', 'g', 's', 'm', 'y', 'o', 'v', 'k', 'f', 'l', 'x', 'c', 'n', 'p', 'u', 't', 'r', 'q', 'j', 'i', 'e', 'w', 'b', 'h', 'd', '4', '8', '3', '5', '6', '0', '7', '2', '1', '9'], 5 : ["V","Z","B","R","G","I","T","Y","U","P","S","D","N","H","L","X","A","W","M","J","Q","O","F","E","C","K", 's', 'b', 'd', 'z', 'n', 'e', 'm', 'v', 'g', 'h', 'a', 't', 'u', 'c', 'o', 'p', 'r', 'i', 'j', 'y', 'f', 'w', 'l', 'k', 'q', 'x','1', '2', '5', '7', '4', '9', '6', '8', '3', '0']}
refB= ['Y','R','U','H','Q','S','L','D','P','X','N','G','O','K','M','I','E','B','F','Z','C','W','V','J','A','T', 'z', 'y', 'g', 'b', 'r', 'j', 's', 'm', 'n', 'x', 'c', 'e', 'a', 'd', 'v', 'k', 'l', 'p', 'i', 'f', 'q', 'h', 'o', 'w', 'u', 't','1', '8', '7', '3', '5', '2', '6', '0', '4', '9']
Alpha = {'A': 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7, 'I' : 8, 'J' : 9, 'K' : 10, 'L' : 11, 'M': 12, 'N': 13, 'O' : 14, 'P' : 15, 'Q' : 16, 'R' : 17, 'S': 18, 'T' : 19, 'U' : 20, 'V' : 21, 'W' : 22, 'X' : 23, 'Y' : 24, 'Z' : 25, 'a' : 26, 'b' : 27, 'c' : 28, 'd' : 29, 'e' : 30, 'f' : 31, 'g' : 32, 'h' : 33, 'i' : 34, 'j' : 35, 'k' : 36, 'l' : 37, 'm' : 38, 'n' : 39, 'o' : 40, 'p' : 41, 'q' : 42, 'r' : 43, 's' : 44, 't' : 45, 'u' : 46, 'v' : 47, 'w' : 48, 'x' : 49, 'y' : 50, 'z' : 51, '1' : 52, '2' : 53, '3' : 54, '4' : 55, '5' : 56, '6' : 57,'7' : 58,'8' : 59,'9' : 60,'0' : 61}
plugboard = (('A', 'B'), ('C', 'D'),('E', 'F'), ('G', 'H'),('I', 'J'), ('K', 'L'),('M', 'N'), ('O', 'P'),('Q', 'R'), ('S', 'T'),('U', 'V'), ('W', 'X'),('Y', 'Z'), ('a', 'b'),('c', 'd'), ('e', 'f'),('g', 'h'), ('i', 'j'),('k', 'l'), ('m', 'n'),('o', 'p'), ('q', 'r'),('s', 't'), ('u', 'v'),('w', 'x'), ('y', 'z'),('1', '2'), ('3', '4'),('5', '6'), ('7', '8'),('9', '0'))


countF = 0
countM = 0
Atext = []

r3, r2, r1 = options()

text = 'A'

# text = input("here: ")
encrypt(text, Alpha)
