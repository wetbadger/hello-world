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

INSTALLATION: Put this file somewhere where Python can see it.

EXAMPLE:

--------------------------------------------------------------------
import realMath

problem = '4 + 2 * 3'
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

__version__ = "1.1"
# Version 1.1
#sequential parenthesis no longer computing backwards
#allowed for -(a+b) expressions
#negative numbers are represented as the entered value
#"=" sign returns true or false
# Version 1.0 9/10/2020


import sys
#global so is not reset on solve()
def solve(problem):
    def resolve(problem): #resolves parenthesis into a readable equation
        pLevel=0
        microproblem=""
        resolution=""
        a=""
        for char in problem:
            if char == "(":
                if pLevel > 0:
                    microproblem=microproblem+char
                pLevel+=1
            elif char == ")":
                pLevel-=1
                if pLevel > 0:
                    microproblem=microproblem+char
            elif pLevel > 0:
                microproblem=microproblem+char
            if pLevel == 0 and solve != "":
                if microproblem != "":
                    a = solve(microproblem)
                    microproblem = ""
            if char in ["+","-","*","/","%","^","=","."] and pLevel == 0:
                a=str(a)+char
            if char.isdigit() and pLevel == 0:
                a=str(a)+char
            resolution=resolution+str(a)
            a=""
        return resolution

    def doMath(nums):
        num1 = None
        operator = ""
        num2 = None
        for n in nums:
            if isinstance(n, int) or isinstance(n, float): #set num1 and num2 to numbers, treat anything else as an operator
                if num1 == None:
                    num1 = n
                else:
                    num2 = n
                    break #break out of for loop
            else:
                operator = n
        try:
            if operator == "+":
                a = num1 + num2
            elif operator == "-":
                try:
                    a = num1 - num2
                except:
                    a = num1
            elif operator == "*":
                a = num1 * num2
            elif operator == "/":
                a = num1 / num2
            elif operator == "%":
                a = num1 % num2
            elif operator == "^":
                a = num1**num2
            elif operator == "": #no operator, return just the number
                return num1
            else:
                print(operator)
                return "There was an error."
        except:
            a = sys.exc_info()[0]
            return "Error: " + str(a)
        if len(nums) > 1:
            nums = nums[3:]
            nums.insert(0,a)
            if len(nums)==1:
                answer = nums[0]
                return answer
            else:
                return doMath(nums)
    problem = resolve(problem) #resolve parenthesis
    nums = []
    d = 0
    i = 0 #tracks index in list nums
    whtspc = False
    unary = True #be aware of a minus sign! if a '-' appears before a number, after '+', or inside a parenthesis, treat it as a negative number
    f = -1 #floating point
    ii = 0 #tracks index of problem string
    negative = False
    for char in problem:
        if char.isdigit() and f == -1:
            if negative == False: #check if positive or negative
                digit = d + int(char)
            else:
                digit = (d - int(char))
            if 0 <= i < len(nums):
                nums[i] = digit
            else:
                nums.append(digit)
            d=nums[i]*10
            whtspc = False
            unary = False #stop looking for unarys
        elif char == " " and whtspc == False:
            d=0
            f=-1
            whtspc = True #skip any further white space
        elif char in ["+","-","*","/","%","^"]:
            negative = False #later set to true if unary '-' is found
            nums.append(char)
            d=0
            f=-1
            if unary == True and char == "-":
                negative = True
            elif unary == False:
                i+=2 #add an extra index
            unary = True
            whtspc = True #skip any further white space
        elif char == ".":
            f=10
            unary=False
        elif char.isdigit() and f > -1:
            if 0 <= i < len(nums):
                nums[i] = nums[i] + int(char) / f
            else:
                nums.append(int(char) / f)
            f = f * 10
        elif char == "=":
            if doMath(nums)==solve(problem[ii+1:]): #is the first side = to the second side?
                return True
            else:
                return False
        elif char != " ": #should not trigger ever as of 1.1
            return 'Error: "'+char+'" not a valid operator'
        ii+=1
    oper=0
    for elem in nums:
        if isinstance(elem, int):
            oper=0
            continue
        elif isinstance(elem, str):
            oper+=1
            if oper >= 2:
                nums.remove(elem) #remove redundant "-"
    answer = doMath(nums)
    return answer
