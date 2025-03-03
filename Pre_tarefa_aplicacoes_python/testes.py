import asp

print('conversão em graus')
a = 1 + 2j
print(a)
b = asp.ret2pol(a, 'g')
print(b)
c = asp.pol2ret(*b, 'g')
print(c)

print('\nconversão em radianos')
a = 1 + 2j
print(a)
b = asp.ret2pol(a)
print(b)
c = asp.pol2ret(*b)
print(c)
