import numpy as np

def print_bank(title, items):
    print(desig)
    print(title)
    for i in items:
        print(i)

def check_pair(boat, bank, correct_pair):
    if np.array_equal(boat, correct_pair):
        print("Boat is filled with a good pair")
        bank[0] = boat[0]
        bank[1] = boat[1]
    else:
        print("Pair is wrong")
        print("Try again")

def send_back(boat, character):
    if character == 'M':
        print(desig)
        print("Correct pair, sending back!")
        boat[0] = character
        boat[1] = None
    else:
        print("Empty boat or boat without man cannot be driven :(")

desig = "______________________________________"
A = np.array(['M', 'G', 'C', 'W'])
C = np.array([None, None])
B = np.array([None, None, None, None])

print_bank("River Bank A", A)
print_bank("Boat", C)
print_bank("River Bank B", B)

print("Enter characters into the boat")
C[0] = input()
C[1] = input()

check_pair(C, B, np.array(['M', 'G']))
send_back(C, input())

print_bank("Boat A", C)
print("M -> B")
print("Enter characters into the boat")
C[0] = input()
C[1] = input()

check_pair(C, B, np.array(['M', 'W']))
send_back(C, input())

print_bank("Boat A", C)
print("M, G -> B")
print_bank("River Bank B", B)

if np.array_equal(A, B):
    print("Problem solved successfully using Python")
else:
    print("Try again from the beginning, the answer was wrong")
