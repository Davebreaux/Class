from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)

app.secret_key = 'ourn@fown6will2VUNG'

@app.route('/')
def index():
    if 'count_num' not in session:
        session['count_num'] = 0
    session['increase_by'] = 0
    session['count_num'] +=1
    if 'count_total' not in session:
        session['count_total'] = session['count_num']
    return render_template('index.html')

@app.route('/destroy_session')
def destroy_session():
    session.pop('count_num')
    session.pop('count_total')
    return redirect('/')

@app.route('/increment/<int:num>')
def increment(num):
    session['count_total'] += num
    return redirect('/')

@app.route('/submit_form',  methods=["POST"])
def submit_form():
    session['increase_by'] = request.form['increase_by']
    
    return redirect(f"/increment/{session['increase_by']}")


if __name__=="__main__":
    app.run(debug=True)