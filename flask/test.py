#!/usr/bin/env python
# -*- coding: utf-8 -*-

from calculator_tools import *
from preprocessing import *

def test(line):
    line = preprocessing(line)
    tokens = tokenize(line)
    preferentially_evaluated_token = prioritizeParentheses(tokens)
    actualAnswer = evaluateAll(preferentially_evaluated_token)
    expectedAnswer = eval(line)
    if abs(actualAnswer - expectedAnswer) < 1e-8:
        print("PASS! (%s = %f)" % (line, expectedAnswer))
    else:
        print("FAIL! (%s should be %f but was %f)" % (line, expectedAnswer, actualAnswer))


# Add more tests to this function :)
def runTest():
    print("==== Test started! ====")
    test("1+ 3")
    test("1+2")
    test("1+2+2")
    test("1-2")
    test("1-2-3")
    test("1+2-3")
    test("1+2+3-9")
    test("1.0+2.0")
    test("1.0-2.0")
    test("1.3+1.5")
    test("1.4-1.3")
    test("1.3+1.4+1.7")
    test("1.5-2.8-3.9")
    test("1.3-5.4+4.5")
    test("2.3+4.9-5.6")
    test("2.34+39.4")
    test("8.59-3.53")
    test("9.58-3.45+3.544")

    test("1*2")
    test("1*2*2")
    test("1/2")
    test("1/2-3")
    test("1*2/3")
    test("1*2*3/9")
    test("1.0*2.0")
    test("1.0/2.0")
    test("1.3*1.5")
    test("1.4/1.3")
    test("1.3*1.4*1.7")
    test("1.5/2.8/3.9")
    test("1.3/5.4*4.5")
    test("2.3*4.9/5.6")
    test("2.34*39.4")
    test("8.59/3.53")
    test("9.58/3.45*3.544")

    test("1+4*3")
    test("1-4*3")
    test("1-4/2")
    test("1+4/2")
    test("1.0+4.0*3.0")
    test("1.0-4.0*3.0")
    test("1.0-4.0/2.0")
    test("1.0+4.0/2.0")
    test("1.2+4.2*3.2")
    test("1.2-4.2*3.2")
    test("1.3-4.3/2.3")
    test("1.4+4.4/2.4")

    test("3+4-5*3")
    test("3-4+5*3")
    test("4+5-5/2")
    test("4-5+5/2")
    test("4-5+5*2+4/2")
    test("4+5-5*2-4/2")
    test("5*2-4/2+4+5")
    test("5*2/6-10+1")
    test("6/2*3+10+1")

    test("3.0+4.3-5.3*30.3")
    test("3.3-4.333+35.3*333.3")
    test("4.6+5.33-5.44/332.4")
    test("44.4-5.2+5.22/222.4")
    test("4.33-5.2222+5444.3*233.55+2.44/44.20")
    test("43.4+5.44-5.44*2.333-3333.4/3.20")
    test("5*27-43.4/2.3+2.344+555.5")
    test("5.009*2.5/6.33-10.44+1.33")
    test("6003.4/2.3*33.3+10.33+1.3")

    test("(3.0+4.3-5.3)*30.3")
    test("(3.3-4.333)+35.3*333.3")
    test("4.6+(5.33-5.44)/332.4")
    test("(44.4-5.2+5.22)/222.4")
    test("(4.33-(5.2222+5444.3*233.55))+2.44/44.20")
    test("43.4+(5.44-5.44*2.333-3333.4)/3.20")
    test("5*27-(43.4/2.3+(2.344+555.5))")
    test("5.009*(2.5/6.33-(10.44+1.33))")
    test("6003.4/(2.3*(33.3+10.33)+1.3)")
    test("((3*1-4)+4/(3-7))")
    test("(3+1-((9*2-(2/2-3-0))))")

    print("==== Test finished! ====\n")

runTest()
