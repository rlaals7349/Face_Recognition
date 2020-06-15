import pickle
import glob
import numpy as np
import sys
import os
# from random import shuffle
import tensorflow as tf
from utils import load_csv_features
import pandas as pd
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

def read_all(data_path):
	addrs = np.array(glob.glob(data_path)) # 16만
	# print(len(addrs))
	
	age_labels = np.array([(addr.split('/')[-1].split('&')[0]) for addr in addrs]) # 16만
	# print("age_labels :", age_labels, "len :", len(age_labels), "type : ", type(age_labels), "shape :", age_labels.shape)
	# print(age_labels[0], type(age_labels[0]))
	
	gender_labels = np.array([(addr.split('/')[-1].split('&')[1].split('.')[0]) for addr in addrs]) # 16만
	# print("gender_labels :", gender_labels, "len :", len(gender_labels), "type :", type(gender_labels))

	return [addrs, age_labels, gender_labels]

# convert to tensorflow function
def _int64_feature(value):
	return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))

def _bytes_feature(value):
	return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))

def _floats_feature(value):
	return tf.train.Feature(float_list=tf.train.FloatList(value=value))

def save_to_tfrecords(outpath, addrs, age_labels, gender_labels):
	writer = tf.python_io.TFRecordWriter(outpath)
	count = 0
	for i in range(len(addrs)): # 40개 [(20_111),(20_112).....(39_112)]
			
		with open(addrs[i], 'rb') as f:
			embedding = pickle.load(f)
		age = np.str(age_labels[i])
		if age == '20_24':
			age=np.array(0)
		if age == '25_29':
			age=np.array(1)
		if age == '30_34':
			age=np.array(2)
		if age == '35_39':
			age=np.array(3)
		
		if gender_labels[i]=='111':
			gender = np.str_(0)
		else :
			gender = np.str_(1)
		print("age=", age, "gender = ", gender)
		count = count + 1
		print("count =", count)

	# Create a feature
		feature = {'age': _int64_feature(age.astype(np.int8)),
							'gender': _int64_feature(gender.astype(np.int8)),
							'features': _floats_feature(embedding),
							'file_name': _bytes_feature(os.path.basename(addrs[i].encode()))}

	# Create an example protocol buffer
		example = tf.train.Example(features=tf.train.Features(feature=feature))
		# Serialize to string and write on the file
		writer.write(example.SerializeToString())
	print(count)
	writer.close()
	sys.stdout.flush()

def shuffle_data(data):
	# 0=addrs, 1=age_labels, 2=gender_labels
	# print('addresses', data[0].shape)
	# print('age_labels', data[1].shape)
	# print('gender_labels', data[2].shape)
	c = list(zip(data[0], data[1], data[2]))
	shuffle(c)
	addrs, age_labels, gender_labels = zip(*c)
	return [addrs, age_labels, gender_labels]

if __name__ == '__main__':
	test_addrs = []
	test_ages = []
	test_genders =[] 

	train_addrs = []
	train_ages = []
	train_genders =[] 
	data_title='sum_wiki_4000+2000'
	tar_name='sum_wiki_4000_mtc'
	tar_age_dir=['20_24','25_29','30_34','35_39']
	tar_remove_age=['40_44','45_49','50_54','55_59','60_64','65_69','70_']
	os.mkdir('/home/team/datasets/{}/tfrecords'.format(data_title))
	cnt = 0
	df = None
	for i in tar_age_dir:
		for j in range(111,113):
			cnt = cnt + 1
			# data_path = [1000개]
			data_path = '/home/team/datasets/{}/pickle/{}/{}&{}&*.pickle'.format(data_title,tar_name,i,j)
			
			addrs, age_labels, gender_labels = read_all(data_path)
			
			

			globals()['train_{}_{}'.format(i,j)] = pd.DataFrame({"addrs":addrs, "ages":age_labels, "genders":gender_labels})
			
			if cnt == 8:
				df = pd.concat([train_20_24_111, train_20_24_112, train_25_29_111, train_25_29_112, \
								train_30_34_111, train_30_34_112, train_35_39_111, train_35_39_112], ignore_index = True)
			
			# break
		# break
	df = shuffle(df)
	df.reset_index()
	print(len(df))
	size=int(len(df)*0.2)

	test_addrs   = tuple(df['addrs'][:size])
	test_ages    = tuple(df['ages'][:size])
	test_genders = tuple(df['genders'][:size])

	train_addrs  = tuple(df['addrs'][size:])
	train_ages   = tuple(df['ages'][size:])
	train_genders =tuple(df['genders'][size:])


	save_to_tfrecords('/home/team/datasets/{}/tfrecords/{}_train.tfrecords'.format(data_title,tar_name), train_addrs, train_ages, train_genders)

	save_to_tfrecords('/home/team/datasets/{}/tfrecords/{}_test.tfrecords'.format(data_title,tar_name), test_addrs, test_ages, test_genders)

	print(len(test_addrs))
	print(len(train_addrs))