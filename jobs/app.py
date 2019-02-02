from flask import Flask, render_template

app = Flask(__main__)

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.htlm')