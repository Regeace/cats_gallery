from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index')
def index():
    return render_template(template_name_or_list='index.html')


@app.route('/cats')
def cats():
    return render_template(template_name_or_list='cats_gallery.html')


app.run(host='localhost', port=8000)
