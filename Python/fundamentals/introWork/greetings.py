""" DPart I & II
Write a program that asks for a users name, and greets them with their name
If the name given is the same as your name, say "Hey, that's my name too!" """
userName = input('What is your name?')
print(f'Hello {userName}')
if userName.lower() == 'dave':
    print('Hey! That\'s my name too!')

"""Part III
Ask for 10 names and keep a record of them.  After 10 names are given, say 'It was nice to meet all of you'."""
names = []
x=0
while x < 10:
    names.append(input('What is your name?'))
    x += 1
else:
    print('It was nice to meet all of you.')
    for y in names:
        print(y)

"""
Part IV - NINJA Level
Ask for 10 names again.  This time check to see if the name was already given.  If it hasn't greet them other wise ask for a new name.  At the end of the program, you should have greeted 10 unique names.
"""
names2 = []
x=0
while x < 10:
    temp = input('What is your name?')
    for entry in names2:
        if entry != temp:
            continue
        else:
            print('name already given')
            break
    else:
        names2.append(temp)
        x += 1
else:
    print('It was nice to meet all of you.')
    for y in names2:
        print(y)
    