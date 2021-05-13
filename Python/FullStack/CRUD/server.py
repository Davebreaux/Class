from flask import Flask, render_template, request, session, redirect
from random import randint
from myconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = 'afjafgjhaghaoihds[iaj;dsfja'

@app.route('/')
def index():
    mysql = connectToMySQL('first_flask')	        # call the function, passing in the name of our db
    friends = mysql.query_db('SELECT * FROM friends;')  # call the query_db function, pass in the query as a string
    print(friends)
    return render_template("index.html", friends = friends)

@app.route('/create_friend', methods = ['post'])
def create_friend():
    print(request.form)
    mysql = connectToMySQL('first_flask')

    query = "insert into friends(first_name, last_name, occupation) values (%(fn)s, %(ln)s, %(occ)s);"

    data = {
        "fn": request.form['fname'],
        "ln": request.form['lname'],
        "occ": request.form['occ']
    }

    new_friend_id = mysql.query_db(query, data)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)