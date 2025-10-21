from flask import Flask, render_template, request, redirect, url_for
from utils import *

app = Flask(__name__)

context, connection, db_object, leader_score = None, None, None, None


@app.route('/index')
def index():
    """Страница для различных тестов."""
    return render_template(template_name_or_list='index.html')


@app.route('/')
def cats():
    """Базовая страница галереи с наполнением из различных баз данных."""
    global context, connection, db_object, leader_score
    context, connection, db_object = form_contex('cats.db', 'cats_db')
    leader_score = max([int(i[2]) for i in context])
    return render_template(template_name_or_list='cats_gallery.html', context=context, leader_score=leader_score)


@app.route('/change_score', methods=['POST'])
def change_score():
    data = request.get_json()
    element_id = data.get('id', '').strip()
    score_increment = int(data.get('score_increment', ''))
    update_score(db_object, element_id, connection, score_increment)
    return '', NO_CONTENT


@app.route('/send_comment', methods=['POST'])
def send_comment():
    data = request.get_json()
    element_id = data.get('id', '').strip()
    comment = data.get('comment', '').strip()
    if comment:
        print(element_id, comment)
        cats()
    return '', NO_CONTENT


if __name__ == '__main__':
    app.run(host='localhost', port=8000)
