from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    with open("html/index.html", 'r', encoding='utf8') as f:
        txt = f.read()
    return txt

@app.route('/1.html')
def html():
    with open("html/1.html", 'r', encoding='utf8') as f:
        txt = f.read()
    return txt

@app.route('/2.html')
def css():
    with open("html/2.html", 'r', encoding='utf8') as f:
        txt = f.read()
    return txt

@app.route('/3.html')
def js():
    with open("html/3.html", 'r', encoding='utf8') as f:
        txt = f.read()
    return txt

if __name__ == '__main__':
    app.run()