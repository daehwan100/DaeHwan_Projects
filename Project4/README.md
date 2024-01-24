# Project 4 - 대기질 및 기상 데이터를 사용한 미세먼지 예측 모델
> 사용 프로그램 < Python(JupyterNotebook) >

* ML (LogisticRegression, KNN, DecisionTree, SVM)
  
* Ensemble (RandomForest, AdaBoost, GradientBoost, XGBoost)

* GridSearch를 사용하여 Hyperparameter 튜닝을 통해 정확도 향상

* 지상 기상 데이터를 ML & Ensemble 기법들로 코딩을 통해 분석 및 적용하고, 최적의 모델을 찾기 위해 비교해 봄

## Project Period

* 2023.04 - 2022.06

## Data

* **AirKorea**의 대기질 데이터, **기상자료개방포털**의 기상에 대한 데이터

* 2019, 2020, 2021, 2022년도(43개월, 1310일) 데이터, 31440개의 Row

* 하루에 726개 관측 지점 별 1시간 단위
  
* 총 16개의 변수 (종속변수, 독립변수)

  - <종속변수: 미세먼지(PM10). 독립변수: 오존, 이산화질소, 기온, 강수량 등 15개>


## Analysis Algorithm

* ML (LogisticRegression, KNN, DecisionTree, SVM)
  
* Ensemble (RandomForest, AdaBoost, GradientBoost, **XGBoost**)


## Conclusion

* ML, Ensemble에 사용되는 Hyperparameter들이 성능 및 과적합에 어떤 영향을 주는지 파악할 수 있었음
* ML보다 Ensemble 기법들의 정확도가 다소 높았으며, 그 중 XGBoost의 정확도가 가장 높았음

* 적은 개수를 가진 범주에 대해서는 다소 아쉬운 정확도를 나타냈음
