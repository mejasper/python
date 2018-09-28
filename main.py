print("Hello World")
5+6
"5"+"6"  # string concatenation
int("7")  # type conversion
str(5)
float("5.5")
bool("True")
None
# strings

'Hello'
"Don't do that"  # escape characters
"she said \"I want this\""
'she said "i want this"'

# string manipulation

"Hello" + " Nick"  # concatenation
"this costs " + str(6) + " bucks."

"Hello:Nick".split(":")  # string splitting into array
"NIk:AS:AS".split(":")[1]

# booleans

True
False
5 == 5  # compare
5 is 5
5 is not 5

# lists

lit = ["one", "two", "three"]
print(lit)
print("My favourite Numbers are " + str(lit))
lit[1]

# dictionaries

print({"name": "Jasper", "age": 21, "hobby": "none"}['name'])

# variables

greetings = "Hello World"
print(greetings)

# built in functions (just a few basic ones)
len("hello")  # number of characters in hello, works with lists
sorted([1, 2, 3])  # sorts numbers
sorted(["A", "F", "C"])


def my_function():
    print("This is my function")


my_function()

# arguments


def my_other(str1, str2):
    print(str1 + str2)


my_other("lol", "lol")

# default arguments


def print_sth(name="Gucci", age="immeasurable"):
    print("My name is", name, "and I am", age, " .")


print_sth("Swag", 420)
print_sth("Power")

# keyword arguments

print_sth(age=27, name="Nick")

# infinite number of arguments


def print_people(*people):  # * indicates multiple arguments
    for person in people:
        print(person)


print_people("lmao", "vier", "4")

# return values


def do_meth(num1, num2):
    return num1*num2


print(do_meth(132, 2)+do_meth(12, 13))


# conditional statements

check = "swucci"

if not check:
    print("no")
elif check:
    print("yes")
else:
    print("Swucci")


# for while loop

numbers = [1,2,3,4,1,12,3,214,214,124,"Kevin"]

for item in numbers:
    print(item)

run = True
current = 0
while run:
    if current == 12:
        run = False
    else:
        print(current)
        current += 1

