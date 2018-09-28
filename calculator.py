import re

print("Calculator:")

previous = 0
run = True
equasion = ""


def perform():
    global run
    global equasion
    global previous

    if previous == 0:
        equasion = input("Enter equasion\n")
    elif equasion == "quit":
        run = False
    else:
        equasion = input(previous)


    equasion = re.sub('[a-zA-Z,.:()" "]', '', equasion)
    if previous == 0:
        previous = eval(equasion)
    else:
        previous = eval(str(previous)+equasion)


while run:
    perform()

