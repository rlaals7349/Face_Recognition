# -*- coding: utf-8 -*- 
import os 
import glob
import numpy as np
import scipy
from PIL import Image
import cv2
import time
tarball = glob.glob("/home/team/datasets/tarball/MTCNN_AFAD-Full/*/*/*.png")
files = glob.glob("/home/team/datasets/tarball/MTCNN_AFAD-Full/*")

genders = ['111', '112']
ages = []

for age in files:
    age = age.split("/")[-1]
    ages.append(age)

ages = sorted(ages)

# 파일 개수 확인, shape 확인
def check_shape():
    UP160 = 0
    UP140 = 0
    UP120 = 0

    files = glob.glob("/home/team/datasets/tarball/AFAD-Full/*/*/*.jpg")

    for cnt, file in enumerate(files):
        if cnt%1000 == 0 :
            print(cnt, len(files))
        if cv2.imread(file).shape[0] >=160 and cv2.imread(file).shape[1] >= 160:
            # print("True")
            UP160 = UP160 + 1
        if cv2.imread(file).shape[0] >=140 and cv2.imread(file).shape[1] >= 140:
            # print("True")
            UP140 = UP140 + 1
        if cv2.imread(file).shape[0] >=120 and cv2.imread(file).shape[1] >= 120:
            # print("True")
            UP120 = UP120 + 1

    print("UP160, DOWN160", UP160, len(files)-UP160)
    print("UP140, DOWN140", UP140, len(files)-UP140)
    print("UP120, DOWN120", UP120, len(files)-UP120)
            
# check_shape()

def move_file():
    # 115529 개 걸러짐
    # files = glob.glob("/home/team/datasets/tarball/AFAD-Full/*/*/*.jpg") # ADAF - 162122
    files = glob.glob("/home/team/datasets/tarball/AFAD-Full/*/*/*.jpg") # UTKFace - 24106 --> 160x160 아닌 image 519개

    del_cnt = 0
    for num, file in enumerate(files):
        # print("이동시킬 파일 :", file)
        age = file.split("/")[-3]
        gender = file.split("/")[-2]
        # print(age, gender)
        if num%1000 == 0:
            print(num, "/", len(files))
        if cv2.imread(file).shape[0] >=100 and cv2.imread(file).shape[1] >= 100:
            
            if 20<=np.int8(age)<=24:
                os.system("cp {} /home/team/datasets/tarball/up160/20_24/{}_{}_{}.jpg".format(file, time.time(), age, gender))
            if 25<=np.int8(age)<=29:
                os.system("cp {} /home/team/datasets/tarball/up100/25_29/{}_{}_{}.jpg".format(file, time.time(), age, gender))
            if 30<=np.int8(age)<=34:
                os.system("cp {} /home/team/datasets/tarball/up100/30_34/{}_{}_{}.jpg".format(file, time.time(), age, gender))
            if 35<=np.int8(age)<=39:
                os.system("cp {} /home/team/datasets/tarball/up100/35_39/{}_{}_{}.jpg".format(file, time.time(), age, gender))
            if 40<=np.int8(age)<=44:
                os.system("cp {} /home/team/datasets/tarball/up100/40_44/{}_{}_{}.jpg".format(file, time.time(), age, gender))
            if 45<=np.int8(age)<=49:
                os.system("cp {} /home/team/datasets/tarball/up100/45_49/{}_{}_{}.jpg".format(file, time.time(), age, gender))
            if 50<=np.int8(age)<=54:
                os.system("cp {} /home/team/datasets/tarball/up100/50_54/{}_{}_{}.jpg".format(file, time.time(), age, gender))
            if 55<=np.int8(age)<=59:
                os.system("cp {} /home/team/datasets/tarball/up100/55_59/{}_{}_{}.jpg".format(file, time.time(), age, gender))
            if 60<=np.int8(age)<=64:
                os.system("cp {} /home/team/datasets/tarball/up100/60_64/{}_{}_{}.jpg".format(file, time.time(), age, gender))
            if 65<=np.int8(age)<=69:
                os.system("cp {} /home/team/datasets/tarball/up100/65_69/{}_{}_{}.jpg".format(file, time.time(), age, gender))
            if np.int8(age)>=70:
                os.system("cp {} /home/team/datasets/tarball/up100/70_/{}_{}_{}.jpg".format(file, time.time(), age, gender))
        else:
            del_cnt += 1
    print("저장된 파일 :", len(files)-del_cnt)
    print("실제 저장 된 파일 : ", len(glob.glob("/home/team/datasets/tarball/up100/*/*.jpg")))


def tarball_pickle_move_category():
    files = glob.glob("/home/team/datasets/tarball/tarball_pickle/*.pickle")

    for num, file in enumerate(files):
        # print("이동시킬 파일 :", file)
        age = np.uint8(file.split("/")[-1].split("_")[0])
        gender = np.uint8(file.split("/")[-1].split("_")[1])
        print(age, gender)
        if num%100 == 0:
            print(num, "/", len(files))

        if 20<=np.int8(age)<=24:
            os.system("mv {} /home/team/datasets/tarball/tarball_pickle/20_24/{}_{}_{}.png".\
            format(file, age, gender, file.split("/")[-1].split("_")[2].split(".")[0])) 
        
        if 25<=np.int8(age)<=29:
            os.system("mv {} /home/team/datasets/tarball/tarball_pickle/25_29/{}_{}_{}.png".\
            format(file, age, gender, file.split("/")[-1].split("_")[2].split(".")[0]))
        
        if 30<=np.int8(age)<=34:
            os.system("mv {} /home/team/datasets/tarball/tarball_pickle/30_34/{}_{}_{}.png".\
            format(file, age, gender, file.split("/")[-1].split("_")[2].split(".")[0]))
        
        if 35<=np.int8(age)<=39:
            os.system("mv {} /home/team/datasets/tarball/tarball_pickle/35_39/{}_{}_{}.png".\
            format(file, age, gender, file.split("/")[-1].split("_")[2].split(".")[0]))
        
        if 40<=np.int8(age)<=44:
            os.system("mv {} /home/team/datasets/tarball/tarball_pickle/40_44/{}_{}_{}.png".\
            format(file, age, gender, file.split("/")[-1].split("_")[2].split(".")[0]))
            
        if 45<=np.int8(age)<=49:
            os.system("mv {} /home/team/datasets/tarball/tarball_pickle/45_49/{}_{}_{}.png".\
            format(file, age, gender, file.split("/")[-1].split("_")[2].split(".")[0]))
        
        if 50<=np.int8(age)<=54:
            os.system("mv {} /home/team/datasets/tarball/tarball_pickle/50_54/{}_{}_{}.png".\
            format(file, age, gender, file.split("/")[-1].split("_")[2].split(".")[0]))
        
        if 55<=np.int8(age)>=59:
            os.system("mv {} /home/team/datasets/tarball/tarball_pickle/55_59/{}_{}_{}.png".\
            format(file, age, gender, file.split("/")[-1].split("_")[2].split(".")[0]))

        if 60<=np.int8(age)>=64:
            os.system("mv {} /home/team/datasets/tarball/tarball_pickle/60_64/{}_{}_{}.png".\
            format(file, age, gender, file.split("/")[-1].split("_")[2].split(".")[0]))

        if 65<=np.int8(age)>=69:
            os.system("mv {} /home/team/datasets/tarball/tarball_pickle/64_69/{}_{}_{}.png".\
            format(file, age, gender, file.split("/")[-1].split("_")[2].split(".")[0]))

        if np.int8(age)>=70:
            os.system("mv {} /home/team/datasets/tarball/tarball_pickle/70_/{}_{}_{}.png".\
            format(file, age, gender, file.split("/")[-1].split("_")[2].split(".")[0]))

def seperate_gender():

    files = glob.glob("/home/team/datasets/wiki_pre/*/*.jpg") # UTKFace - 24106 --> 160x160 아닌 image 519개

    for num, file in enumerate(files):
        age = file.split("_")[-2]
        gender = file.split("_")[-1].split(".")[0]
        # print(age, gender)
        if num%1000 == 0:
            print(num, "/", len(files))
        
        if np.int8(gender) == 0:

            if 20<=np.int8(age)<=24:
                os.system("mv {} /home/team/datasets/wiki_pre/111/20_24/{}_{}_{}.jpg".format(file, time.time(), age, gender))
            if 25<=np.int8(age)<=29:
                os.system("mv {} /home/team/datasets/wiki_pre/111/25_29/{}_{}_{}.jpg".format(file, time.time(), age, gender))
            if 30<=np.int8(age)<=34:
                os.system("mv {} /home/team/datasets/wiki_pre/111/30_34/{}_{}_{}.jpg".format(file, time.time(), age, gender))
            if 35<=np.int8(age)<=39:
                os.system("mv {} /home/team/datasets/wiki_pre/111/35_39/{}_{}_{}.jpg".format(file, time.time(), age, gender))
            if 40<=np.int8(age)<=44:
                os.system("mv {} /home/team/datasets/wiki_pre/111/40_44/{}_{}_{}.jpg".format(file, time.time(), age, gender))
            if 45<=np.int8(age)<=49:
                os.system("mv {} /home/team/datasets/wiki_pre/111/45_49/{}_{}_{}.jpg".format(file, time.time(), age, gender))
            if 50<=np.int8(age)<=54:
                os.system("mv {} /home/team/datasets/wiki_pre/111/50_54/{}_{}_{}.jpg".format(file, time.time(), age, gender))
            if 55<=np.int8(age)<=59:
                os.system("mv {} /home/team/datasets/wiki_pre/111/55_59/{}_{}_{}.jpg".format(file, time.time(), age, gender))
            if 60<=np.int8(age)<=64:
                os.system("mv {} /home/team/datasets/wiki_pre/111/60_64/{}_{}_{}.jpg".format(file, time.time(), age, gender))
            if 65<=np.int8(age)<=69:
                os.system("mv {} /home/team/datasets/wiki_pre/111/65_69/{}_{}_{}.jpg".format(file, time.time(), age, gender))
            if np.int8(age)>=70:
                os.system("mv {} /home/team/datasets/wiki_pre/111/70_/{}_{}_{}.jpg".format(file, time.time(), age, gender))

        if np.int8(gender) == 1:

            if 20<=np.int8(age)<=24:
                os.system("mv {} /home/team/datasets/wiki_pre/112/20_24/{}_{}_{}.jpg".format(file, time.time(), age, gender))
            if 25<=np.int8(age)<=29:
                os.system("mv {} /home/team/datasets/wiki_pre/112/25_29/{}_{}_{}.jpg".format(file, time.time(), age, gender))
            if 30<=np.int8(age)<=34:
                os.system("mv {} /home/team/datasets/wiki_pre/112/30_34/{}_{}_{}.jpg".format(file, time.time(), age, gender))
            if 35<=np.int8(age)<=39:
                os.system("mv {} /home/team/datasets/wiki_pre/112/35_39/{}_{}_{}.jpg".format(file, time.time(), age, gender))
            if 40<=np.int8(age)<=44:
                os.system("mv {} /home/team/datasets/wiki_pre/112/40_44/{}_{}_{}.jpg".format(file, time.time(), age, gender))
            if 45<=np.int8(age)<=49:
                os.system("mv {} /home/team/datasets/wiki_pre/112/45_49/{}_{}_{}.jpg".format(file, time.time(), age, gender))
            if 50<=np.int8(age)<=54:
                os.system("mv {} /home/team/datasets/wiki_pre/112/50_54/{}_{}_{}.jpg".format(file, time.time(), age, gender))
            if 55<=np.int8(age)<=59:
                os.system("mv {} /home/team/datasets/wiki_pre/112/55_59/{}_{}_{}.jpg".format(file, time.time(), age, gender))
            if 60<=np.int8(age)<=64:
                os.system("mv {} /home/team/datasets/wiki_pre/112/60_64/{}_{}_{}.jpg".format(file, time.time(), age, gender))
            if 65<=np.int8(age)<=69:
                os.system("mv {} /home/team/datasets/wiki_pre/112/65_69/{}_{}_{}.jpg".format(file, time.time(), age, gender))
            if np.int8(age)>=70:
                os.system("mv {} /home/team/datasets/wiki_pre/112/70_/{}_{}_{}.jpg".format(file, time.time(), age, gender))
        

seperate_gender()
# file_name = ["wiki_pre", "imdb_pre", "UTKFace", "tarball"]