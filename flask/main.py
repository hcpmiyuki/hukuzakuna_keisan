#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask,render_template,request
from calculator_tools import *
from preprocessing import *

app = Flask(__name__)

@app.route('/')
def top():
    # 全角を半角に、空白を削除する
    line = preprocessing(request.args.get('line', ''))
    
    # 不正な入力（記号の連続、数字と記号以外の入力等）を防ぐ
    if validator(line) == True:
        tokens = tokenize(line)
        preferentially_evaluated_token = prioritizeParentheses(tokens)
        answer = evaluateAll(preferentially_evaluated_token)
    else:
        answer = validator(line)
    return render_template('top.html', ans=answer)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
