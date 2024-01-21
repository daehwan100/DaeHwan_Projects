# Project 4
> 대기질 및 날씨 데이터를 사용한 미세먼지 예측 모델
 
* 머신러닝 알고리즘 (LogisticRegression, KNN, DecisionTree, SVM)
  
* 앙상블 알고리즘 (RandomForest, AdaBoost, GradientBoost, XGBoost)

* 머신러닝과 앙상블 모델을 코딩을 통해 적용하여 깊은 이해 및 학습.

> 사용 프로그램 < Python >

## 기간

* 2023.04 - 2022.06

## 데이터

* 2020, 2021년도(24개월, 730일) 데이터 

* 하루에 726개 관측 지점 별 10분 단위
  
* 총 44개의 변수 (종속변수, 독립변수) 중 19개의 독립 변수를 지정.

  - <종속변수: 지면온도. 독립변수: 파랑 가시밴드, 이산화탄소 밴드, 수증기 밴드 등 19개>

* 독립변수의 관측 단위시간이 달랐기 때문에, 1시간 단위로 downsampling 후 분석 진행

* 시계열 데이터이므로 정상성 시계열인지 판단 위해 오차(yhat - y)로 ADF Test 진행

![image](https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/588e2543-a6d1-4795-8dc5-6303ac430548)
![image](https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/f32e1426-f42a-4d9d-a709-8ccfa3b3ec5d)


## 분석 알고리즘

* 머신러닝: SVR, KNR, LGBM, XGBoost

* 딥러닝: LSTM, GRU
* LSTM, GRU 알고리즘
  
![image](https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/c3fd4c29-b76c-4452-b351-9255546849cf)

* 시점을 이용한 make_dataset 알고리즘
  
![image](https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/87fda812-9557-485d-9548-ca49270681ae)


## 결론 및 한계점

* 하이퍼파라미터를 튜닝해가며 분석한 결과, 머신러닝 기법 중 SVR 모델이 성능이 가장 좋게 나왔고,
* 딥러닝 기법에서는 LSTM이 높게 나왔다.

* 하지만, 추세를 잘 찾지만 이상치 및 튀는 값에 대해서는 오차가 많이 났다는 한계가 있었음.









