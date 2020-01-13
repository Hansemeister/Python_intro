#variable assignment and printing
my_name = "Hansemann"
print(my_name + " is now in the house!") # Automatically prints a newLine
print("This prevents an automatic newLine,", end=" ")
print("by writing: print('text', end=" ")") # Useful when you dont want the automatic newLine from print

#creating a function
def my_function(integer, string):
    integer = integer*2
    string = string + " sometimes taste funny "
    print(string + "after I've eaten my " + str(integer) + "th-breakfast")

my_function(2, "Cake") #calling the function
