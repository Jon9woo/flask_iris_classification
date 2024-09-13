from flask import Flask, render_template, request
import numpy as np
import pickle

# 1. ML 모델 메모리에 로딩
model_path = 'models/iris_model_svc.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)




# 플라스크 객체 생성
app = Flask(__name__)

# http://127.0.0.1:5000/
@app.route('/', methods=['GET','POST']) # 라우팅 경로 설정
def index():
    # 사용자 입력 데이터를 받아서 예측 수행
    ## 클라이언트에서 넘어온 요청이 re.quest == POST일 경우
    if request.method == 'POST':
        ## input으로 받은 4개의 데이터에서 value를 뽑기
        sl = float(request.form['sl'])
        sw = float(request.form['sw'])
        pl = float(request.form['pl'])
        pw = float(request.form['pw'])
        ## numpy 2D로 만들기
        data = np.array([[sl, sw, pl, pw]])
        ## 모델 예측 수행
        prediction_class = model.predict(data)[0]
        # 예측된 클래스 이름
        class_name = ['Setosa', 'Versicolor', 'Virginica'][prediction_class]
        img_path = f'static/{class_name.lower()}.jpg'
    
    ## 모델 예측수행 -> 결과 index.html에 랜더링
        return render_template('index_flask.html', predict=class_name, img_path=img_path) 

    ## 아니면 (클라이언트에서 넘어온 요청이 request == GET일 경우)
    ### 데이터 입력 페이지 처리(GET방식, default get임)
    return render_template('index_flask.html')
    

if __name__ == '__main__':
    app.run(host="127.0.0.1",port='5000',debug=True)