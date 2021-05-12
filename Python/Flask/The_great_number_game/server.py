from flask import Flask, render_template, request, session, redirect
from random import randint
app = Flask(__name__)
app.secret_key = 'afjafgjhaghaoihds[iaj;dsfja'



@app.route('/')
def index():
    if 'block_color' not in session:
        session['block_color'] = 'white'
    if 'message' not in session:
        session['message'] = ''
    if 'rand_num' not in session:
        session['rand_num'] = randint(1,100)
    print(session['rand_num'])
    return render_template('index.html', message = session['message'], color = session['block_color'])

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    if session['guess'] > session['rand_num']:
        session['message'] = f"Your guess of {session['guess']} is too high"
        session['block_color'] = 'red'
    elif session['guess'] < session['rand_num']:
        session['message'] = f"Your guess of {session['guess']} is too low"
        session['block_color'] = 'red'
    elif session['guess'] == session['rand_num']:
        session['message'] = f"You guessed {session['guess']}! That\'s correct!"
        session['block_color'] = 'green'
    session.modified = True
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('block_color')
    session.pop('message')
    session.pop('rand_num')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)