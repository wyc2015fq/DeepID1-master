import tensorflow as tf
import matplotlib.pyplot as plt
import os
import random
import pickle
import numpy as np
from PIL import Image, ImageEnhance
import tensorflow as tf

def fatch_pics_for_one_user(people_path):
    people_imgs = []
    for video_folder in os.listdir(people_path):
        if video_folder.startswith(".DS"):
            continue
        for video_file_name in os.listdir(os.path.join(people_path, video_folder)):
            if video_file_name.startswith(".DS"):
                continue
            people_imgs.append(os.path.join(people_path, video_folder, video_file_name))
    random.shuffle(people_imgs)
    return people_imgs

def build_dataset(src_folder):
    total_people, total_picture = 0, 0
    test_set = []
    for people_folder in os.listdir(src_folder):
        if people_folder.startswith(".DS"):
            continue
        people_imgs = fatch_pics_for_one_user(os.path.join(src_folder, people_folder))
        total_people += 1
        total_picture += len(people_imgs)
        for i in range(len(people_imgs)):
            for j in range(i):
                test_set.append((people_imgs[j], people_imgs[i], 1))
    return test_set

def set_to_csv_file(data_set, file_name):
    with open(file_name, "w") as f:
        for item in data_set:
            print(" ".join(map(str, item)), file=f)

###
###code for vec
###
def vectorize_imgs(img_path):
    with Image.open(img_path) as img:
        arr_img = np.asarray(img, dtype='float32')
        return arr_img

def vectorize_imgs2(img_path):
    with Image.open(img_path) as img:
        arr_img = np.asarray(img, dtype='float32')
        arr_img_bri = np.asarray(ImageEnhance.Brightness(img).enhance(0.8), dtype='float32')
        arr_img_dar = np.asarray(ImageEnhance.Brightness(img).enhance(1.2), dtype='float32')
        return [arr_img, arr_img_bri, arr_img_dar]

def read_csv_pair_file(csv_file):
    x1, x2, y = [], [], []
    with open(csv_file, "r") as f:
        for line in f.readlines():
            p1, p2, label = line.strip().split()
            x1.append(vectorize_imgs(p1))
            x2.append(vectorize_imgs(p2))
            y.append(int(label))
    return np.asarray(x1, dtype='float32'), np.asarray(x2, dtype='float32'), np.asarray(y, dtype='int32')

def read_csv_pair_file2(csv_file):
    x1, x2, y = [], [], []
    with open(csv_file, "r") as f:
        for line in f.readlines():
            p1, p2, label = line.strip().split()
            #print(vectorize_imgs2(p1))
            x1.extend(vectorize_imgs2(p1))
            x2.extend(vectorize_imgs2(p2))
            y.extend([int(label), int(label), int(label)])
    return np.asarray(x1, dtype='float32'), np.asarray(x2, dtype='float32'), np.asarray(y, dtype='int32')



def show_load_data():
    with open("/Users/ljl/Desktop/info注册信息管理系统/data/dataset.pkl", "rb") as f:
        testX1 = pickle.load(f)
        testX2 = pickle.load(f)
        testY  = pickle.load(f)
        return testX1, testX2, testY

if __name__ == "__main__":
    '''
    src_folder    = "/Users/ljl/Desktop/info注册信息管理系统/result"
    test_set_file = "/Users/ljl/Desktop/info注册信息管理系统/data/test_set.csv"
    test_set = build_dataset(src_folder)
    set_to_csv_file(test_set, test_set_file)
    '''
    testX1, testX2, testY = read_csv_pair_file2("/Users/ljl/Desktop/info注册信息管理系统/data/test_set.csv")
    print(testX1.shape)
    with open('/Users/ljl/Desktop/info注册信息管理系统/data/dataset.pkl', 'wb') as f:
        pickle.dump(testX1, f, pickle.HIGHEST_PROTOCOL)
        pickle.dump(testX2, f, pickle.HIGHEST_PROTOCOL)
        pickle.dump(testY, f, pickle.HIGHEST_PROTOCOL)
