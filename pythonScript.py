#variable assignment and printing
def assignment_and_print():
    my_name = "Hansemann"
    print(my_name + " is now in the house!") # Automatically prints a newLine
    print("This prevents an automatic newLine,", end=" ")
    print("by writing: print('text', end=" ")\n") # Useful when you dont want the automatic newLine from print
#assignment_and_print()

#creating a function
def my_function(integer, string):
    integer = integer*2
    string = string + " sometimes taste funny "
    print(string + "after I've eaten my " + str(integer) + "th-breakfast\n")

#my_function(2, "Cake") #calling the function

# for in range loop
def my_for_loop(integer):
    for int in range(-1, integer): #goes from 0 to (range-1) if no base is declared
        print(int)
    print()
#my_for_loop(10)

# for each element in array
def for_each():
    colors = ("red", "white", "yellow", "blue", "green", "purple")
    for color in colors:
        print(color)
#for_each()

# backward loop
def backward_loop():
    colors = ("red", "white", "yellow", "blue", "green", "purple")
    for color in reversed(colors):
        print(color)
#backward_loop()

# while loop
def my_while_loop(integer):
    while integer != 0:
        print (integer)
        integer -= 1
    print("The number is now " + str(integer))
#my_while_loop(10)

def iterate_over_collection():
    colors = ("red", "white", "yellow", "blue", "green", "purple")
    for i, color in enumerate(colors):
        print (i, "-->", color)
#iterate_over_collection()

def iterate_over_several_collections():
    names = ("Hans", "Olav", "Oddbjørg Elise")
    colors = ("red", "white", "yellow", "blue", "green", "purple")
    for name, color in zip(names, colors):
        print(name + " --> " + color)
#iterate_over_several_collections()

#sorting and reverse sorting (alphabetical on strings, low---high values on numbers)
def looping_over_sorted():
    colors = ("red", "white", "yellow", "blue", "green", "purple")
    for color in sorted(colors):
        print(color)
    for color in sorted(colors, reverse = True):
        print(color)
#looping_over_sorted()

# the key that is used can be len (length) or str.lower (alphabetical)
def custom_sort_order():
    colors = ("red", "white", "yellow", "blue", "green", "purple")
    print (sorted(colors, key = len))
custom_sort_order()
