import simpleMath as Simple

WELCOME_MESSAGE="""
             _______________________________________________
            |                                               |
            |              REALMATH CALCULATOR              |
            |_______________________________________________|

            Welcome to realMath calculator! The calculator
            that does math from left to right!

      Acceptable operations: + - * / ^ % =

        q to quit

"""
print(WELCOME_MESSAGE)
while True:
    calculation = input()
    if calculation == "q":
        break
    print(Simple.solve(calculation))
