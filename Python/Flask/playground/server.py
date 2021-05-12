from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play_game():
    return render_template("play.html", times=3, color='blue')

@app.route('/play/<num>')
def play_num(num):
    return render_template("play.html", times=int(num), color='blue')

@app.route('/play/<num>/<bcolor>')
def play_color(num, bcolor):
    return render_template("play.html", times=int(num), color= bcolor)

if __name__=="__main__":
    app.run(debug=True)