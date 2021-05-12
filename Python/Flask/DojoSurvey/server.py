from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def dojo_survey():

    return render_template('index.html')

@app.route('/survey', methods=["POST"])
def survey_done():
    print(request.form)
    name = request.form['name']
    location = request.form['location']
    favorite_language = request.form['favorite_language']
    comments = request.form['comments']
    return render_template('survey.html', name = name, location = location, favorite_language = favorite_language, comments = comments)


if __name__=="__main__":
    app.run(debug=True)