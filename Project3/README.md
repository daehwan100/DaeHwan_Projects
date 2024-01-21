# Project 3
> 기상청 공모전
> 
> 기상 위성 자료를 활용한 지면온도 예측

* 머신러닝 알고리즘 (SVR, KNR, LGBM, XGBoost)

* 딥러닝 RNN 알고리즘 (LSTM, GRU)를 이용하여 분석 진행

* 사용 프로그램 < Python >

## 기간

* 2022.06 - 2022.07

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












