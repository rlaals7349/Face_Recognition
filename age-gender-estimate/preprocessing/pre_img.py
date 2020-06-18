#임포트
import pandas as pd
import numpy as np
import random
import os
import shutil
import glob
import pickle
# check_num_img(data_title,tar_name)
# get_img_by_num(tar_age_dir)
data_title='tarball'
tar_name='tarball_1000'
tar_age_dir=['20_24','25_29','30_34','35_39']
tar_remove_age=['40_44','45_49','50_54','55_59','60_64','65_69','70_']
####sum_img(data2_end_num,data1_title,data2_title,tar1_name,tar2_name,sav_dir,sav_tar)# 인자###
data2_end_num=1000
data1_title='sum_2000+2000'
data2_title='wiki'
tar1_name='sum_2000_mtc'
tar2_name='wiki_pre_mtc'
sav_dir = 'sum_wiki_4000+2000'
sav_tar = 'sum_wiki_4000_mtc'
path = '/home/team/datasets/'

# 이미지 개수확인
def check_num_img(data_title, tar_name):
    for i in tar_age_dir:
        print(i)
        print(len(glob.glob("/home/team/datasets/{}/{}/111/{}/*".format(data_title,tar_name,i))))
        print(len(glob.glob("/home/team/datasets/{}/{}/112/{}/*".format(data_title,tar_name,i))))
        print('###################')
#특정 데이터 셋에서 원하는 개수만큼 사진 가져오기 필요시 실행
def get_img_by_num(tar_age_dir,data_title,tar_name):
    for N in tar_age_dir:
        print("/home/team/datasets/{}/{}/{}/*_111.png".format(data_title,tar_name,N))
        globals()['AFAD_{}_111'.format(N)]=glob.glob("/home/team/datasets/{}/{}/{}/*_111.png".format(data_title,tar_name,N))
        globals()['AFAD_{}_0'.format(N)]=glob.glob("/home/team/datasets/{}/{}/{}/*_0.png".format(data_title,tar_name,N))
        globals()['AFAD_{}_112'.format(N)]=glob.glob("/home/team/datasets/{}/{}/{}/*_112.png".format(data_title,tar_name,N))
        globals()['AFAD_{}_1'.format(N)]=glob.glob("/home/team/datasets/{}/{}/{}/*_1.png".format(data_title,tar_name,N))
        globals()['AFAD_{}_111'.format(N)]=globals()['AFAD_{}_111'.format(N)]+globals()['AFAD_{}_0'.format(N)]
        globals()['AFAD_{}_112'.format(N)]=globals()['AFAD_{}_112'.format(N)]+globals()['AFAD_{}_1'.format(N)]
        random.shuffle(globals()['AFAD_{}_111'.format(N)])#셔플
        random.shuffle(globals()['AFAD_{}_112'.format(N)])#셔플
    #확인
    # for N in tar_age_dir:
    #     print('남 sum =',len(globals()['AFAD_{}_111'.format(N)][0:2000]))
    # print('여 sum =',len(globals()['AFAD_{}_112'.format(N)][0:2000]))
    # print('%%%%%%%%%%%%%%%%%%%%%')
    # print(AFAD_20_24_111[1])

    # print(AFAD_20_24_111[0])

    # print(AFAD_25_29_111[1])
    # print(AFAD_25_29_111[0])

    # print(AFAD_30_34_111[0])
    # print(AFAD_30_34_111[1])

    # print(AFAD_35_39_111[0])
    # print(AFAD_35_39_111[1])
    # print(len(AFAD_35_39_111[0:2000]))
    for i in tar_age_dir:
        tmp_111=globals()['AFAD_{}_111'.format(i)][0:2000]
        os.makedirs('/home/team/datasets/{}/{}/111/{}'.format(data_title,tar_name,i), exist_ok=True)
        tmp_112=globals()['AFAD_{}_112'.format(i)][0:2000]
        os.makedirs('/home/team/datasets/{}/{}/112/{}'.format(data_title,tar_name,i), exist_ok=True)
        print(type(tmp_111))
    for j in range(0,2000):
        os.system('cp {} /home/team/datasets/{}/{}/111/{}/'.format(tmp_111[j],data_title,tar_name,i))
        os.system('cp {} /home/team/datasets/{}/{}/112/{}/'.format(tmp_112[j],data_title,tar_name,i))
    for i in tar_age_dir:
        print(len(glob.glob('/home/team/datasets/{}/{}/112/{}/*.png'.format(data_title,tar_name,i))))

#원하는 개수 만큼 데이터셋 합치기
def sum_img(tar_age_dir,data2_end_num,data1_title,data2_title,tar1_name,tar2_name,sav_dir,sav_tar):
    for N in tar_age_dir:
        globals()['sum_{}_111'.format(N)]=list() #리스트 생성
        globals()['sum_{}_112'.format(N)]=list() #리스트 생성
        globals()['AFAD_{}_111'.format(N)]=glob.glob("/home/team/datasets/{}/{}/111/{}/*.png".format(data1_title,tar1_name,N))
        globals()['AFAD_{}_112'.format(N)]=glob.glob("/home/team/datasets/{}/{}/112/{}/*.png".format(data1_title,tar1_name,N))
        globals()['imdb_{}_111'.format(N)]=glob.glob("/home/team/datasets/{}/{}/111/{}/*.png".format(data2_title,tar2_name,N))
        globals()['imdb_{}_112'.format(N)]=glob.glob("/home/team/datasets/{}/{}/112/{}/*.png".format(data2_title,tar2_name,N))
        
    #     globals()['AFAD_{}_111'.format(N)]=globals()['AFAD_{}_111'.format(N)]+globals()['AFAD_{}_0'.format(N)]
    #     globals()['AFAD_{}_112'.format(N)]=globals()['AFAD_{}_112'.format(N)]+globals()['AFAD_{}_1'.format(N)]
        random.shuffle(globals()['AFAD_{}_111'.format(N)]) #셔플
        random.shuffle(globals()['AFAD_{}_112'.format(N)])
        random.shuffle(globals()['imdb_{}_111'.format(N)])
        random.shuffle(globals()['imdb_{}_112'.format(N)])
        globals()['sum_{}_111'.format(N)]=globals()['sum_{}_111'.format(N)] + globals()['AFAD_{}_111'.format(N)] #합치기
        globals()['sum_{}_112'.format(N)]=globals()['sum_{}_112'.format(N)] + globals()['AFAD_{}_112'.format(N)]
        globals()['sum_{}_111'.format(N)]=globals()['sum_{}_111'.format(N)] + globals()['imdb_{}_111'.format(N)][0:data2_end_num]
        globals()['sum_{}_112'.format(N)]=globals()['sum_{}_112'.format(N)] + globals()['imdb_{}_112'.format(N)][0:data2_end_num]
    for i in tar_age_dir:
        tmp_111=globals()['sum_{}_111'.format(i)]
        os.makedirs('/home/team/datasets/{}/{}/111/{}'.format(sav_dir,sav_tar,i), exist_ok=True)
        tmp_112=globals()['sum_{}_112'.format(i)]
        os.makedirs('/home/team/datasets/{}/{}/112/{}'.format(sav_dir,sav_tar,i), exist_ok=True)
        for j in range(0,len(tmp_111)):
            os.system('cp {} /home/team/datasets/{}/{}/111/{}/'.format(tmp_111[j],sav_dir,sav_tar,i))
        for j in range(0,len(tmp_112)):
            os.system('cp {} /home/team/datasets/{}/{}/112/{}/'.format(tmp_112[j],sav_dir,sav_tar,i))
    # for i in tar_age_dir:
# sum_img(data2_end_num,data1_title,data2_title,tar1_name,tar2_name,sav_dir,sav_tar)# 인자###


# check_num_img(data_title,tar_name)