from flask import Flask, render_template
import numpy as np
import pickle


# 플라스크 객체 생성
app = Flask(__name__)

# http://127.0.0.1:5000/
@app.route('/', methods=['GET','POST']) # 라우팅 경로 설정
def index():
    aaa = "헬로 플라스크"
    bbb = "static/setosa.jpg"
    print(aaa)
    # render_template() 함수로 index.html 파일을 렌더링한 후에 return하는 순서로 진행
    return render_template('index_v1.html', predict=aaa, img_path=bbb) # aaa 변수를 index2.html로 전달, bbb 변수를 index2.html로 전달
    

if __name__ == '__main__':
    app.run(host="127.0.0.1",port='5000',debug=True)