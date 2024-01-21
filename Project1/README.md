# Project 1
> 베이지안 이론을 이용한 정규분포 데이터 예측 모델

* 정규분포를 따르는 분기별 공군 하의 수치 데이터를
베이지안 이론을 이용해 사후분포를 예측해보았음.

* 사용 프로그램 < R >

## 기간

* 2022.04 - 2022.06

## 데이터

* 국방부 공군 신체측정정보 (2021년 1분기, 2021년 2분기)

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


