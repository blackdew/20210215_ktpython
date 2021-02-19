from flask import Flask, render_template, request, redirect
app = Flask(__name__, template_folder='templates', static_folder='style')
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

@app.route('/')
def index():
    title = "Welcome"
    content = "The World Wide Web (abbreviated WWW or the Web) is an information space where documents and other web resources are identified by Uniform Resource Locators (URLs), interlinked by hypertext links, and can be accessed via the Internet. English scientist Tim Berners-Lee invented the World Wide Web in 1989. He wrote the first web browser computer program in 1990 while employed at CERN in Switzerland. The Web browser was released outside of CERN in 1991, first to other research institutions starting in January 1991 and to the general public on the Internet in August 1991."

    import os 
    menus = os.listdir('content')

    return render_template('template.html', title=title, content=content, menus=menus)

@app.route('/<title>')
def content(title):
    import os 
    menus = os.listdir('content')
    
    with open(f'content/{title}', 'r', encoding='utf8') as f:
        content = f.read() 
    return render_template('template.html', title=title, content=content, menus=menus)

@app.route('/create', methods=['get', 'post'])
def create():
    import os 
    menus = os.listdir('content')

    if request.method == 'GET':
        return render_template('create.html', menus=menus)
    else:
        return redirect('/')
    

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