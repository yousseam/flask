from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    #return render_template('home.html')
    return '<h1>Hello!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

if __name__ == '__main__':
    app.run(debug=True)