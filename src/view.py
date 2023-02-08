# viewファイルの実装

# coding: utf-8

# render_templateでtemplatesにあるファイルと繋げる
from flask import Flask, render_template

# appという変数で、Flaskクラスをインスタンス化
app = Flask(__name__)

# --- View側の設定 ---
# ルートディレクトリにアクセスした場合の挙動
@app.route('/')

# def 以下がアクセス後の操作
def index():
    # return 'Hello World!'
    return render_template('index.html')

# エントリーポイント
if __name__ == '__main__':
    app.run()

