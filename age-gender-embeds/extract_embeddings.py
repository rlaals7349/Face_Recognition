import random
import os
import shutil
import glob  


for age in range(20,40):
    for gender in (111,112):
        os.makedirs('/home/team/datasets/tarball_sample/{}/{}'.format(age, gender), exist_ok=True)
        all_file=glob.glob('/home/team/datasets/tarball/MTCNN_AFAD-Full/{}/{}/*.png'.format(age,gender))
        random.shuffle(all_file)
        sample=all_file[0:1000]
        print(sample)
#         for N in f_111:
#             name=N.split('/')[-1]
# #             print(type(name))
#             shutil.copy('/home/team/tarball/MTCNN_AFAD-Full/{}/{}/{}'.format(i,j,name),'/home/team/tarball/20_39_1000/{}/{}/{}'.format(i,j,name))
            
# 1000장씩 잘라서 카피 하기

# #1000장 짜른거 확인 글롭으로
# for i in range(20,40):
#     a=len(glob.glob('/home/team/tarball/20_39_1000/{}/{}/*.png'.format(i,111)))
#     b=len(glob.glob('/home/team/tarball/20_39_1000/{}/{}/*.png'.format(i,112)))
#     print(a)
#     print('33333333333333333333333333')
#     print(b)
#     print('33333333333333333333333333')

# #불러오기
# #111 > 남자
# #112 > 여자
# all_emmbeddings = list()
# label_strings=list()
# all_labels= list()
# for N in range(20,40):
#     globals()['emmbeding_{}'.format(N)]=np.load("/home/team/test/export_embeddings/{}/embeddings.npy".format(N))
#     globals()['label_strings_{}'.format(N)]=np.load("/home/team/test/export_embeddings/{}/label_strings.npy".format(N))
#     globals()['labels_{}'.format(N)]=np.load("/home/team/test/export_embeddings/{}/labels.npy".format(N))
#     all_emmbeddings.append(globals()['emmbeding_{}'.format(N)])
#     label_strings.append(globals()['label_strings_{}'.format(N)])
#     all_labels.append(globals()['labels_{}'.format(N)])
# #폴더뎁스x
# columns=[]
# # (1100, 512) [ [embedding],[...],[...],[...],[...], ... ]
# for i,age in enumerate(range(20,40)):

#     tmp=list()
#     for row in all_emmbeddings[i]:
#         tmp.append(row)
#     df=pd.DataFrame(data={'embeddings' : tmp,
#                          'gender' : label_strings[i],})
    
#     for number in range(df.shape[0]) :

#         if df['gender'][number]=='111': 
#             with open('/home/team/test/dataset/{}_111_{}.pickle'.format(age, number), 'wb') as ff:
#                 pickle.dump(df['embeddings'][number], ff, pickle.HIGHEST_PROTOCOL)
#         if df['gender'][number]=='112': 
#             with open('/home/team/test/dataset/{}_112_{}.pickle'.format(age, number), 'wb') as f:
#                 pickle.dump(df['embeddings'][number], f, pickle.HIGHEST_PROTOCOL)  

# print(len(glob.glob('/home/team/test/dataset/*')))
# a=[]
# for i in range(20,40):
#     print(len(glob.glob('/home/team/test/dataset/{}_111_*'.format(i))))
#     a.append(len(glob.glob('/home/team/test/dataset/{}_111_*'.format(i))))
# sum(a)
    