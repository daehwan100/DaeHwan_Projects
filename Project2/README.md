# Project 2 
> CNN을 활용한 점자문자 이미지 분석

* 점자문자 이미지 데이터(알파벳)를 CNN으로 학습하여 Classification 하는 모델
* CNN 알고리즘의 과적합 방지 및  최적화 하는 과정에 대해서 학습함. 

* 사용 프로그램 < Python >

## 기간

* 2022.04 - 2022.06

## 데이터

* Kaggle의 점자문자 이미지 데이터 셋

<img src="https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/4881c235-991b-496b-8574-807471187223.png" width="400" height="200"/>

## 데이터 증강
* CNN 성능을 높이기 위해 대비 및 색상, 흐림정도를 변경하여 데이터 개수를 10배수 늘림

<img src="https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/2016a91e-df1d-4351-9518-353f93895d40.png" width="400" height="200"/>

## 데이터셋 구성
* Test:Train:Validation = 15:15:70 으로 구성

## CNN 모델 구성
<img src="https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/09684cc6-2d25-437a-95f3-734db741dfec.png" width="400" height="200"/>

* Optimizer, epoch, batchsize, Dropout의 하이퍼파라미터를 튜닝하며 최적의 모델을 찾음

<img src="https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/10dcda50-078b-41a6-ae54-401e079240c8.png" width="400" height="200"/>

## 한계
* train, validation, test 데이터들을 높은 정확도로 끌어내었지만,
  비슷한 패턴의 점자문자 이미지들에서만 높은 성능을 보인다는 것.
* 그렇기 때문에 실생활에 사용에는 한정적인 것.
