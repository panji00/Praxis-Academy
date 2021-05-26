print(list(range(3, 6)))
print()

#
args = [3, 6]
print(list(range(*args)))
print()

#
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volta through it.", end=' ')
    
d = {"voltage": "four ,illion", "state": "bleedin' demised", "action": "VOOM"}
print(parrot(**d))
