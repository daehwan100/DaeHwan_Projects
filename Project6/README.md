# Project 6 - 실종 아동 Segmentation 및 Tracking 기반 CCTV 솔루션
> 2024 지능정보 SW 아카데미 경진대회
> 사용 프로그램 < Python(Colab, pycharm) >

* Segmentation: Segment Anything Model. SAM (2023)

* Tracking: XMem(2022)

* 위 두 모델을 사용하였고, 아동 CCTV 영상 데이터로 fine-tuning을 통해 성능 향상시킴

## Project Period

* 2023.10 - 2023.12

## Data & fine-tuning Process

* AI허브의 [어린이 보호구역 내 어린이 도로보행 위험행동 영상] 데이터

* DataPreprocessing.ipynb파일: 영상을 넣고, 프레임 단위를 지정하여 단위별로 프레임 추출하는 코드

* Fine_Tune_SAM.ipynb파일
  - 프레임별로 쪼개진 사진들을 불러오고, '사람'을 인식하기 위해 YOLOv8을 사용해 사람만 추출
  - 사람이 없는 이미지에 대해서는 저장 X
  - 나온 사람(아동)에 대해서 SAM_vit_huge를 사용하여 mask 진행
  - 진행된 이미지 데이터들은 ground_truth_mask로 지정
  - fine-tuning을 위해 데이터 사이즈 변경 (2160 * 3840) -> (1024 * 1024)
  - 약 2000장의 데이터 생성
    
<img src="https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/5d791b1d-33f0-472b-b78e-bb308e235c7f.png" width="400" height="200"/>

![image](https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/86063704-4ebd-444c-b4f4-50cb8c10e4da)

* 위와 같은 과정으로 진행

* IoU값을 가장 높게 만들기 위해 Hyperparameter(LearningRate, LossFunction, Optimizer)튜닝 

* Fine-Tuning된 가중치로 학습에 사용되지 않은 새로운 이미지를 넣었을 때, 약 0.85 이상의 IoU값들이 나오는 것을 확인
  
<img src="https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/e77aba82-1cef-425b-bbbb-9056215f8b34.png" width="400" height="200"/>

## Segmentation & Tracking Process

* Video Input -> Video Frame별로 Segmentation 진행 -> 원하는 객체를 Initialization(SAM) -> Tracking(XMem) -> Output
  
![image](https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/72a0f0e7-86d2-4287-ad7a-6ff346901fa4)




## Demonstration Video

https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/4d3bf3fa-1911-4230-8b9e-dcacad99207e

