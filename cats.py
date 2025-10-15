from flask import Flask, render_template
from utils import form_contex

app = Flask(__name__)


# def form_contex(data: dict):
#     context = data
#     return context
# leader_score = max(context.values())[0]


@app.route('/index')
def index():
    """Страница для различных тестов."""
    return render_template(template_name_or_list='index.html')


@app.route('/cats')
def cats():
    """Базовая страница галереи с наполнением из различных баз данных."""
    context, connection, db_object = form_contex('cats.db', 'cats_db')
    leader_score = max([int(i[2]) for i in context])
    return render_template(template_name_or_list='cats_gallery.html', context=context, leader_score=leader_score)

if __name__ == '__main__':
    app.run(host='localhost', port=8000)
