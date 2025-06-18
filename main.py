from typing import Optional

from fastapi import FastAPI

from fastapi.responses import HTMLResponse #インポート

import random  # randomライブラリを追加

import copy    # copyライブラリを追加

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
            <title>HTML Returned!</title>
            <style>
                .marquee-wrapper {
                    width: 100%;
                    overflow: hidden;
                    background: #f0f0f0;
                    white-space: nowrap;
                }
                .marquee-wrapper:hover .marquee-text {
                    animation-play-state: paused;
                }
                .marquee-text {
                    display: inline-block;
                    padding-left: 100%; /* テキストを右端の外側に配置 */
                    animation: scroll-left 15s linear infinite;
                }
                .marquee-text p {
                    margin: 0;
                    padding: 0;
                    font-size: 1.2em;
                }
                /* 各速度クラスごとに異なる速度設定 */
                .slow {
                    animation: scroll-left 20s linear infinite;
                }
                .medium {
                    animation: scroll-left 10s linear infinite;
                }
                .fast {
                    animation: scroll-left 5s linear infinite;
                }

                @keyframes scroll-left {
                    0% {
                        transform: translateX(0%);
                    }
                    100% {
                        /* テキストが左端の外側まで移動したら消える */
                        transform: translateX(-100%);
                    }
                }
            </style>
        </head>
        <body>
            <h1>Scroll Texts with HTML!</h1>
            <div class="marquee-wrapper">
                <div class="marquee-text slow">
                    <p>のんびり歩くことも大切さ</p>
                </div>
                <div class="marquee-text medium">
                    <p>焦らずに一歩一歩着実に</p>
                </div>
                <div class="marquee-text fast">
                    <p>行けるところまで駆けていくよ！</p>
                </div>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/present")
async def give_present(request):
    charList_request = list(request)
    offer = copy.copy(charList_request)
    for i in range(len(charList_request)):
        offer[i] = charList_request[len(charList_request) - (i + 1)]
    response = "".join(offer)
    print(response)
    return {"response": f"サーバです。メリークリスマス！ {request}ありがとう。お返しは{response}です。"}  # f文字列というPythonの機能を使っている