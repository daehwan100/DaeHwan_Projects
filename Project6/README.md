# Project 6
> 2024 지능정보 SW 아카데미 경진대회

> 실종 아동 Segmentation 및 Tracking 기반 CCTV 솔루션

* Segmentation: Segment Anything Model. SAM (2023)

* Tracking: XMem(2022)

* 아동 CCTV 영상 데이터로 fine-tuning을 통한 성능 향상

> 사용 프로그램 < Python(Colab, pycharm) >

## 기간

* 2023.10 - 2023.12

## 데이터 및 fine-tuning 과정

* AI허브의 [어린이 보호구역 내 어린이 도로보행 위험행동 영상] 데이터

* DataPreprocessing.ipynb파일: 영상을 넣고, 프레임 단위를 지정하여 단위별로 프레임 추출하는 코드

* Fine_Tune_SAM.ipynb파일
  - 프레임별로 쪼개진 사진들을 불러오고, '사람'을 인식하기 위해 YOLOv8을 사용해 사람만 추출
  - 나온 사람(아동)에 대해서 SAM_vit_huge를 사용하여 mask 진행
  - 진행된 이미지 데이터들은 ground_truth_mask로 지정
  - fine-tuning을 위해 데이터 사이즈 변경 (2160 * 3840) -> (1024 * 1024)
    
<img src="https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/5d791b1d-33f0-472b-b78e-bb308e235c7f.png" width="400" height="200"/>

![image](https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/86063704-4ebd-444c-b4f4-50cb8c10e4da)

* 위와 같은 과정으로 진행

* 학습률, 손실함수, Optimizer등의 하이퍼파라미터를 변경해가며 IoU값을 가장 높게 만듦

* 학습에 사용되지 않은 새로운 이미지를 넣었을 때, 약 0.85 이상의 IoU값들이 나오는 것을 확인
  
<img src="https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/e77aba82-1cef-425b-bbbb-9056215f8b34.png" width="400" height="200"/>

## 시연 영상

https://github.com/daehwan100/DaeHwan_Projects/assets/141620597/4d3bf3fa-1911-4230-8b9e-dcacad99207e

