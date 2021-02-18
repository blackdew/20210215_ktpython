from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    with open("html/index.html", 'r', encoding='utf8') as f:
        html = f.read()
    return html

@app.route('/hello')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()