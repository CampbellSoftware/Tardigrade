# Tardigrade
A Fully Fledged Data Manipulation Program with a built-in Scripting Language written entirely in Python.

# Notice
In order to get the latest executable, look in the releases.

# Features
- A fully custom syntax
- No indentation
- Variable storage, everything else a scripting language might need
- A tkinter program for running the code

# Required Dependencies
- None! (Executable out now!)

# Docs

In the left console, you will be able to script in Glowscript, the native scripting language for Tardigrade. The Syntax goes like "Function Args", where Function is the function, and args are the arguments. You will be able to use the following functions:

## PRINT args; 
Prints args.
## SET x arg; 
Sets a variable named x with value arg.
## LIST x args; 
Creates a list named x with values equal to args.
## LOOP line iter condition; 
Goes back to line. Every time it hits LOOP, iter goes down by one, and once iter reaches zero, the LOOP function stops working. Optional: condition is a condition (x > y, x = y, x < y) that makes it so the LOOP function only takes effect when it is true.
## PLUS x num;
Adds num to x. Num cannot be a variable.
## TIMES x num;
Multiplies x by num. Num cannot be a variable.
## INDEX x y; 
Gets element y in list x.
## IMPORT type file;
Imports a file named file of type type.
## INTERP a TYPE x y b;
Interpolates a function with x values = x and y values = y with type TYPE, sets x to b, and stores the result in a.
## MAP list FUNC num
Maps a function FUNC with value num to list list
## CALL line
Goes to a line, comes back.
## GOTO line
Goes to a line.
## Set functions
DIFF, INTER, SYMDIFF, JOIN. All do the respective set function on two sets.
## MODULO var a b
Takes the modulo of a and b, and stores it in var.
(Not out yet)
## SUM/LEN/MEAN list
Takes the sum/length/mean of a list.
(Not out yet)
## DICT a b
Makes a dict from two lists a and b
(Not out yet)
## FIND x y
Finds element y in dict x.
(Not out yet)

Here is an example you might find helpful:
"SET x 0
PLUS x 1
PRINT x
LOOP 2 5"
which prints 1, 2, 3, 4, 5, and 6.

Thanks for reading the documentation! I am only 14, so any help will be greatly appreciated!
