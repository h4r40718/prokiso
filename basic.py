"""
ファイル構造

任意のファイル
|
| -templates(絶対このファイル名)
|   |-basic.html
|   |-basic2.html
|
basic.py

"""

from flask import Flask, request
from flask import render_template

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def stairs():
    if request.method == 'POST': #ここらへんの表記よくわかってない
       stairs = int(request.form['stairs']) # formのname = "stairs"を取得
       return render_template('basic2.html',stairs=stairs) # stairsが取得出来たらbasic2.htmlを表示
    else:
       return render_template('basic.html') # 最初はbasic.htmlが表示される