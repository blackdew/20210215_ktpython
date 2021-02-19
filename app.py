from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

@app.route('/')
def index():
    title = "Welcome"
    content = "The World Wide Web (abbreviated WWW or the Web) is an information space where documents and other web resources are identified by Uniform Resource Locators (URLs), interlinked by hypertext links, and can be accessed via the Internet. English scientist Tim Berners-Lee invented the World Wide Web in 1989. He wrote the first web browser computer program in 1990 while employed at CERN in Switzerland. The Web browser was released outside of CERN in 1991, first to other research institutions starting in January 1991 and to the general public on the Internet in August 1991."
    return render_template('template.html', title=title, content=content)

@app.route('/html')
def html():
    title = "HTML"
    content = "Hypertext Markup Language (HTML) is the standard markup language for creating web pages and web applications. With Cascading Style Sheets (CSS) and JavaScript it forms a triad of cornerstone technologies for the World Wide Web.[2] Web browsers receive HTML documents from a web server or from local storage and render them into multimedia web pages. HTML describes the structure of a web page semantically and originally included cues for the appearance of the document."
    return render_template('template.html', title=title, content=content)

@app.route('/css')
def css():
    title = "CSS"
    content = "Cascading Style Sheets (CSS) is a style sheet language used for describing the presentation of a document written in a markup language.[1] Although most often used to set the visual style of web pages and user interfaces written in HTML and XHTML, the language can be applied to any XML document, including plain XML, SVG and XUL, and is applicable to rendering in speech, or on other media. Along with HTML and JavaScript, CSS is a cornerstone technology used by most websites to create visually engaging webpages, user interfaces for web applications, and user interfaces for many mobile applications."
    return render_template('template.html', title=title, content=content)

@app.route('/javascript')
def js():
    title = "Javascript"
    content = "JavaScript (/ˈdʒɑːvəˌskrɪpt/), often abbreviated as JS, is a high-level, dynamic, weakly typed, object-based, multi-paradigm, and interpreted programming language. Alongside HTML and CSS, JavaScript is one of the three core technologies of World Wide Web content production. It is used to make webpages interactive and provide online programs, including video games. The majority of websites employ it, and all modern web browsers support it without the need for plug-ins by means of a built-in JavaScript engine. Each of the many JavaScript engines represent a different implementation of JavaScript, all based on the ECMAScript specification, with some engines not supporting the spectrum fully, and with many engines supporting additional features beyond ECMA."
    return render_template('template.html', title=title, content=content)

@app.route('/movies')
def movie():
    return "hello movie 11111 2222"

if __name__ == '__main__':
    app.run()