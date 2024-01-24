# Project 4 - 대기질 및 기상 데이터를 사용한 미세먼지 예측 모델
> 사용 프로그램 < Python(JupyterNotebook) >

* ML (LogisticRegression, KNN, DecisionTree, SVM)
  
* Ensemble (RandomForest, AdaBoost, GradientBoost, XGBoost)

* 머신러닝과 앙상블 모델을 코딩을 통해 적용하여 깊은 이해 및 학습.

## Project Period

* 2023.04 - 2022.06

## Data

* AirKorea의 대기질 데이터, 기상자료개방포털의 기상에 대한 데이터

* 2019, 2020, 2021, 2022년도(24개월, 730일) 데이터, 31440개의 Row

* 하루에 726개 관측 지점 별 10분 단위
  
* 총 16개의 변수 (종속변수, 독립변수)

  - <종속변수: 미세먼지(PM10). 독립변수: 오존, 이산화질소, 기온, 강수량 등 15개>

* 1시간 단위로 분석 진행


## Analysis Algorithm

* ML 알고리즘 (LogisticRegression, KNN, DecisionTree, SVM)
  
* Ensemble 알고리즘 (RandomForest, AdaBoost, GradientBoost, XGBoost)


## Conclusion

* ML, Ensemble에 사용되는 Hyperparameter들이 성능 및 과적합에 어떤 영향을 주는지 파악할 수 있었음
* ML보다 Ensemble 기법들의 정확도가 다소 높았으며, 그 중 XGBoost의 정확도가 가장 높았음

* 적은 개수를 가진 범주에 대해서는 다소 아쉬운 정확도를 나타냈음
