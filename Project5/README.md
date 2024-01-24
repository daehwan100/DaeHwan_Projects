# Project 5 - 지상 기상 데이터를 활용한 지면온도 예측
> 2023 기상청 공모전

> 사용 프로그램 < Python(Colab, JupyterNotebook) >

* ML (MultiLinearRegression)

* Ensemble (RandomForest, GradientBoostRegression, XGBoostRegression, CatBoostRegression)
  
* GridSearch와 Optuna를 사용하여 Hyperparameter 튜닝을 통해 정확도 향상

* 지상기상 데이터를 ML & Ensemble 기법들로 코딩을 통해 분석 및 적용하고, 최적의 모델을 찾기 위해 비교해 봄

## Project Period

* 2023.06 - 2023.07

## Data

* 기상청 제공 데이터

* A년 ~ E년까지 총 5개년 데이터 약 43만개

* Spline Interpolation 기법을 통해 결측치 보간.

* 지점별로 4계절을 나누어 분석 진행

* 하루에 726개 관측 지점 별 10분 단위
  
* 총 44개의 변수 (종속변수, 독립변수) 중 19개의 독립 변수를 지정.

  - <종속변수: 지면온도. 독립변수: 년도, 월/일/시간, 지점번호, 기온, 풍속, 등 13개>


## Analysis Algorithm

* ML Algorithm (MultiLinearRegression)

* Ensemble Algorithm (RandomForest, GradientBoostRegression, XGBoostRegression, CatBoostRegression)

* 이 중 CatBoostRegression이 가장 높은 성능을 보였으며, MAE Score는 다음과 같음

![image](https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/514bc170-e38a-462e-a7e5-5337cb74cc03)

## Conclusion

* 봄과 가을의 경우 여름, 겨울보다 MAE Score가 더 낮았음
  - 이유는 여름 겨울의 이상치가 봄, 가을보다 많았기 때문임

* Catboost 모델의 정확도를 최대로 끌어올렸지만, 데이터 탐색 및 전처리 과정인 Interpolation 과정에서 성능이 갈렸다고 생각함
  - 결측치가 몰려있던 경우에 대해서 선형적으로 보간했다는 문제점이라 판단
    
* 이후, 이를 보완한 보간 방법인 NAOMI, BRITS를 학습할 수 있는 계기가 됨
  









