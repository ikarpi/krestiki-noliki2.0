from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    context = {
        "link": "Перейти по ссылке"
    }
    return render_template('about.html', **context)

@app.route('/about2')
def about2():
    context = {
        "link": "Посмотреть новость"
    }
    return render_template('about.html', **context)


if __name__ == '__main__':
    app.run()
