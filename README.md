#  Face Recognition, Age Gender Estimate using IoT

## Service
- 매장을 방문하는 성별과 연령을 인공지능을 통해 판별하고 매출데이터와 엮어 데이터베이스에 적재합니다.
- When Cunstomer visiting a store, We can restore Age, Gender data in the database that estimated by AI. That is effective way to get a sales improvment.


## Compatibility
- Tensorflow 1.7 version, Ubuntu 16.04, python 3.5에서 테스트되었습니다. 
- The code is tested using Tensorflow 1.7 under Ubuntu 16.04 with Python 3.5. 

## Face Recognition
- 얼굴 인식 모델은 [Facenet](https://github.com/davidsandberg/facenet)을 참조하였고 pre-trained model을 제공받았습니다.

- 한국인의 얼굴 인식률을 높이기 위해 Asian face dataset과 kface를 활용하여 가중치를 수정하는 transfer learning을 하였습니다.

- We refered to [Facenet](https://github.com/davidsandberg/facenet) and provided pre-trained model as well.

- We used transfer learning to improve recognition rate about Asian, so adjusted some weights from pre-trained model, using asian face, k-face datasets.

- asian face dataset is [here](http://trillionpairs.deepglint.com/overview)
- k-face dataset is [here](http://www.aihub.or.kr/aidata/73) ( if you want to use k-face dataset, you have to inform of project plan and submit kind of project discription. )


## Age Gender Estimate
- ResNet-v1을 거쳐 나오는 Output(Representation)을 활용하여 나이와 성별을 분류하는 작업을 진행하였습니다.

- We estimate Age, Gender, using the Representation that passed in the ResNet-v1 and have a 1x1x512 vector.

## Datasets
- Supervised Learning을 위해 성별, 연령이 Labeling된 데이터셋이 필요하였습니다. 아래의 데이터셋을 Trian Datsets으로 사용하였습니다.
- To estimate Age, Gender, we had to get datasets which labeled with Age, Gender. So we refered to 4 datasets.

- [IMDB-Wiki Dataset](https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/)
- [AFAD-Datset](https://afad-dataset.github.io/)
- [UTKFace](https://susanqq.github.io/UTKFace/)

- 현재 데이터 셋은 품질자체가 좋지 않고 잘못된 labeling이 많이 있습니다. 또한 동양과 서양의 데이터 개수를 맞추지 않는다면 성별과 연령을 잘못 예측할 가능성이 있습니다. 가능하다면 Dummy Data를 걸러내는 작업을 진행하십시오.

- There are some data which have low quality and mismatched label in datasets. Also you have to consider about quantity of each single class (because of data fairness or data bias) to estimate age, gender more effectively and high accuracy ratio. So it is needed that filter kind of dummy data i said and set the data of each class equally.

![AFAD-graph](https://user-images.githubusercontent.com/58922804/84971050-da89f700-b156-11ea-9297-15f2055142b8.png)
![imdb-wiki_grap](https://user-images.githubusercontent.com/58922804/84971054-df4eab00-b156-11ea-84f5-108f10ae8b23.png)

## Database
- We are using Postgre-sql, and Django for web service. if you want to run this code for web, you should build database, Webcam first. if just code, don't need it. 

- Postgre-sql과 Django를 사용하여 웹을 구현하였습니다. 웹을 사용하신다면 먼저 데이터베이스와 Webcam을 설치하여야 합니다. 


## Pre-processing
- 얼굴을 Detecting하고 Alignment하는 Preproccessing에는 [Facenet](https://github.com/davidsandberg/facenet)과 동일한 [Multi-task CNN](https://kpzhang93.github.io/MTCNN_face_detection_alignment/index.html)사용. 

- We used [Multi-task CNN](https://kpzhang93.github.io/MTCNN_face_detection_alignment/index.html) to detect and align the face(raw image) like [Facenet](https://github.com/davidsandberg/facenet)


## Example
![sample](https://user-images.githubusercontent.com/58922804/84972058-06a67780-b159-11ea-920d-15ca5a16bc49.png)

- 실제 서비스 페이지 링크는  [여기](https://github.com/euskate/face_recognition_web)서 확인할 수 있습니다.

- Example of Web service [here](https://github.com/euskate/face_recognition_web)

## Performance


