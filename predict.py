#! /usr/bin/python
import pickle
from deepid1 import *
import tensorflow as tf
from scipy.spatial.distance import cosine, euclidean, pdist
from vec import *
import show_pic

def one_list(l):
    c = [1/(1+x) for x in l]
    return c

if __name__ == '__main__':

    #print(testX1[:5], testX2[:5])
    #print(testY[:5])
    testx1, testx2, testy = show_pic.show_load_data()
    test1 = np.concatenate((testx1, testX1[:1]), axis=0)
    test2 = np.concatenate((testx2, testX2[:1]), axis=0)
    testY1 = np.concatenate((testy, testY[:1]), axis=0)
    with tf.Session() as sess:
        saver.restore(sess, 'checkpoint/30000.ckpt')
        v1 = sess.run(h5, {h0: test1})
        v2 = sess.run(h5, {h0: test2})
        print(len(v1[0]))
        #pre_y = sess.run(tf.clip_by_value([cosine(x, y) for x, y in zip(v1, v2)], 1e-10, 10))
        pre = one_list([pdist(np.vstack([x, y])) for x, y in zip(v1, v2)])
        #pre_y = np.array(pre_y)

    pre_y = np.array([cosine(x, y) for x, y in zip(v1, v2)])
    #print(v1, v2)
    print (pre)
    print(pre_y)
    print(testY1)

    def part_mean(x, mask):
        z = x * mask
        return float(np.sum(z) / np.count_nonzero(z))

    true_mean = part_mean(pre_y, testY1)
    false_mean = part_mean(pre_y, 1-testY1)
    print(true_mean, false_mean)

    print(np.mean((pre_y < (true_mean + false_mean)/2) == testY1.astype(bool)))

    print([(pre_y < (true_mean + false_mean)/2) == testY1.astype(bool)])

