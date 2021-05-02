num1 = 42  #variable declaration; initialize; number
num2 = 2.3 #variable declaration; initialize; number
boolean = True #variable declaration; initialize; Boolean
string = 'Hello World' #variable declaration; initialize; string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration; initialize; List
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration; initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration; initialize; tuple
print(type(fruit)) #log statement; type check; tuple
print(pizza_toppings[1]) #log statement; access value; list; string
pizza_toppings.append('Mushrooms') #function; paramater; add value; list; string
print(person['name']) #log statement; dictionary; access value; string
person['name'] = 'George' #dictionary; change value; string
person['eye_color'] = 'blue' #dictionary; add value; string
print(fruit[2]) #log statement; tuple; access value; string

if num1 > 45: #if statement; numbers
    print("It's greater") #log statetment; string
else: #else statement
    print("It's lower") #log statement; string

if len(string) < 5: #if statement; length check; numbers
    print("It's a short word!") #log statement; string
elif len(string) > 15: #else if statement; length check; numbers
    print("It's a long word!") #log statement; string
else: #else statement
    print("Just right!") #log statement; string

for x in range(5): #for loop; start x=0; stop x<5; increment x+1
    print(x) #log statement; numbers
for x in range(2,5): #for loop; start x=2; stop x<5; increment x+1
    print(x) #log statement; numbers
for x in range(2,10,3):#for loop; start x=2; stop x<10; increment x+3
    print(x) #log statement; numbers
x = 0 #variable declaration; numbers
while(x < 5): #while loop; start x=0; stop x<5
    print(x) #log statement; numbers
    x += 1 #increment x+1

pizza_toppings.pop() #list; deletes last value
pizza_toppings.pop(1) #list; deletes value at index 1

print(person) #log statement; dictionary; access values
person.pop('eye_color') #dictionary; deletes value 'eye_color'; strings
print(person) #log statement; dictionary; access values

for topping in pizza_toppings: #for loop; variable declaration; access values; list; strings
    if topping == 'Pepperoni': #if statement; strings
        continue #for loop; continue
    print('After 1st if statement') #log statement; strings
    if topping == 'Olives': #if statement; strings
        break #for loop; break

def print_hello_ten_times(): #function declaration; no paramater
    for num in range(10): #for loop; variable declaration; start num=0; stop num<10; increment num+1; numbers
        print('Hello') #log statement; strings

print_hello_ten_times() #function call; no argument

def print_hello_x_times(x): #function declaration; paramater x
    for num in range(x): #for loop; variable declaration; start num=0; stop num<x; increment num+1; variables; numbers
        print('Hello') #log statement; strings

print_hello_x_times(4) #function call; argument 4

def print_hello_x_or_ten_times(x = 10): #function declararion; paramater x=10 (unless argument passed)
    for num in range(x): #for loop; variable declaration; start num=0; stop num<x; increment num+1; numbers
        print('Hello') #log statement; strings

print_hello_x_or_ten_times() #function call; no argument
print_hello_x_or_ten_times(4) #function call; argument 4 (overrules paramater value in function)


"""   multi line comment
Bonus section
"""

# print(num3) #single line comment (all remainging lines); log statement; NameError (num3 is defined after the program is asked to use it)
# num3 = 72 #variable declaration; should be above the log statement calling it
num3 = 72 #variable declaration; numbers
print(num3) #log statement; variable
# fruit[0] = 'cranberry' #TypeError: 'tuple' object does not support item assignment (tuples are immutable)
# print(person['favorite_team']) #KeyError: 'favorite_team' (key does not exist)
# print(pizza_toppings[7]) #IndexError: list index out of range (index is past last entry in list.)
print(pizza_toppings[len(pizza_toppings)-1]) #log statement; list; access value; length check; list; numbers
#   print(boolean) #IndentationError: unexpected indent
print(boolean) #log statement; variable
# fruit.append('raspberry') #AttributeError: 'tuple' object has no attribute 'append' (tuples are immutable)
# fruit.pop(1) #AttributeError: 'tuple' object has no attribute 'pop' (tupples are immutable)