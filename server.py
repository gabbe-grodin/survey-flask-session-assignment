from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'lkjshfghekrhglkn897763i4ujt5dfjbiy987RE3MF0a94KiIetjnOgfb349867xcvb57689b8vn0fmx'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def submit_survey():
    print("Got Posted Survey Results:")
    print(f'NAME: ' + request.form['name'])
    print(f'DOJO: ' + request.form['dojo'])
    print(f'RATING: ' + request.form['score'])
    print(f'COMMENT: ' + request.form['comment'])
    print(f'NEXT SUBJECTS TO LEARN: ' + request.form['learnnext'])
    session['name'] = request.form['name']
    session['dojo'] = request.form['dojo']
    session['score'] = request.form['score']
    session['comment'] = request.form['comment']
    session['learnnext'] = request.form['learnnext']
    return redirect('/process')
    
@app.route('/process')
def process_survey():
    return render_template('result.html', name=session['name'], dojo=session['dojo'], score=session['score'], comment=session['comment'], learnnext=session['learnnext'])

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8000)