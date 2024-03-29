# Project 2 - CNN(Convolution Neural Network)을 활용한 점자문자 이미지 분석
> 사용 프로그램 < Python(Spyder) >

* 점자문자 이미지 데이터(알파벳)를 CNN(7개의 층)으로 학습하여 Classification 하는 모델
  
* CNN 알고리즘의 과적합 방지 및 최적화 하는 과정에 대해 직접 구현해보며 학습함

## Project Period

* 2022.04 - 2022.06

## Data

* Kaggle의 점자문자 이미지 데이터 셋

<img src="https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/4881c235-991b-496b-8574-807471187223.png" width="400" height="200"/>

## Data Augmentation
* CNN 성능을 높이기 위해 대비 및 색상, 흐림정도를 변경하여 데이터 개수를 10배수 늘림
* 총 11440개의 데이터

<img src="https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/2016a91e-df1d-4351-9518-353f93895d40.png" width="400" height="200"/>

## DataSet

* Train:Test:Validation = 72.25:15:12.25 으로 구성

## CNN Model

<img src="https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/09684cc6-2d25-437a-95f3-734db741dfec.png" width="400" height="200"/>

* 시행착오를 통해 위와 같은 CNN 구조가 가장 성능이 좋았음

* 또한 Optimizer, epoch, batchsize, Dropout의 Hyperparameter를 튜닝하며 성능, 시간적인 면에서 최적의 모델을 찾음

* Optimizer Adam, Epoch 10, Batchsize 128, Dropout 0.2

<img src="https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/10dcda50-078b-41a6-ae54-401e079240c8.png" width="400" height="200"/>

## Conclusion
* train, validation, test 데이터들에 대해 높은 정확도를 끌어내었음
  
* 하지만 비슷한 패턴의 점자문자 이미지들로만 학습하였기 때문에 높은 성능을 보였으므로, 실생활 사용에는 한계가 있음
