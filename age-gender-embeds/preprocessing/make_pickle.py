#임포트
import pandas as pd
import numpy as np
import random
import os
import shutil
import glob
import pickle
import sys
import tensorflow as tf
from utils import load_csv_features
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

data_title='sum_wiki_4000+2000'
tar_name='sum_wiki_4000_mtc'
tar_age_dir=['20_24','25_29','30_34','35_39']
tar_remove_age=['40_44','45_49','50_54','55_59','60_64','65_69','70_']
#pickle저장 디렉토리 생성
def make_pickle():
    os.makedirs('/home/team/datasets/{}/pickle/{}'.format(data_title,tar_name), exist_ok=True)
    print('만들었다','/home/team/datasets/{}/pickle/{}'.format(data_title,tar_name))
    #이미지 개수 확인/ 나중에 맞는지 확인하기용
    age_111_len=[]
    age_112_len=[]
    for i in tar_age_dir:
        tmp_age_111=glob.glob('/home/team/datasets/{}/{}/{}/{}/*.png'.format(data_title,tar_name,str(111),i))
        tmp_age_112=glob.glob('/home/team/datasets/{}/{}/{}/{}/*.png'.format(data_title,tar_name,str(112),i))
        age_111_len.append(len(tmp_age_111))
        age_112_len.append(len(tmp_age_112))
        print(len(tmp_age_111))
        print(len(tmp_age_112))
    print('age_111_len = ',sum(age_111_len))
    print('age_112_len = ',sum(age_112_len))
    all_embeddings = list()
    label_strings=list()
    all_labels= list()
    for N in [111,112]:
        globals()['embedding_{}'.format(N)]=np.load("/home/team/datasets/{}/embeddings/{}/{}/embeddings.npy".format(data_title,tar_name,N))
        globals()['label_strings_{}'.format(N)]=np.load("/home/team/datasets/{}/embeddings/{}/{}/label_strings.npy".format(data_title,tar_name,N))
        globals()['labels_{}'.format(N)]=np.load("/home/team/datasets/{}/embeddings/{}/{}/labels.npy".format(data_title,tar_name,N))
        all_embeddings.append(globals()['embedding_{}'.format(N)])
        label_strings.append(globals()['label_strings_{}'.format(N)])
        all_labels.append(globals()['labels_{}'.format(N)])
    for i,gender in enumerate([111,112]):
        tmp=list()
        for row in all_embeddings[i]:
            tmp.append(row)
        df=pd.DataFrame(data={'embeddings' : tmp,
                            'age' : label_strings[i],})
        df['gender']=gender
        for tar in tar_remove_age:
            df_tmp=df[df['age']==tar].index 
            df=df.drop(df_tmp)

        for number in range(df.shape[0]) :
            age=df['age'][number]
            if df['gender'][number]==111: 
                with open('/home/team/datasets/{}/pickle/{}/{}&111&{}.pickle'.format(data_title,tar_name,age, number), 'wb') as ff:
                    pickle.dump(df['embeddings'][number], ff, pickle.HIGHEST_PROTOCOL)
            if df['gender'][number]==112: 
                with open('/home/team/datasets/{}/pickle/{}/{}&112&{}.pickle'.format(data_title,tar_name,age, number), 'wb') as f:
                    pickle.dump(df['embeddings'][number], f, pickle.HIGHEST_PROTOCOL)      
    all_pick=glob.glob('/home/team/datasets/{}/pickle/{}/*'.format(data_title,tar_name))
    print('pickle =',len(all_pick))

    print('img_111=',sum(age_111_len))

    print('img_112=',sum(age_112_len))

    print('img_sum = ',sum(age_111_len)+sum(age_112_len))
    # rm_111_age=[]
    # rm_112_age=[]
    # for i in tar_remove_age:
    #     tmp_age_111=glob.glob('/home/team/datasets/{}/{}/{}/{}/*.png'.format(data_title,tar_name,str(111),i))
    #     rm_111_age.append(len(tmp_age_111))
    #     tmp_age_112=glob.glob('/home/team/datasets/{}/{}/{}/{}/*.png'.format(data_title,tar_name,str(112),i))
    #     rm_112_age.append(len(tmp_age_112))


    # print('2',sum(rm_111_age)+sum(rm_112_age))
    # print('age_111_len = ',sum(age_111_len))
    # print('age_112_len = ',sum(age_112_len))

    # print('rm_111_age = ',sum(rm_111_age))
    # print('rm_112_age = ',sum(rm_112_age))