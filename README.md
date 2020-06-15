#  Face Recognition, Age Gender Estimate 

## Face Recognition

매장을 방문하는 성별과 연령을 인공지능을 통해 판별하고 매출데이터와 엮어 데이터베이스에 적재합니다.
When Cunstomer visiting a store, We can restore Age, Gender data in the database that estimated by AI. That is effective way to get a sales improvment.

## Compatibility
Tensorflow 1.7 version, Ubuntu 16.04, python 3.5에서 테스트되었습니다. 또한 Facenet을 참조하였고 Pre-trained된 모델을 제공받았습니다.
The code is tested using Tensorflow 1.7 under Ubuntu 16.04 with Python 3.5. We refered to [Facenet](https://github.com/davidsandberg/facenet) and provided pre-trained model as well.

## Age Gender Estimate
ResNet-v1을 Output인 1x1x512의 vector(Representation)을 활용하여 나이와 성별을 분류하는 작업을 진행하였습니다.

## Datasets
To estimate Age, Gender, we had to get datasets which labeled with Age, Gender. So we refered to 4 datasets.
Supervised Learning을 위해 성별, 연령이 Labeling된 데이터셋이 필요하였습니다. 아래의 데이터셋을 Trian Datsets으로 사용하였습니다.

- [IMDB-Wiki Dataset](https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/)
- [AFAD-Datset](https://afad-dataset.github.io/)
- [UTKFace](https://susanqq.github.io/UTKFace/)

현재 데이터 셋은 품질자체가 좋지 않고 잘못된 labeling이 많이 있습니다. 또한 동양과 서양의 데이터 개수를 맞추지 않는다면 성별과 연령을 잘못 예측할 가능성이 있습니다. 가능하다면 Dummy Data를 걸러내는 작업을 진행하십시오.

## Database
- We are using Postgre-sql, and Django that is needed web. if you want to run this code for web, you should build database, Webcam first. if just code, don't need it. 
- Postgre-sql과 Django를 사용하여 웹을 구현하였습니다. 웹을 사용하신다면 먼저 데이터베이스와 Webcam을 설치하여야 합니다. 


## Pre-processing
얼굴을 Detecting하고 Alignment하는 Pre-preccessing에는 Facenet과 동일한 [Multi-task CNN](https://kpzhang93.github.io/MTCNN_face_detection_alignment/index.html)사용. 


## Example
사진 추가, 영상 추가

## Running training
Currently, the best results are achieved by training the model using softmax loss. Details on how to train a model using softmax loss on the CASIA-WebFace dataset can be found on the page [Classifier training of Inception-ResNet-v1](https://github.com/davidsandberg/facenet/wiki/Classifier-training-of-inception-resnet-v1) and .

