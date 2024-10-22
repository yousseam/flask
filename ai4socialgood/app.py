from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    #return render_template('templates/home.html')
    return "hello"

if __name__ == '__main__':
    app.run(debug=True) 