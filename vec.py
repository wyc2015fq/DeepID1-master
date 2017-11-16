#! /usr/bin/python
import pickle
import numpy as np
from PIL import Image

def vectorize_imgs(img_path):
    with Image.open(img_path) as img:
        arr_img = np.asarray(img, dtype='float32')
        return arr_img

def read_csv_file(csv_file):
    x, y = [], []
    with open(csv_file, "r") as f:
        for line in f.readlines():
            path, label = line.strip().split()
            x.append(vectorize_imgs(path))
            y.append(int(label))
    return np.asarray(x, dtype='float32'), np.asarray(y, dtype='int32')

def read_csv_pair_file(csv_file):
    x1, x2, y = [], [], []
    with open(csv_file, "r") as f:
        for line in f.readlines():
            p1, p2, label = line.strip().split()
            x1.append(vectorize_imgs(p1))
            x2.append(vectorize_imgs(p2))
            y.append(int(label))
    return np.asarray(x1, dtype='float32'), np.asarray(x2, dtype='float32'), np.asarray(y, dtype='int32')

def load_data():
    with open('/Users/ljl/Desktop/deepid/dataset.pkl', 'rb') as f:
        testX1 = pickle.load(f)
        testX2 = pickle.load(f)
        testY  = pickle.load(f)
        validX = pickle.load(f)
        validY = pickle.load(f)
        trainX1 = pickle.load(f)
        trainY1 = pickle.load(f)
        trainX2 = pickle.load(f)
        trainY2 = pickle.load(f)
        trainX3 = pickle.load(f)
        trainY3 = pickle.load(f)
        trainX4 = pickle.load(f)
        trainY4 = pickle.load(f)
        trainX5 = pickle.load(f)
        trainY5 = pickle.load(f)
        return testX1, testX2, testY, validX, validY, trainX1, trainY1, trainX2, \
               trainY2, trainX3, trainY3, trainX4, trainY4, trainX5, trainY5

if __name__ == '__main__':
    testX1, testX2, testY = read_csv_pair_file('/Users/ljl/Desktop/deepid/test_set.csv')
    validX, validY = read_csv_file('/Users/ljl/Desktop/deepid/valid_set.csv')
    trainX, trainY = read_csv_file('/Users/ljl/Desktop/deepid/train_set.csv')
    trainX1, trainY1 = trainX[:20000], trainY[:20000]
    trainX2, trainY2 = trainX[20000:40000], trainY[20000:40000]
    trainX3, trainY3 = trainX[40000:60000], trainY[40000:60000]
    trainX4, trainY4 = trainX[60000:80000], trainY[60000:80000]
    trainX5, trainY5 = trainX[80000:], trainY[80000:]

    print(testX1.shape, testX2.shape, testY.shape)
    print(validX.shape, validY.shape)
    print(trainX1.shape, trainY1.shape)
    print(trainX5.shape, trainY5.shape)

    with open('/Users/ljl/Desktop/deepid/dataset.pkl', 'wb') as f:
        pickle.dump(testX1, f, pickle.HIGHEST_PROTOCOL)
        pickle.dump(testX2, f, pickle.HIGHEST_PROTOCOL)
        pickle.dump(testY , f, pickle.HIGHEST_PROTOCOL)
        pickle.dump(validX, f, pickle.HIGHEST_PROTOCOL)
        pickle.dump(validY, f, pickle.HIGHEST_PROTOCOL)
        pickle.dump(trainX1, f, pickle.HIGHEST_PROTOCOL)
        pickle.dump(trainY1, f, pickle.HIGHEST_PROTOCOL)
        pickle.dump(trainX2, f, pickle.HIGHEST_PROTOCOL)
        pickle.dump(trainY2, f, pickle.HIGHEST_PROTOCOL)
        pickle.dump(trainX3, f, pickle.HIGHEST_PROTOCOL)
        pickle.dump(trainY3, f, pickle.HIGHEST_PROTOCOL)
        pickle.dump(trainX4, f, pickle.HIGHEST_PROTOCOL)
        pickle.dump(trainY4, f, pickle.HIGHEST_PROTOCOL)
        pickle.dump(trainX5, f, pickle.HIGHEST_PROTOCOL)
        pickle.dump(trainY5, f, pickle.HIGHEST_PROTOCOL)
