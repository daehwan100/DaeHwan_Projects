# Project 1 - Bayesian Theory을 이용한 정규분포 데이터 예측 모델
> 사용 프로그램 < R >

* 정규분포를 따르는 분기별 공군 하의 수치 데이터를
베이지안 이론을 이용해 사후분포를 예측해 보았고,

* 빈도 주의 통계와 고전적 신뢰구간을 비교해 봄


## Project Period

* 2022.04 - 2022.06

## Data

* 국방부 공군 신체측정정보 (2021년 1분기, 2021년 2분기)
* 1분기 325개, 2분기 330개
  
  <img src="https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/c957b73a-5cb4-43ba-8788-06298ee38d18.png" width="400" height="200"/>

## Normality Test

* 왜도, 첨도 고려 후, 로그변환하여 Shapiro-Wilk 검정, Q-Q Plot을 통해 정규성 검정
* (H0 : F(x)는 정규분포이다. 
   H1 : F(x)는 정규분포가 아니다.)
* p-value = 0.5641로 귀무가설 채택 -> 정규성 만족>

<img src="https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/308c9ec5-636e-418e-9ab9-915692929208.png" width="400" height="200"/>

## Analysis Process

  - Bayesian Theory: 일어나지 않은 사건에 대한 확률(불확실성)을 사건과 관련있는 여러 확률을 사용해 추정하는 것

<img src="https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/2c7b7c23-c272-40e9-85a5-05c2321563c5.png" width="400" height="200"/>

---

<img src="https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/deaaea20-24e8-4fee-aafc-c35fdb826c73.png" width="400" height="200"/>

---

* 위 식을 이용한 예측 분포
<img src="https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/70377fed-da87-4c52-8356-da8fe37a560d.png" width="400" height="200"/>

<img src="https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/f0985eec-1e50-4013-bbe6-41f7104785d5.png" width="400" height="200"/>

---

### Comparison of HPD Interval and Confidence Interval
<img src="https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/80a17985-d0b9-40b9-b597-140a6d163c96.png" width="400" height="200"/>

## Conclusion

* 사전분포를 이용해 사후분포를 예측하는 과정, HPD Interval과 고전적 신뢰구간을 비교하는 과정을 코딩으로 직접 구현하여 더 깊은 이해가 가능했음
  
* 빈도주의 통계, 베이지안 통계에 대한 차이점을 알게 됨
