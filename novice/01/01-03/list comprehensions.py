squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

squares = list(map(lambda x: x**2, range(10)))
squares = [x**2 for x in range(10)]

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print()

#
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
print(combs)
print()

#
vec = [-4, -2, 0, 2, 4]
print([x*2 for x in vec])
print()

#
print([x for x in vec if x >= 0])
print()

#
print([abs(x) for x in vec])
print()

# #
# reshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# [weapon.strip() for weapon in freshfruit]
# print(weapon.strip)

#
# print(vec = [[1,2,3], [4,5,6], [7,8,9]]
# [num for elem in vec for num in elem])

#
from math import pi
print([str(round(pi, i)) for i in range(1, 6)])

