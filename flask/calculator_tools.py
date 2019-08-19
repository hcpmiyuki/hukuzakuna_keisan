#!/usr/bin/env python
# -*- coding: utf-8 -*

def readNumber(line, index):
    # string to number
    number = 0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.':
        index += 1
        keta = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * keta
            keta /= 10
            index += 1
    token = {'type': 'NUMBER', 'number': number}
    return token, index


def readPlus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1


def readMinus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1


def readMulti(line, index):
    token = {'type': 'MULTI'}
    return token, index + 1


def readDiv(line, index):
    token = {'type': 'DIV'}
    return token, index + 1


def readRParentheses(line, index):
    token = {'type': 'R_PARENTHESES'}
    return token, index + 1


def readLParentheses(line, index):
    token = {'type': 'L_PARENTHESES'}
    return token, index + 1


def multiplication(tokens, tmp, index):
    term = tmp['number']*tokens[index+1]['number']
    tmp = {'type': 'NUMBER', 'number': term}
    return tmp, index + 2


def division(tokens, tmp, index):
    term = tmp['number']/tokens[index+1]['number']
    tmp = {'type': 'NUMBER', 'number': term}
    return tmp, index + 2


def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit(): (token, index) = readNumber(line, index)
        elif line[index] == '+': (token, index) = readPlus(line, index)
        elif line[index] == '-': (token, index) = readMinus(line, index)
        elif line[index] == '*': (token, index) = readMulti(line, index)
        elif line[index] == '/': (token, index) = readDiv(line, index)
        elif line[index] == ')': (token, index) = readRParentheses(line, index)
        elif line[index] == '(': (token, index) = readLParentheses(line, index)
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens


# multiplication, division
def evaluateMD(tokens):
    tmp = {'type': 'PLUS'}
    md_tokens = []
    index = 0
    while index < len(tokens):
        if tokens[index]['type'] == 'MULTI':
            (tmp, index) = multiplication(tokens, tmp, index)
        elif tokens[index]['type'] == 'DIV':
            (tmp, index) = division(tokens, tmp, index)
        else:
            md_tokens.append(tmp) # ひとつ前に保存したtoken
            tmp = tokens[index] # 現在のtokenに更新
            index += 1
    md_tokens.append(tmp)
    return md_tokens


# addition, subtraction
def evaluateAS(tokens):
    answer = 0
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print('Invalid syntax')
                exit(1)
        index += 1
    return answer


def evaluateAll(tokens):
    md_tokens = evaluateMD(tokens)
    answer = evaluateAS(md_tokens)
    return answer


# calculate in parentheses preferentially
def prioritizeParentheses(tokens):
    b_index = len(tokens) - 1
    f_index = 0
    #  search 'L_PARENTHESES' from the end of the list
    while b_index >= 0:
        if tokens[b_index]['type'] == 'L_PARENTHESES':
            f_index = b_index
             #  search 'R_PARENTHESES' from the index where 'L_PARENTHESES' was found
            while f_index < len(tokens):
                if tokens[f_index]['type'] == 'R_PARENTHESES':
                    # calculate in parentheses
                    answer_in_parentheses = evaluateAll(tokens[b_index+1:f_index])
                    tokens[b_index] = {'type': 'NUMBER', 'number': answer_in_parentheses}
                    # delete tokens[b_index+1:f_index+1]
                    for i in range(b_index+1, f_index+1):
                        tokens.pop(b_index+1)
                    break
                f_index += 1
        b_index -= 1
    return tokens
