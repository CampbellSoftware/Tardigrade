# Tardigrade
A Fully Fledged Data Manipulation Program with a built-in Scripting Language.

In the left console, you will be able to script in Glowscript, the native scripting language for Tardigrade. The Syntax goes like "Function Args", where Function is the function, and args are the arguments. You will be able to use the following functions:

PRINT args; Prints args.
SET x arg; Sets a variable named x with value arg.
LIST x args; Creates a list named x with values equal to args.
LOOP line iter condition; Goes back to line. Every time it hits LOOP, iter goes down by one, and once iter reaches zero, the LOOP function stops working. Optional: condition is a condition (x > y, x = y, x < y) that makes it so the LOOP function only takes effect when it is true.
PLUS x num; Adds num to x. Num cannot be a variable.
TIMES x num; Multiplies x by num. Num cannot be a variable.
INDEX x y; Gets element y in list x.
IMPORT type file; Imports a file named file of type type.
INTERP a TYPE x y b; Interpolates a function with x values = x and y values = y with type TYPE, sets x to b, and stores the result in a.

Here is an example you might find helpful:
"SET x 0
PLUS x 1
PRINT x
LOOP 2 5"
which prints 1, 2, 3, 4, 5, and 6.

Thanks for reading the documentation! I am only 14, so any help will be greatly appreciated!
