import facenet
import numpy as np
import tensorflow as tf
import os
from scipy import misc
from os import path
from PIL import Image 

facenet_model_checkpoint = '/home/team/models/20180402-114759' #모델
model_path = "/home/team/facenet_master/age-gender-embeds/frozen.pb"
# model_path = '/home/team/facenet/models/20180402-114759/20180402-114759.pb'

path = "/home/team/datasets/kface/selected_mtcnn_160/19062421/S001L2E01C10.png" # 이미지
im = Image.open(path)  
image=np.array(im)

def prewhiten(x):
    mean = np.mean(x)
    std = np.std(x)
    std_adj = np.maximum(std, 1.0/np.sqrt(x.size))
    y = np.multiply(np.subtract(x, mean), 1/std_adj)
    return y

class Encoder:
    def __init__(self):
        self.sess = tf.Session()
        with self.sess.as_default():
            facenet.load_model(facenet_model_checkpoint) # 모델이 들어간다.

    def generate_embedding(self, face):
        # Get input and output tensors
        images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
        embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")
        phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")

        prewhiten_face = prewhiten(image)# 배열로 바뀐 image가 들어감 (160, 160, 3)
        print(prewhiten_face, prewhiten_face.shape)
        print(image.shape)
        # Run forward pass to calculate embeddings
        feed_dict = {images_placeholder: [prewhiten_face], phase_train_placeholder: False}
        return self.sess.run(embeddings, feed_dict=feed_dict)[0]

def load_graph(frozen_graph_filename):
    # We load the protobuf file from the disk and parse it to retrieve the 
    # unserialized graph_def
    with tf.gfile.GFile(frozen_graph_filename, "rb") as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())

    # Then, we import the graph_def into a new Graph and returns it 
    with tf.Graph().as_default() as graph:
        # The name var will prefix every op/nodes in your graph
        # Since we load everything in a new graph, this is not needed
        tf.import_graph_def(graph_def, name="")
    return graph

def run(features, model_path):
    #모델 받는곳
    graph = load_graph(model_path)
    
    with tf.Session(graph=graph) as sess:
        # print(graph.get_tensor_by_name(),'@@@@@@@@@@@@@@')#add
        input = graph.get_tensor_by_name('input:0')
        age = graph.get_tensor_by_name('age:0')
        gender = graph.get_tensor_by_name('gender:0')
        # print(input)
        # print(age)
        # print(gender)
        return sess.run([age, gender], feed_dict={
           input: features,
        })

# self.encoder.generate_embedding(face)
encoder = Encoder()

embedding = encoder.generate_embedding(image)
embedding = np.array(embedding).reshape(1, 512)
# embedding=np.expand_dims(embedding, axis=0)
# print(embedding.shape)
# print(embedding.shape,'######')#(512,)
ages, genders = run(embedding, model_path)
# print(type(ages),type(genders),len(ages),len(genders))
print('ages : ', ages[0], 'genders :',genders[0])


