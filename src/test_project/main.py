from flask import Flask, request, make_response, redirect, render_template


app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login')
def about():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug = True)

