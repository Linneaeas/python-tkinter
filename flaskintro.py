from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return "<h1>Contact us!</h1>"

@app.route('/about')
def about():
    return "<h1>This is the about page</h1>"


if __name__ == '__main__':
    app.run(debug=True)
