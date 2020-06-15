# -*- coding: utf-8 -*- 
from multiprocessing import Process
import os
import glob
dir_name='sum_wiki_4000+2000'
name='sum_wiki_4000_mtc'
data_dir=glob.glob('/home/team/datasets/{}/{}/*'.format(dir_name,name))
def make(N):
    os.makedirs('/home/team/datasets/{}/embeddings/{}/{}'.format(dir_name,name,N), exist_ok=True)
    os.system(r'''python /home/team/facenet/contributed/export_embeddings.py --model_dir /home/team/facenet/models/20180402-114759/20180402-114759.pb --data_dir /home/team/datasets/{2}/{0}/{1}/ --margin 32 --gpu_memory_fraction 0.25 --embeddings_name /home/team/datasets/{2}/embeddings/{0}/{1}/embeddings.npy --labels_name /home/team/datasets/{2}/embeddings/{0}/{1}/labels.npy --labels_strings_name /home/team/datasets/{2}/embeddings/{0}/{1}/label_strings.npy'''.format(name,N,dir_name))

procs = []
for N in [112]:    
    proc = Process( target=make, args=(N,))
    procs.append( proc )
    proc.start()

for p in procs:
    proc.join()