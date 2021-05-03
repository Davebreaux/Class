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