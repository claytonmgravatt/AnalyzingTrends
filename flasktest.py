# -*- coding: utf-8 -*-
from flask import Flask,request,render_template
import time
app = Flask(__name__)

numberlist=[]


@app.route('/number/<first>')

def number(first):
    one = int(first)
    numberlist.append(one)

    return 'number is: ' +str(one)

@app.route('/numbers')

def numbers():
    return str(numberlist)


@app.route('/search/<number>')
def search(number):
    if int(number) == 1:
        return "Ooga"
    elif int(number) == 2:
        return "Booga"
    else:
        return "Ooga Booga"
    
@app.route('/')
def picture():
    message = 'Welcome!'
    return render_template('index.html',message=message)

@app.route('/form')
def my_form():
    return render_template('my_form.html')

@app.route('/form',methods=['Post'])
def my_form_post():
    text = request.form['text']
    size = request.form['size']
    processed_size = str(size)
    processed_text=text.upper()
    time.sleep(0)
    return render_template('return_form.html',processed_size=processed_size,processed_text=processed_text)

@app.route('/inputtest')
def myform():
    return render_template('my_form.html')

@app.route('/inputtest',methods=['Post'])
def input_post():
    text = request.form['text']
    size = request.form['size']
    return render_template('return_input.html',text=text)


if __name__ == "__main__":
    app.run(host="localhost", port=int("777"),debug=True,use_reloader=False)