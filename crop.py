#! /usr/bin/python
import os
from PIL import Image, ImageEnhance
import random

#cut to (47, 55), and save in dest file
def crop_img_by_half_center(src_file_path, dest_file_path):
    im = Image.open(src_file_path)
    x_size, y_size = im.size
    start_point_xy = x_size / 4
    end_point_xy   = x_size / 4 + x_size / 2
    box = (start_point_xy, start_point_xy, end_point_xy, end_point_xy)
    new_im = im.crop(box)
    new_new_im = new_im.resize((47,55))

    opt = random.randint(1, 7)
    if opt<3:
        rand_opt2(dest_file_path, new_new_im, 1.8)
    elif opt>=3 and opt<5:
        rand_opt2(dest_file_path, new_new_im, 1.5)
    elif opt>=5 and opt<7:
        new_new_im.save(dest_file_path)
    else:
        new_new_im.save(dest_file_path)
        rand_opt2(dest_file_path, new_new_im, 1.9)


def rand_opt2(dest_file_path, new_new_im, num):
    dest_path = dest_file_path.split('.')
    im_dark = ImageEnhance.Brightness(new_new_im).enhance(num)
    dest_file_path3 = '.'.join(dest_path[:-1]) + '3.' + dest_path[-1]
    im_dark.save(dest_file_path3)

def walk_through_the_folder_for_crop(aligned_db_folder, result_folder):
    if not os.path.exists(result_folder):
        os.mkdir(result_folder)
    
    i = 0
    img_count = 0
    for people_folder in os.listdir(aligned_db_folder):
        if people_folder.startswith(".DS"):
            continue
        src_people_path = aligned_db_folder + people_folder + '/'
        dest_people_path = result_folder + people_folder + '/'
        if not os.path.exists(dest_people_path):
            os.mkdir(dest_people_path)
        for video_folder in os.listdir(src_people_path):
            if video_folder.startswith(".DS"):
                continue
            src_video_path = src_people_path + video_folder + '/'
            dest_video_path = dest_people_path + video_folder + '/'
            if not os.path.exists(dest_video_path):
                os.mkdir(dest_video_path)
            for img_file in os.listdir(src_video_path):
                if img_file.startswith(".DS"):
                    continue
                src_img_path = src_video_path + img_file
                dest_img_path = dest_video_path + img_file
                crop_img_by_half_center(src_img_path, dest_img_path)
            i += 1
            img_count += len(os.listdir(src_video_path))
        
if __name__ == '__main__':
    #/Users/ljl/Desktop/info注册信息管理系统/source
    aligned_db_folder = "/Users/ljl/Desktop/deepid/source"
    result_folder = "/Users/ljl/Desktop/deepid/result"
    if not aligned_db_folder.endswith('/'):
        aligned_db_folder += '/'
    if not result_folder.endswith('/'):
        result_folder += '/'
    walk_through_the_folder_for_crop(aligned_db_folder, result_folder)
    
