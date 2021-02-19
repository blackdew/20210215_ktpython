from flask import Flask, render_template
app = Flask(__name__, template_folder='templates', static_folder='style')
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

@app.route('/movies/<num>')
def movie(num):

    import datetime, requests, bs4

    def get_date(num=1):
        datalist = [datetime.date.today() - datetime.timedelta(7 * i) for i in range(num)]
        datalist = [d.strftime('%Y%m%d') for d in datalist]
        return datalist

    datelist = get_date(int(num))

    movies = []
    for d in datelist:
        url = f"https://movie.daum.net/boxoffice/weekly?startDate={d}"
        res = requests.get(url)

        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        tags = soup.select('.desc_boxthumb')

        movies += [{"날짜": d,
                "제목": tag.strong.a.get_text(),
                "평점": tag.em.get_text(),
                "관객수": tag.select('.list_state dd')[0].get_text(),
                "개봉일": tag.select('.list_state dd')[1].get_text()} for tag in tags]

    return render_template('movies.html', movies=movies)

@app.route('/daum')
def daum():
    import requests
    kt_logo = 'https://search3.kakaocdn.net/argon/0x200_85_hr/5t18mzjv1W'
    daum_logo = 'https://t1.daumcdn.net/daumtop_chanel/op/20200723055344399.png'

    res = requests.get('https://daum.net')
    return res.text.replace(daum_logo, kt_logo)

if __name__ == '__main__':
    app.run()