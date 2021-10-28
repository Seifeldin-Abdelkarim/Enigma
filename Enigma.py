class enigma:
    def __init__(self, starting_pos, rotors, ringsettings, plugboard):
        plugboard = {'A': 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7, 'I' : 8, 'J' : 9, 'K' : 10, 'L' : 11, 'M': 12, 'N': 13, 'O' : 14, 'P' : 15, 'Q' : 16, 'R' : 17, 'S': 18, 'T' : 19, 'U' : 20, 'V' : 21, 'W' : 22, 'X' : 23, 'Y' : 24, 'Z' : 25, 'a' : 26, 'b' : 27, 'c' : 28, 'd' : 29, 'e' : 30, 'f' : 31, 'g' : 32, 'h' : 33, 'i' : 34, 'j' : 35, 'k' : 36, 'l' : 37, 'm' : 38, 'n' : 39, 'o' : 40, 'p' : 41, 'q' : 42, 'r' : 43, 's' : 44, 't' : 45, 'u' : 46, 'v' : 47, 'w' : 48, 'x' : 49, 'y' : 50, 'z' : 51, '1' : 52, '2' : 53, '3' : 54, '4' : 55, '5' : 56, '6' : 57,'7' : 58,'8' : 59,'9' : 60,'0' : 61}
        rotors = {1 : ["E","K","M","F","L","G","D","Q","V","Z","N","T","O","W","Y","H","X","U","S","P","A","I","B","R","C","J"], 2 : ["A","J","D","K","S","I","R","U","X","B","L","H","W","T","M","C","Q","G","Z","N","P","Y","F","V","O","E"], 3 : ["B","D","F","H","J","L","C","P","R","T","X","V","Z","N","Y","E","I","W","G","A","K","M","U","S","Q","O"], 4 : ["E","S","O","V","P","Z","J","A","Y","Q","U","I","R","H","X","L","N","F","T","G","K","D","C","M","W","B"], 5 : ["V","Z","B","R","G","I","T","Y","U","P","S","D","N","H","L","X","A","W","M","J","Q","O","F","E","C","K"]}
        starting_pos = 0
        

    def ecnrypt(self, stting):
        """
        encrypt the string
        """
        ecnrypted_string = ""
        return ecnrypted_string


class plugboard:
    def __init__(self, c1: str, c2: str):
        self.c1 = c1
        self.c2 = c2

    def pairMap(self):
        """
        replace letter c1 with c2 or c2 with c1
        """


class rotor:
    def __init__(self, keys, notch, starting_pos, offset):
        self.keys = keys  # this is an array/list
        self.notch = notch
        # Dont forget to implment the starting position and the offset

    def advance(self):
        # advance rotor by 1
        pass

    def mapchar2keys(self, char):
        # maps the character to the corresponding key on the rotor
        pass


class reflector:
    def __init__(self, keys):
        self.keys = keys  # this is an array/list

    def mapchar2keys(self, char):
        # maps the character to the corresponding key on the rotor
        pass