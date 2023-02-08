# ターミナル立ち上げ　command+j
# 仮想環境の作成　python3 -m venv flask
# 仮想環境のアクティベート　source flask/bin/activate 
# 仮想環境にflaskをインストール　pip3 install flask
# 仮想環境にflaskがインストールできたか確認　import flask

# ↓flaskの雛形コード　簡単なWebページを作ってみる

# 必要なモジュールのインポート
from flask import Flask

# flaskをインスタンス化
app = Flask(__name__)

# ルートディレクトリ(＝URL に一番最初にアクセスした時に表示する場所)にアクセスがあった時の処理
# ルートディレクトリで指定したページには、最初に見せたい画面や Web サイトのトップページなどのページを書いていく
@app.route('/')
def hello():
    return 'Hello World'

# エントリーポイント
# sample.py ファイルを実行した時に、一番最初にエントリーポイントの中の app.run() が実行される時に URL へのアクセスに応じて実行される
if __name__ == '__main__':
    app.run()

