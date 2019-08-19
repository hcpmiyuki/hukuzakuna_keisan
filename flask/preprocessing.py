#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mojimoji
import re

def preprocessing(line):
    line = mojimoji.zen_to_han(line)
    line = line.replace(" ", "")
    return line

def validator(line):
    listed_line = list(line)
    num_pattern = ["0" ,"1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbol_pattern = ["+", "-", "*", "/"]
    kakko_pattern = [")", "("]
    l_kakko_count = 0
    r_kakko_count = 0
    for i in range(len(line)):
        # patternに含まれなかったらfalse
        if (not listed_line[i] in num_pattern) and (not listed_line[i] in symbol_pattern) and (not listed_line[i] in kakko_pattern):
            return "使用できない記号または数字以外の文字列が入力されています"
        # symbolが連続していたらfalse
        if i != 0 and (listed_line[i] in symbol_pattern) and (listed_line[i-1] in symbol_pattern):
            return "不正な入力です"

        if listed_line[i] in kakko_pattern:
            if listed_line[i] == "(":
                #開き括弧の前が数字だったら掛け算を省略して入力しているのでfalse
                if i != 0 and (listed_line[i-1] in num_pattern):
                    return "掛け算は省略できません"
                l_kakko_count += 1
            else:
                #閉じ括弧の後が数字だったら掛け算を省略しているのでfalse
                if i != (len(line)-1) and (listed_line[i+1] in num_pattern):
                    return "掛け算は省略できません"
                r_kakko_count += 1
    #左右の括弧の数が異なっていたらfalse
    if l_kakko_count != r_kakko_count:
        return "不正な入力です"

    return True
