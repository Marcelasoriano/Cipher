#name: Marcela Soriano Cornejo
#email: marcela.sorianocornejo40@myhunter.cuny.edu
#date: September 11, 2022
#This program prints: encryptes a message based on caeser cipher when given a phrase and key

phrase=input("input: ")
letters=[*phrase]

key=int(input("shift: "))

cipher=""
for i in letters:
    if ord(i)+key<=122:
        cipher+=chr(ord(i)+key)
    else:
        cipher+=chr(97+(ord(i)+key-123))

print("ciphered string:",cipher)