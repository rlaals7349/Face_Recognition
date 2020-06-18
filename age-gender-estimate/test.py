tar_age_dir=['20_24','25_29','30_34','35_39']
import argparse
import os

import numpy as np
import tensorflow as tf
from network_conv import inference
from utils import get_inputs


def test_once(tfrecords_path, batch_size, model_checkpoint_path):
    with tf.Graph().as_default():
        sess = tf.Session()
        
        features, age_labels, gender_labels, file_paths = get_inputs(path=tfrecords_path, batch_size=batch_size, num_epochs=1)

        net, gender_logits, age_logits = inference(features, age_labels, gender_labels,
                                          training=False)

        age_cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=age_labels, logits=age_logits)
        age_cross_entropy_mean = tf.reduce_mean(age_cross_entropy)

        gender_cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=gender_labels, logits=gender_logits)
        gender_cross_entropy_mean = tf.reduce_mean(gender_cross_entropy)
        total_loss = tf.add_n(
            [gender_cross_entropy_mean, age_cross_entropy_mean] + tf.get_collection(tf.GraphKeys.REGULARIZATION_LOSSES),
            name="total_loss")

        # age_ = tf.cast(tf.constant([i for i in range(0, 117)]), tf.float32)
        # prob_age = tf.reduce_sum(tf.multiply(tf.nn.softmax(age_logits), age_), axis=1)
        # test=tf.convert_to_tensor(tf.nn.softmax(age_logits)) # modify
        prob_age = tf.argmax(tf.nn.softmax(age_logits), 1)
        age_acc = tf.reduce_mean(tf.to_float(tf.equal(tf.to_int64(prob_age), age_labels)))

        # abs_age_error = tf.losses.absolute_difference(prob_age, age_labels)
        # test=tf.nn.softmax(gender_logits)
        prob_gender = tf.argmax(tf.nn.softmax(gender_logits), 1)
        gender_acc = tf.reduce_mean(tf.to_float(tf.equal(tf.to_int64(prob_gender), gender_labels)))
        init_op = tf.group(tf.global_variables_initializer(),
                           tf.local_variables_initializer())
        sess.run(init_op)
        saver = tf.train.Saver()
        saver.restore(sess, model_checkpoint_path)

        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(sess=sess, coord=coord)

        mean_age_acc, mean_gender_acc, mean_loss = [], [], []
        try:
            while not coord.should_stop():
                prob_gender_val, real_gender, prob_age_val, real_age, image_val, gender_acc_val, age_acc_val, cross_entropy_mean_val, file_names = sess.run(
                    [prob_gender, gender_labels, prob_age, age_labels, features, gender_acc, age_acc, total_loss,
                     file_paths])
                # print(type(prob_gender_val[0]))

                if prob_gender_val[0] == 0:
                    # prob_gender_val = "M"
                    # print('gender_logits',gender_logits)
                    # print('prob_gender_val',prob_gender_val,type(prob_gender_val))
                    # print("prob_age_val, real_age, prob_gender_val, real_gender",tar_age_dir[int(prob_age_val[0])], tar_age_dir[int(real_age[0])], prob_gender_val, real_gender)
                    # print(tar_age_dir[int(prob_age_val)],',', tar_age_dir[int(real_age)],',', prob_gender_val,',', real_gender)
                    print(prob_age_val,',', real_age,',', prob_gender_val,',', real_gender)
                else :
                    # prob_gender_val = "F"
                    # print("prob_age_val, real_age, prob_gender_val, real_gender",tar_age_dir[int(prob_age_val[0])], tar_age_dir[int(real_age[0])], prob_gender_val, real_gender)
                    print(prob_age_val,',', real_age,',', prob_gender_val,',', real_gender)

                mean_age_acc.append(age_acc_val)
                mean_gender_acc.append(gender_acc_val)
                mean_loss.append(cross_entropy_mean_val)
                # print("Age_acc:%s, Gender_Acc:%s, Loss:%.2f" % (
                #     age_acc_val, gender_acc_val, cross_entropy_mean_val))
        except tf.errors.OutOfRangeError:
            print('Summary:')
        finally:
            
            # When done, ask the threads to stop.
            coord.request_stop()
        coord.join(threads)
        sess.close()
        return prob_age_val, real_age, prob_gender_val, real_gender, image_val, np.mean(mean_age_acc), np.mean(
            mean_gender_acc), np.mean(mean_loss), file_names


def choose_best_model(model_path, image_path, batch_size):
    ckpt = tf.train.get_checkpoint_state(model_path)
    best_gender_acc, best_gender_idx = 0.0, 0
    best_age_acc, best_age_idx = 0.0, 0
    result = []
    for idx in range(len(ckpt.all_model_checkpoint_paths)):
        print("restore model %d!" % idx)
        # gender_acc_val, age_acc_val, cross_entropy_mean_val,
        _, _, _, _, _, mean_age_acc, mean_gender_acc, mean_loss, _ = test_once(image_path, batch_size,
                                                                                 ckpt.all_model_checkpoint_paths[idx], )
        result.append([ckpt.all_model_checkpoint_paths[idx], mean_age_acc, mean_gender_acc])
        if mean_gender_acc > best_gender_acc:
            best_gender_acc, best_gender_idx = mean_gender_acc, idx
        if mean_age_acc > best_age_acc:
            best_age_acc, best_age_idx = mean_age_acc, idx
    return best_gender_acc, ckpt.all_model_checkpoint_paths[best_gender_idx], best_age_acc, \
           ckpt.all_model_checkpoint_paths[best_age_idx], result


def main(model_path, image_path, batch_size):
    best_gender_acc, gender_model, best_age_acc, age_model, result = choose_best_model(model_path, image_path,
                                                                                       batch_size)
    return best_gender_acc, gender_model, best_age_acc, age_model, result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # parser.add_argument("--tfrecords", type=str, default="/home/team/datasets/sum_wiki_4000+2000/tfrecords/sum_wiki_4000_mtc_test.tfrecords", help="Testset path")
    parser.add_argument("--tfrecords", type=str, default="/home/team/datasets/sum_wiki_4000+2000/tfrecords/sum_wiki_4000_mtc_test.tfrecords", help="Testset path")
    parser.add_argument("--batch_size", type=int, default=30, help="Batch size")
    # parser.add_argument("--model_path", type=str, default="/home/team/models/sum_wiki_4000+2000_bat64/models/", help="Model path")
    parser.add_argument("--model_path", type=str, default="/home/team/models/sum_wiki_4000+2000_bat64/models/", help="Model path")
    parser.add_argument("--choose_best", action="store_true", default=False,
                        help="If you use this flag, will test all models under model path and return the best one.")
    parser.add_argument("--cuda", default=False, action="store_true",
                        help="Set this flag will use cuda when testing.")
    args = parser.parse_args()
    if not args.cuda:
        os.environ['CUDA_VISIBLE_DEVICES'] = ''

    if args.choose_best:
        best_gender_acc, gender_model, best_age_acc, age_model, result = main(args.model_path, args.tfrecords,
                                                                              args.batch_size)
        print("Age_acc:%s, Gender_Acc:%s, Age_model:%s, Gender_model:%s" % (
            best_age_acc, best_gender_acc, age_model, gender_model))
    else:
        ckpt = tf.train.get_checkpoint_state(args.model_path)
        if ckpt and ckpt.model_checkpoint_path:
            prob_age_val, real_age, prob_gender_val, real_gender, _, mean_age_acc, mean_gender_acc, mean_loss, _ = test_once(args.tfrecords,
                                                                                     args.batch_size,
                                                                                     ckpt.model_checkpoint_path)
            print("Age_acc:%s, Gender_Acc:%s, Loss:%.2f" % (mean_age_acc, mean_gender_acc , mean_loss))
            
            # if prob_age_val == 0:
            #     prob_age_val='20_24'
            # if prob_age_val == 1:
            #     prob_age_val='25_29'
            # if prob_age_val == 2:
            #     prob_age_val='30_34'
            # if prob_age_val ==3:
            #     prob_age_val='35_39'
            # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!","prob_age_val, real_age, prob_gender_val, real_gender", tar_age_dir[int(prob_age_val)], tar_age_dir[int(real_age)], prob_gender_val, real_gender)
        else:
            raise IOError("Pretrained model not found!")

# model_20 
# Age_MAE:4.80, Gender_Acc:96.42%
# Age_model:/home/team/age-gender-embeds/models/model.ckpt-14001
# Gender_model:/home/team/age-gender-embeds/models/model.ckpt-7001