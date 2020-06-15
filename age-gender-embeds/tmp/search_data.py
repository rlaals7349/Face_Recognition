# -*- coding: utf-8 -*- 
import os
import numpy as np
import glob
# use multi CPU
import time
from datetime import datetime
import pandas as pd
from scipy.io import loadmat

imdb_path = '/home/team/datasets/imdb_crop/*'
wiki_path = '/home/team/datasets/wiki_crop/*'
utk_path = '/home/team/datasets/UTKFace/'
tarball_path = '/home/team/datasets/tarball/AFAD-Full/*'
# print(os.listdir(imdb_path))

def get_meta(mat_path, db):
    if len(db)==2:
        meta = loadmat(mat_path[0])
        full_path = meta[db[0]][0, 0]["full_path"][0]
        dob = meta[db[0]][0, 0]["dob"][0]  # Matlab serial date number
        gender = meta[db[0]][0, 0]["gender"][0]
        photo_taken = meta[db[0]][0, 0]["photo_taken"][0]  # year
        face_score = meta[db[0]][0, 0]["face_score"][0]
        second_face_score = meta[db[0]][0, 0]["second_face_score"][0]
        age = [calc_age(photo_taken[i], dob[i]) for i in range(len(dob))]
        data = {"file_name": full_path, "gender": gender, "age": age, "score": face_score,
                "second_score": second_face_score}
        dataset1 = pd.DataFrame(data)

        meta = loadmat(mat_path[1])
        full_path = meta[db[1]][0, 0]["full_path"][0]
        dob = meta[db[1]][0, 0]["dob"][0]  # Matlab serial date number
        gender = meta[db[1]][0, 0]["gender"][0]
        photo_taken = meta[db[1]][0, 0]["photo_taken"][0]  # year
        face_score = meta[db[1]][0, 0]["face_score"][0]
        second_face_score = meta[db[1]][0, 0]["second_face_score"][0]
        age = [calc_age(photo_taken[i], dob[i]) for i in range(len(dob))]
        data = {"file_name": full_path, "gender": gender, "age": age, "score": face_score,
                "second_score": second_face_score}
        dataset2 = pd.DataFrame(data)
        dataset = pd.concat([dataset1,dataset2],axis=0)
    else:
        meta = loadmat(mat_path)
        full_path = meta[db][0, 0]["full_path"][0]
        dob = meta[db][0, 0]["dob"][0]  # Matlab serial date number
        gender = meta[db][0, 0]["gender"][0]
        photo_taken = meta[db][0, 0]["photo_taken"][0]  # year
        face_score = meta[db][0, 0]["face_score"][0]
        second_face_score = meta[db][0, 0]["second_face_score"][0]
        age = [calc_age(photo_taken[i], dob[i]) for i in range(len(dob))]
        data = {"file_name": full_path, "gender": gender, "age": age, "score": face_score,
                "second_score": second_face_score}
        dataset = pd.DataFrame(data)
    return dataset

def calc_age(taken, dob):
    birth = datetime.fromordinal(max(int(dob) - 366, 1))

    # assume the photo was taken in the middle of the year
    if birth.month < 7:
        return taken - birth.year
    else:
        return taken - birth.year - 1

def imdb():
    ages = []
    paths = glob.glob(imdb_path)
    for path in paths:
        age = path.split("/")[-1]
        if age == "wiki.mat":
            continue
        ages.append(int(age))
    return sorted(ages)

def wiki():
    ages = []
    paths = glob.glob(wiki_path)
    for path in paths:
        age = path.split("/")[-1]
        if age == "wiki.mat":
            continue
        ages.append(int(age))
    print(sorted(ages))

def tarball():
    ages = []
    paths = glob.glob(tarball_path)
    for path in paths:
        print(path)
        age = path.split("/")[-1]
        if age == "README.md" or age == "AFAD-Full.txt":
            continue
        ages.append(int(age))

    print(sorted(ages))
    return sorted(ages)

# 20_24, 24_29, 30_34, 35_39
# 40_44, 44_49, 50_54, 55_59

def mv_tarball_img():

    ages = tarball()
    genders = ["111","112"]
    count = 0

    for age in ages:
        if 20<=age<=60:
            print(age)
        for gender in genders:
            if gender == "111":
                for img in glob.glob("/home/team/datasets/tarball/AFAD-Full/{}/{}/*.jpg".format(age,int(gender))):
                    # print(img)
                    count = count + 1
                    print(count) #  os.system("mv /home/team/datasets/tarball/AFAD-Full/{}/{}/*.jpg /home/team/datasetes/total/20_24")
            if gender == "112":
                for img in glob.glob("/home/team/datasets/tarball/AFAD-Full/{}/{}/*.jpg".format(age,int(gender))):
                    # print(img)
                    count = count + 1
                    print(count)

def test():
    ages = imdb()
    genders = ["111","112"]
    count = 0
    for age in ages:
        if 20<=int(age)<=60:
            print(age)
        for gender in genders:
            if gender == "111":
                for img in glob.glob("/home/team/datasets/tarball/AFAD-Full/{}/{}/*.jpg".format(age,int(gender))):
                    # print(img)
                    count = count + 1
                    print(count) # 여기에 os.system("mv /home/team/datasets/tarball/AFAD-Full/{}/{}/*.jpg /home/team/datasetes/total/20_24")
            if gender == "112":
                for img in glob.glob("/home/team/datasets/tarball/AFAD-Full/{}/{}/*.jpg".format(age,int(gender))):
                    # print(img)
                    count = count + 1
                    print(count)


def check_img_num_per_directory(path):

    for tmp in glob.glob(path):
        print(tmp, len(glob.glob(tmp+"/*.jpg")))
    
print(len(glob.glob("/home/team/datasets/tarball/up160/*/*.jpg")))
print(len(glob.glob("/home/team/datasets/tarball/up140/*/*.jpg")))
print(len(glob.glob("/home/team/datasets/tarball/up120/*/*.jpg")))
