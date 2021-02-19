from flask import Flask
app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

@app.route('/')
def index():
    with open("html/template.html", 'r', encoding='utf8') as f:
        txt = f.read()
        
    title = "Welcome"
    content = "The World Wide Web (abbreviated WWW or the Web) is an information space where documents and other web resources are identified by Uniform Resource Locators (URLs), interlinked by hypertext links, and can be accessed via the Internet. English scientist Tim Berners-Lee invented the World Wide Web in 1989. He wrote the first web browser computer program in 1990 while employed at CERN in Switzerland. The Web browser was released outside of CERN in 1991, first to other research institutions starting in January 1991 and to the general public on the Internet in August 1991."
    return txt.format(title, content)

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

@app.route('/movies')
def movie():
    return "hello movie 11111 2222"

if __name__ == '__main__':
    app.run()