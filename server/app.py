#!/usr/bin/env python3

from flask import Flask

app = Flask(name)
@app.route('/')
def index():
    return  '<h1>Python Operations with Flask Routing and Views</h1>'
@app.route('/print/<string:text>')
def print_string(text):
    print(text)
    return text

@app.route('/count/<int:n>')
def count(n):
    numbers = ""
    for i in range(n):
        numbers += f"{i}\n"
    return numbers

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2) 
    elif operation == 'div':
        return str(num1 / num2)
    elif operation == '%':
        return str(num1 % num2)
    else:
        return 'Invalid operation'                           

if name == 'main':
    app.run(port=5555, debug=True)