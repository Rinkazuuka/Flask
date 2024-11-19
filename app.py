from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/mama')
def hello_mama():
    return '<b>Hello mama</b>'

@app.route('/image')
def image():
    return '<img src=https://images.immediate.co.uk/production/volatile/sites/63/2024/08/jaszczurka-zwinka-fot-iwona-kaluzinska-wikimedia-commons-cc-by-4-0-d5406d4.jpg>'

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'POST':
        return 'Użyto metody POST'
    else:
        return 'Użyto metody GET'

    
@app.route('/hello/<name>')
def hello_name(name):
    return f'Witaj, {name}!'

@app.route('/moja_liczba/<liczba>')
def moja_liczba(liczba):
    return f'Witaj, {int(liczba)+6}!'

@app.route('/podzielnosc/<liczba>')
def podzielnosc(liczba):
    if int(liczba) % 2 == 0 and int(liczba) % 3 == 0 and int(liczba) % 5 == 0: 
        return f'Liczba {liczba} jest podzielna przez 2,3 i 5'
    else:
        return f'Liczba {liczba} nie jest podzielna przez 2,3 i 5'
    
@app.route("/<name>/<name2>")
def hello_names(name, name2):
        return render_template('about.html', name=name, name2=name2)