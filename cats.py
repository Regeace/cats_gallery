from flask import Flask, render_template
from utils import *

app = Flask(__name__)


def form_contex(data: dict):
    context = data
    return context

@app.route('/index')
def index():
    """Страница для различных тестов."""
    return render_template(template_name_or_list='index.html')


@app.route('/cats')
def cats():
    """Базовая страница галереи с наполнением из различных баз данных."""
    context = form_contex(CATS_DB)
    leader_score = max(context.values())[0]
    return render_template(template_name_or_list='cats_gallery.html', context=context, leader_score=leader_score)


app.run(host='localhost', port=8000)
