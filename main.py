from typing import Optional

from fastapi import FastAPI

from fastapi.responses import HTMLResponse #インポート

import random  # randomライブラリを追加

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉！素晴らしい幸運が舞い込むでしょう。",
        "中吉！努力が実を結び、良い結果が待っています。",
        "小吉！ちょっとした幸運があなたの元にやってきます。",
        "吉！安定した幸せな日々が続くでしょう。",
        "半吉！まもなく転機が訪れるのかもしれません。",
        "末吉！努力が実り始め、良い方向に進む時期です。",
        "末小吉！これから良いことが舞い込んでくるでしょう。",
        "凶。悪いことが起こるかもしれませんが、気を引き締めてください。",
        "小凶。注意が必要な日です。慎重に行動しましょう。",
        "大凶。厳しい状況が訪れるかもしれませんが、乗り越えましょう。"
    ]
    
    return {"result" : omikuji_list[random.randrange(10)]}

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/present")
async def give_present(present):
    return {"response": f"サーバです。メリークリスマス！ {present}ありがとう。お返しはキャンディーです。"}  # f文字列というPythonの機能を使っている