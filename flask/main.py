#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask,render_template,request
from calculator_tools import *
from preprocessing import *

app = Flask(__name__)

@app.route('/')
def top():
    line = preprocessing(request.args.get('line', ''))

    if validator(line) == True:
        tokens = tokenize(line)
        preferentially_evaluated_token = prioritizeParentheses(tokens)
        answer = evaluateAll(preferentially_evaluated_token)
    else:
        answer = validator(line)
    return render_template('top.html', ans=answer)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
