basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print()

print('orange' in basket)
print()

print('crabgrass' in basket)
print()

print('apple' in basket)
print()

a = set('abracadabra')
b = set('alacazam')
print(a)
print()

print(a - b)
print()

print(a | b)
print()

print(a & b)
print()

print(a ^ b)
print()

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
