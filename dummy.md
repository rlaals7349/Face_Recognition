
```py
import os
import glob
import numpy as np


def get_meta_data():

    id_path = glob.glob('/home/team/datasets/kface/Midle_Resolution/*')
    clip_path = glob.glob('/home/team/datasets/kface/Midle_Resolution/19082742/*')
    lux_path = glob.glob('/home/team/datasets/kface/Midle_Resolution/19082742/S001/*')
    exp_path = glob.glob('/home/team/datasets/kface/Midle_Resolution/19082742/S001/L30/*')
    angle_path = glob.glob('/home/team/datasets/kface/Midle_Resolution/19082742/S001/L30/E01/*.jpg')

    id = []
    clip = []
    lux = []
    exp = []
    angle = []

    for id_ in id_path:
        id.append(id_.split("/")[-1])

    for clip_ in clip_path:
        clip.append(clip_.split("/")[-1])

    for lux_ in lux_path:
        lux.append(lux_.split("/")[-1])

    for exp_ in exp_path:
        exp.append(exp_.split("/")[-1])

    for angle_ in angle_path:
        angle.append(angle_.split("/")[-1])
    return id, clip, lux, exp, angle


# def count():

# id, clip, lux, exp, angle = get_meta_data()

num = 0
# id = all
# for i in id:
#     # clip = S001
#     for c in clip:
#         if c == 'S001':
#         # lux = L2
#             for l in lux:
#                 if l =='L2':
#                 # exp = all
#                     for e in exp:
#                         # angle = all
#                         for a in angle:
                                
#                             # num = num + 1
#                             # print(num)
#                             if e="E02":
#                                 a = 
#                                 pass
#                             if e="E03":
#                                 pass
#                             if os.path.isdir("/home/team/datasets/kface_selected") == False:
#                                 os.system("mkdir /home/team/datasets/kface_selected")
#                             if os.path.isdir("/home/team/datasets/kface_selected/{}".format(i)) == False:
#                                 os.system("mkdir /home/team/datasets/kface_selected/{}".format(i))
import random

id_path = glob.glob('/home/team/datasets/kface/selected_mtcnn_160_train/*')
# num = np.arange(0,120)
# print(num)
# print(id_path)
for id_ in id_path:
    
    idd = id_.split("/")[-1]
    if len(idd) != 8:
        continue
    print(idd, len(idd))
    # if os.path.isdir("/home/team/datasets/kface/selected_mtcnn_160_test/{idd}".format(idd)) == False:
        # os.system("mkdir /home/team/datasets/kface/selected_mtcnn_160_test/{idd}".format(idd))
    
    files = glob.glob('/home/team/datasets/kface/selected_mtcnn_160_train/{}/'.format(idd))
    print(files)
    choices = random.sample([1,2,3,4,5], 24)
    
    print(choices)
    # for choice in choices:
        # print(choice)
        # shutil.copy(choice, test_dir)
    # print ('Finished!')

    # os.system("mv /home/team/datasets/kface/selected_mtcnn_160_train/{}/ /home/team/datasets/kface/selected_mtcnn_160_test/".format(idd) )

    #####################################################################################################
```