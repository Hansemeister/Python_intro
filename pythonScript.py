#variable assignment and printing
my_name = "Hansemann"
print(my_name + " is now in the house!") # Automatically prints a newLine
print("This prevents an automatic newLine,", end=" ")
print("by writing: print('text', end=" ")\n") # Useful when you dont want the automatic newLine from print

#creating a function
def my_function(integer, string):
    integer = integer*2
    string = string + " sometimes taste funny "
    print(string + "after I've eaten my " + str(integer) + "th-breakfast\n")

my_function(2, "Cake") #calling the function

# for in range loop
def my_for_loop(integer):
    for int in range(-1, integer): #goes from 0 to (range-1) if no base is declared
        print(int)
    print()
my_for_loop(10)

# while loop
def my_while_loop(integer):
    while integer != 0:
        print (integer)
        integer -= 1
    print("The number is now " + str(integer))
my_while_loop(10)
