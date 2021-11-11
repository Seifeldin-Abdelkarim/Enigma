# Enigma
an Enigma machine code
The Enigma machine was created in the early of the 20th century in the year 1919 by the Nazi Germany to Cypher text and messages which protects the integrity and confidentiality of the communications done by them in the military, diplomatic and commercial side. This machine was made during war world 2 in all areas in the German military. The Enigma machine was cracked in the year 1941 by the British cryptologists thereby helping greatly in the war, the person who made the biggest contribution in cracking the code is Alan Turing who was known as an amazing mathematician in that era.

This program was made to simulate an enigma machine will all its functions with some extra features in it, this enigma machine code takes text from the user to cypher, the user chooses 3 rotors out of 5 as well as the ring settings and the offset of the rotors. The text passes through the plugboard, rotors then the reflector and goes all the way back to the plugboard again.
How it works?
This program was done very differently from a typical enigma code where the rotors contain 63 characters which include the ‘space’ button, numbers from 0 to 9, small and capitalized letters. The Rotors rotate and the character’s order change according to every character the user entered in the program to encipher. There are three kinds of rotors in the machine where the user has to choose which one will be the Fast rotor, middle rotor and the slow rotor. The Fast rotor rotates for every character in the text the user entered, while the middle one needs the Fast rotor to rotate a full cycle for it to work, the same for the Slow rotor as it waits for the middle rotor to rotate a full cycle for it to rotate too. The ring settings changes the characters on the rotors depending on what the user wants, which means if a user chooses ring settings ‘B’ for a Rotor, then a character will be changed to the one after it in the alphabet by 1, so an “A” in the rotor will became a “B” and the same for other characters, the characters will keep on rotating instead of going out of bounds so a “Z” in the alphabet will be “A” instead of getting out of the list of Alphabets. The offset the user chooses will the rotor without the user entering characters for it to rotate. So instead of the rotor beginning with 9 it will become 0. For the ring settings and the offset settings, the user gets to choose from 63 characters in both settings. 
What appears for the user?
A menu will appear in front of the user asking if he’s going to change the rotors, ring settings and offset values from the default ones, or if he wants to reset the program to its default state, the program will persist until the user exits voluntarily from the program. The program can also take text from a .txt file to cypher and it can also write the cyphered/deciphered text in a .txt file. Every Input has its own validation asking the user to enter the right characters for the Enigma since it cannot cypher characters that it doesn’t have.
