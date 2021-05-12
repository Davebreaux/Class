from flask import Flask
app = Flask(__name__)   
from flask import render_template

@app.route('/')          
def hello_world():
    return render_template('index.html', phrase='hello', times=5)  

@app.route('/dojo')
def dojo():
    return 'Dojo'

@app.route('/say/<phrase>')
def say_hi(phrase):
    if any(chr.isdigit() for chr in phrase):
        return 'That\'s not a word.'
    else:
        return f'Hi {phrase}!'


@app.route('/repeat/<num>/<word>')
def repeat(num, word):
    if num.isnumeric() and not any(chr.isdigit() for chr in word):
        number = int(num)
        word_repeat = ''
        for i in range(number):
            word_repeat += word
        return word_repeat
    else: 
        return 'invalid inputs'

@app.errorhandler(404)
def not_found(error):
    return 'Sorry! No response. Try again.'



if __name__=="__main__":     
    app.run(debug=True)    