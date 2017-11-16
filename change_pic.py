import tensorflow as tf
import matplotlib.pyplot as plt

img_data = tf.gfile.FastGFile("/Users/ljl/Desktop/info注册信息管理系统/source/zw/1/1311510627436_.pic.jpg").read()

with tf.Session() as sess:
    img = tf.image.decode_jpeg(img_data)
    plt.imshow(img.eval())
    plt.show()

    #img = tf.image.convert_image_dtype(img, dtype=tf.float32)

    img_brightness = tf.image.adjust_brightness(img, -0.25)
    #with tf.gfile.GFile("/Users/ljl/Desktop/info注册信息管理系统/source/ljl/1/", "wb") as f:
    #    f.write(img.eval)
    plt.imshow(img_brightness.eval())
    plt.show()
