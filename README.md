# realMath.py
"""Simple calculator for doing math left to right

This module is designed to do math from left to right ignoring order
of operations. The purpose of this is to prove that PEMDAS also known
as Please Excuse My Dear Aunt Sally, also known as Parenthesis
Exponents Multiplication Division Addition Subtraction is unnecessary
and all math could be done virtually without parenthesis if problems
were solved left to right.

Rather than building a calculator from scratch, this forces python to 
do the operations in order of left to right.

LICENSE: This is open-source software released under the terms of the
GPL (http://www.gnu.org/licenses/gpl.html).

EXAMPLE:

--------------------------------------------------------------------
import realMath

problem = "4 + 2 * 3"
answer = realMath.solve(problem)

print(answer)

OUTPUT:
18
--------------------------------------------------------------------

OVERVIEW:
When entering a problem into realMath.solve(string), the problem should
be expressed as a string. Any amount of whitespace is ignored. And Python
is forced to do operations from left to right.
"""

__version__ = "1.0"

# Version 1.0 9/10/2020
