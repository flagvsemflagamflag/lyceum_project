#когда-нибудь я сделаю эту штуку красивой. Наверное.

from flask import Flask, request, url_for, render_template, redirect
from loginform import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/', methods=['POST', 'GET'])
@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return render_template('new.html')

    elif request.method == 'POST':
        first = float(request.form['first'])
        second = float(request.form['second'])
        what_to_do = request.form['what_to_do']
        if what_to_do == '+':
            answer = first + second
        elif what_to_do == '-':
            answer = first - second
        elif what_to_do == '•':
            answer = first * second
        elif what_to_do == ':':
            if second != 0:
                answer = first / second
        elif what_to_do == '^':
            if not(first == 0 and second == 0):
                answer = first ** second
        if answer == int(answer):
            answer = int(answer)
        return render_template('new.html', answer=answer, first=first, second=second, what_to_do=what_to_do)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
