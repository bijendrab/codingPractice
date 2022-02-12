'''
 *             CODERBYTE STRING EXPRESSION CHALLENGE            *
 *                                                              *
 * Problem Statement                                            *
 * Have the function StringExpression(str) read the str         *
 * parameter being passed which will contain the written out    *
 * version of the numbers 0-9 and the words "minus" or "plus" & *
 * convert the expression into an actual final number written   *
 * out as well.                                                 *
 * For example: if str is "foursixminustwotwoplusonezero" then  *
 * this converts to "46 - 22 + 10" which evaluates to 34 and    *
 * your program should return the final string threefour.       *
 * If your final answer is negative it should include the       *
 * word "negative."                                             *
 *                                                              *
 * Examples                                                     *
 * Input 1: "onezeropluseight"                                  *
 * Output 1: oneeight                                           *
 *                                                              *
 * Input 2: oneminusoneone                                      *
 * Output 2: negativeonezero                                    *
 *                                                              *
'''
import re


def getStringExpression(stringParam):
    numberToWords = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
                     'nine': 9, 'minus': '-', 'plus': '+'}
    wordsToNumber = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
                     9: 'nine'}
    count = 0
    position = 0
    expression = ""
    for i in range(len(stringParam) + 1):
        if count == 3 or count == 4 or count == 5:
            if numberToWords.get(stringParam[position:i]) is None:
                continue
            else:
                expression = expression + str(numberToWords[stringParam[position:i]])
                count = 0
                position = i
        count = count + 1

    expressionResult = sum(map(int, re.findall(r'[+-]?\d+', expression)))
    result = ""
    for i in range(len(str(expressionResult))):
        if str(expressionResult)[i] == "-":
            result = result + "negative"
        else:
            result = result + wordsToNumber[int(str(expressionResult)[i])]
    return result


if __name__ == "__main__":
    print(getStringExpression("foursixminustwotwoplusonezero"))
    print(getStringExpression("onezeropluseight"))
    print(getStringExpression("oneminusoneone"))
