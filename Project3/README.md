# Project 3
> 기상청 공모전
> 
> 기상 위성 자료를 활용한 지면온도 예측

* 머신러닝 알고리즘 (SVR, KNR, LGBM, XGBoost 등)

* 딥러닝 RNN 알고리즘 (LSTM, GRU)를 이용하여 분석 진행

* 사용 프로그램 < Python >

## 기간

* 2022.06 - 2022.07

## 데이터

* 2020, 2021년도(24개월, 730일) 데이터 

* 하루에 726개 관측 지점 별 10분 단위
  
* 총 44개의 변수 (종속변수, 독립변수) 중 19개의 독립 변수를 지정.

* 독립변수의 관측 단위시간이 달랐기 때문에, 1시간 단위로 downsampling 후 분석 진행

* 시계열 데이터이므로 정상성 시계열인지 판단 위해 잔차(yhat - y)로 ADF Test 진행

* 

  <img src="https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/c957b73a-5cb4-43ba-8788-06298ee38d18.png" width="400" height="200"/>

## 정규성 검정

* 왜도, 첨도 고려 후, 로그변환하여 Shapiro-Wilk 검정, Q-Q Plot을 통해 정규성 검정
* (H0 : F(x)는 정규분포이다. 
   H1 : F(x)는 정규분포가 아니다.)
* p-value = 0.5641로 귀무가설 채택 -> 정규성 만족>

<img src="https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/308c9ec5-636e-418e-9ab9-915692929208.png" width="400" height="200"/>

## 분석 과정
<img src="https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/2c7b7c23-c272-40e9-85a5-05c2321563c5.png" width="400" height="200"/>

---

<img src="https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/deaaea20-24e8-4fee-aafc-c35fdb826c73.png" width="400" height="200"/>

---

* 위 식을 이용한 예측 분포
<img src="https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/70377fed-da87-4c52-8356-da8fe37a560d.png" width="400" height="200"/>

<img src="https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/f0985eec-1e50-4013-bbe6-41f7104785d5.png" width="400" height="200"/>

---

### HPD Interval과 고전적 신뢰구간의 비교
<img src="https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/80a17985-d0b9-40b9-b597-140a6d163c96.png" width="400" height="200"/>



