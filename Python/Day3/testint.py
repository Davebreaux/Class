d = "test"
e = "stuff"
x = f'{d} {e}'
constructor = globals()[x]
junk = constructor()
print(x)
print(junk)