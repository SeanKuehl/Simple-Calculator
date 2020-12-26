
# start of function 1
#all test cases are dealt with in one way or the other.
#try this test case: 4 / 41 * 1000 / 2 ^ 2222 / -42 + 999999999 - 1 ^ 1000000
#this input gives an error: 1 + 2 * 76 - 0.5 * 100 ^ 100 - 2222
#above test case produces number I have trouble dealing with
#good test case: 2 * ( 3 ^ 1.5 ) - 9 * 8 * 2 + ( 1000 / 2 ) + 1 ^ 0




def StartingErrorCheck():
    x = str(input())
    if len(x) > 100:

        raise Exception("input too long")

        # throw self-made error message
        # nums too long
    x = x.split()
    x = list(x)
    if len(x) > 50:

        raise Exception("too many terms")
        # throw self-made error message
        # line too long

    openBracketCount = 0
    closedBracketCount = 0
    lastCharacterOperator = False
    requiredChecks = []
    operatorList = ["(", ")", "^", "-", "+", "*", "/", "//"]

    for item in x:

        if item not in operatorList:
            lastCharacterOperator = False
        if item == '(':
            openBracketCount += 1
        if item == ')':
            closedBracketCount += 1
        if item in operatorList:
            print(item)
            if lastCharacterOperator == False:
                lastCharacterOperator = True
            else:

                raise Exception("double operator error")
                # throw double operator custom error

    if openBracketCount != closedBracketCount:

        raise Exception("bracket error")
        # throw custom error
    BracketArrow(x)

    print(x)

# end of function 1

# start of function 2

    # this is the bracket arrow
    # go with no nested brackets rule
def BracketArrow(x):

    #make def cycle which will go through all the arrows, pass each bracket through all the arrows
    count = 0
    bracketStart = -1
    bracketStop = 0
    bracketList = []
    temporaryX = x
    bracketLength = 0
    temporaryCount = 0
    bracketOpen = False
    complete = False

    for item in x:


        if item == '(':
            bracketOpen = True

            #this is only being called once, why?

        count += 1
        temporaryCount = count
        if bracketOpen == True:
            bracketList.append(item)


        if item == ')':
            bracketOpen = False

            bracketStart = x.index('(')
            bracketStop = x.index(')')


            #print(x, bracketStart)


            for i in range(bracketStart,bracketStop,1):
                x.pop(bracketStart)

            x.pop(x.index(')')) #get rid of the bracket that is left over after
                #-1/+1 to deal with the brackets themselves
            #why would count = 0 at some point past start?


            bracketList = BracketArrowCycle(bracketList)



            x.insert(bracketStart, bracketList)



            count = temporaryCount
            #x altering code will be put here
            bracketList = []
            bracketLength = 0

            if '(' in x:
                BracketArrow(x)




    x = ArrowCycle(x)
    print(x)




    # call the exponents etc things to check for and solve the different things
    # this should make a list of items in brackets and then where in the list it starts and stops.


# end of function 2


# start of function 3

def BracketArrowCycle(x):

    x = ExponentArrow(x, returnBool = True)

    x = IntDivisionArrow(x, returnBool = True)

    x = MainDivisionArrow(x, returnBool = True)


    x = MultiplicationArrow(x, returnBool = True)


    x = AdditionArrow(x, returnBool = True)


    x = SubtractionArrow(x, returnBool = True)

    x = Trim(x)


    return x

def ArrowCycle(x):

    #only the above print(x) is reached, therefor, the error is encountered in ExponentArrow
    x = ExponentArrow(x, returnBool = True)
    print(x)

    x = IntDivisionArrow(x, returnBool = True)
    print(x)
    x = MainDivisionArrow(x, returnBool = True)
    print(x)
    x = MultiplicationArrow(x, returnBool = True)
    print(x)
    x = AdditionArrow(x, returnBool = True)
    print(x)
    x = SubtractionArrow(x, returnBool = True)
    print(x)


    return x



# this is the exponent solver

def Trim(x):
    #this will take bracketlist from ['(', 128.0, ')']
    #to a string or something that can be put in the list


    x.pop(0)

    x.pop(-1)


    #remove the brackets

    x = x[0]

    return x

def ExponentArrow(x, returnBool = False):
    #error is in first or second repitition of this function
    #error may be related to lack of sign correction. Add sign correction to
    #all arrow functions, it applies to all of them, not just addition and
    #subtraction!

    numberForPlacement = 0
    temporarySignSpot = 0
    numberOneNegative = 1
    numberTwoNegative = 1
    count = 0
    signSpot = 0
    signCorrection = False




    # it is -+1 because of the spacing between things
    for item in x:

        if item == '^':

            signSpot = count

        count += 1

        if signSpot > 0:

            numberOne = (x[signSpot - 1])
            numberTwo = (x[signSpot + 1])
            print(numberOne, numberTwo, signSpot + 1, x)
            if str(numberOne)[0] == '-':
                numberOneNegative = -1
            elif x[signSpot - 2] == '-':
                numberOneNegative = -1
                signCorrection = True
            if str(numberTwo)[0] == '-':
                numberTwoNegative = -1
            if signCorrection == True:
                x.pop(signSpot - 2)
                x.insert(signSpot - 2, '+')



            try:
                if ((float(x[signSpot - 1]) * numberOneNegative) ** (float(x[signSpot + 1]) * numberTwoNegative)) > 0 and (float(x[signSpot - 1]) * numberOneNegative) ** (float(x[signSpot + 1]) * numberTwoNegative) * -1 > 0:
                    raise Exception("result of exponent caused stack overflow")
            except:
                raise Exception("result of exponent causes stack overflow")


            numberForPlacement = (float(x[signSpot - 1]) * numberOneNegative) ** (float(x[signSpot + 1]) * numberTwoNegative)

            x.insert(signSpot - 1, numberForPlacement)
            # puts it behind current element there
            for y in range(3):
                x.pop(signSpot + 2)
                signSpot -= 1

            signSpot = 0    #loop could keep going without it



    if '^' in x:
        x = ExponentArrow(x, returnBool)



    if returnBool == True:
        return x


def MainDivisionArrow(x, returnBool = False):
    count = 0
    signSpot = 0
    numberForPlacement = 0
    temporarySignSpot = 0
    numberOneNegative = 1
    numberTwoNegative = 1
    signCorrection = False

    # it is -+1 because of the spacing between things
    for item in x:
        if item == '/':
            signSpot = count
        count += 1

        if signSpot > 0:
            numberOne = (x[signSpot - 1])
            numberTwo = (x[signSpot + 1])

            if str(numberOne)[0] == '-':
                numberOneNegative = -1
            elif x[signSpot - 2] == '-':
                numberOneNegative = -1
                signCorrection = True
            if str(numberTwo)[0] == '-':
                numberTwoNegative = -1
            if signCorrection == True:
                x.pop(signSpot - 2)
                x.insert(signSpot - 2, '+')

            if (((float(x[signSpot - 1]) * numberOneNegative) - (float(x[signSpot + 1]) * numberTwoNegative)) > 0 and (float(x[signSpot - 1]) * numberOneNegative) - (float(x[signSpot + 1]) * numberTwoNegative) * -1 > 0):
                raise Exception("result of exponent caused stack overflow")

            numberForPlacement = (float(x[signSpot - 1]) * numberOneNegative) / (float(x[signSpot + 1]) * numberTwoNegative)

            x.insert(signSpot - 1, numberForPlacement)
            # puts it behind current element there
            for y in range(3):
                x.pop(signSpot + 2)
                signSpot -= 1

            signSpot = 0

    if '/' in x:
        x = MainDivisionArrow(x, returnBool)

    if returnBool == True:
        return x

def IntDivisionArrow(x, returnBool = False):
    count = 0
    signSpot = 0
    numberForPlacement = 0
    temporarySignSpot = 0
    numberOneNegative = 1
    numberTwoNegative = 1
    signCorrection = False

    # it is -+1 because of the spacing between things
    for item in x:
        if item == '//':
            signSpot = count
        count += 1

        if signSpot > 0:
            numberOne = (x[signSpot - 1])
            numberTwo = (x[signSpot + 1])

            if str(numberOne)[0] == '-':
                numberOneNegative = -1
            elif x[signSpot - 2] == '-':
                numberOneNegative = -1
                signCorrection = True
            if str(numberTwo)[0] == '-':
                numberTwoNegative = -1
            if signCorrection == True:
                x.pop(signSpot - 2)
                x.insert(signSpot - 2, '+')

            if (((float(x[signSpot - 1]) * numberOneNegative) - (float(x[signSpot + 1]) * numberTwoNegative)) > 0 and (float(x[signSpot - 1]) * numberOneNegative) - (float(x[signSpot + 1]) * numberTwoNegative) * -1 > 0):
                raise Exception("result of exponent caused stack overflow")

            numberForPlacement = (float(x[signSpot - 1]) * numberOneNegative) // (float(x[signSpot + 1]) * numberTwoNegative)

            x.insert(signSpot - 1, numberForPlacement)
            # puts it behind current element there
            for y in range(3):
                x.pop(signSpot + 2)
                signSpot -= 1

            signSpot = 0

    if '//' in x:
        x = IntDivisionArrow(x, returnBool)

    if returnBool == True:
        return x

def MultiplicationArrow(x, returnBool = False):
    count = 0
    signSpot = 0
    numberForPlacement = 0
    temporarySignSpot = 0
    numberOneNegative = 1
    numberTwoNegative = 1
    signCorrection = False

    # it is -+1 because of the spacing between things
    for item in x:
        if item == '*':
            signSpot = count
        count += 1

        if signSpot > 0:
            numberOne = (x[signSpot - 1])
            numberTwo = (x[signSpot + 1])

            if str(numberOne)[0] == '-':
                numberOneNegative = -1
            elif x[signSpot - 2] == '-':
                numberOneNegative = -1
                signCorrection = True
            if str(numberTwo)[0] == '-':
                numberTwoNegative = -1
            if signCorrection == True:
                x.pop(signSpot - 2)
                x.insert(signSpot - 2, '+')

            if ((float(x[signSpot - 1]) * numberOneNegative) ** (float(x[signSpot + 1]) * numberTwoNegative)) > 0 and (float(x[signSpot - 1]) * numberOneNegative) ** (float(x[signSpot + 1]) * numberTwoNegative) * -1 > 0:
                raise Exception("result of exponent caused stack overflow")


            numberForPlacement = (float(x[signSpot - 1]) * numberOneNegative) * (float(x[signSpot + 1]) * numberTwoNegative)

            x.insert(signSpot - 1, numberForPlacement)
            # puts it behind current element there
            for y in range(3):
                x.pop(signSpot + 2)
                signSpot -= 1

            signSpot = 0

    if '*' in x:
        x = MultiplicationArrow(x, returnBool)


    if returnBool == True:
        return x

def AdditionArrow(x, returnBool = False):
    count = 0
    signSpot = 0
    numberForPlacement = 0
    temporarySignSpot = 0
    numberOneNegative = 1
    numberTwoNegative = 1
    signCorrection = False
    numberList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    temporaryNumber = ""

    # it is -+1 because of the spacing between things
    for item in x:
        if item == '+':
            signSpot = count
        count += 1

        if signSpot > 0:


            numberOne = (x[signSpot - 1])
            numberTwo = (x[signSpot + 1])

            if str(numberOne)[0] == '-':
                numberOneNegative = -1
            elif x[signSpot - 2] == '-':
                numberOneNegative = -1
                signCorrection = True
            if str(numberTwo)[0] == '-':
                #when computer makes negatives, string statement can't detect it
                numberTwoNegative = -1
            if float(numberTwo) * -1 > 0 and float(numberTwo) > 0:
                #this is all experimental
                numberTwo = str(numberTwo)




                #because of the special case 5e+199 * -1 = 5e+199 according to this computer, I'll arrange it this way if
                #it is one of those cases.
                #input where this occurs: 1 + 2 * 76 - 0.5 * 100 ^ 100 - 2222
            if signCorrection == True:
                x.pop(signSpot-2)
                x.insert(signSpot-2, '+')

            #how do I make num2 negative in this case

            #if the first item of list(str()) of a number is not a number, it's a negative
            if (((float(x[signSpot - 1]) * numberOneNegative) + (float(x[signSpot + 1]) * numberTwoNegative)) > 0 and (float(x[signSpot - 1]) * numberOneNegative) + (float(x[signSpot + 1]) * numberTwoNegative) * -1 > 0):
                raise Exception("result of exponent caused stack overflow")

            numberForPlacement = (float(x[signSpot - 1]) * numberOneNegative) + (float(x[signSpot + 1]) * numberTwoNegative)

            x.insert(signSpot - 1, numberForPlacement)

            # puts it behind current element there
            for y in range(3):
                x.pop(signSpot + 2)
                signSpot -= 1

            signSpot = 0

    if '+' in x:
        x = AdditionArrow(x, returnBool)

    if returnBool == True:
        return x

def SubtractionArrow(x, returnBool = False):
    count = 0
    signSpot = 0
    numberForPlacement = 0
    temporarySignSpot = 0
    numberOneNegative = 1
    numberTwoNegative = 1
    signCorrection = False

    # it is -+1 because of the spacing between things
    for item in x:
        if item == '-':
            signSpot = count
        count += 1

        if signSpot > 0:
            numberOne = (x[signSpot - 1])
            numberTwo = (x[signSpot + 1])

            if str(numberOne)[0] == '-':
                numberOneNegative = -1
            elif x[signSpot - 2] == '-':
                numberOneNegative = -1
                signCorrection = True
            if str(numberTwo)[0] == '-':
                numberTwoNegative = -1
            if signCorrection == True:
                x.pop(signSpot - 2)
                x.insert(signSpot - 2, '+')

            if (((float(x[signSpot - 1]) * numberOneNegative) - (float(x[signSpot + 1]) * numberTwoNegative)) > 0 and (float(x[signSpot - 1]) * numberOneNegative) - (float(x[signSpot + 1]) * numberTwoNegative) * -1 > 0):
                raise Exception("result of exponent caused stack overflow")

            numberForPlacement = (float(x[signSpot - 1]) * numberOneNegative) - (float(x[signSpot + 1]) * numberOneNegative)

            x.insert(signSpot - 1, numberForPlacement)
            # puts it behind current element there
            for y in range(3):
                x.pop(signSpot + 2)
                signSpot -= 1

            signSpot = 0
            print(x)

    if '-' in x:
        x = SubtractionArrow(x, returnBool)

    if returnBool == True:
        return x

#temporary
StartingErrorCheck()
