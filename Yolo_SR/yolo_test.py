import cv2
from PIL import Image
import numpy as np
import time
import torch
import os
import matplotlib.pyplot as plt
from yolo import YOLO

yolo = YOLO()
path = './input/'
dirs = os.listdir( path )
for file in dirs:
    img_name = file.split('.')[0]
    img_name_last = file.split('.')[1]
    detection_start = time.time()
    image = Image.open(os.path.join(path,file))
    uncroped_image = cv2.imread(os.path.join(path,file))
    r_image,boxes = yolo.detect_image(image)
    torch.cuda.synchronize()
    detection_end = time.time()
    print ('detection inference time: {}'.format(detection_end-detection_start))
    box = boxes

    cropping_start = time.time()
    for i in range(boxes.shape[0]):
        top = boxes[i][0]
        left = boxes[i][1]
        bottom = boxes[i][2]
        right = boxes[i][3]

        top = top - 5
        left = left - 5
        bottom = bottom + 5
        right = right + 5

        # coordinate
        top = int(max(0, np.floor(top + 0.5).astype('int32')))
        left = int(max(0, np.floor(left + 0.5).astype('int32')))
        bottom = int(min(np.shape(image)[0], np.floor(bottom + 0.5).astype('int32')))
        right = int(min(np.shape(image)[1], np.floor(right + 0.5).astype('int32')))

        croped_region = uncroped_image[top:bottom,left:right]
        os.makedirs("./yolo_output", exist_ok=True)
        cv2.imwrite("./yolo_output/croped_img_"+str(img_name)+"_"+str(i)+".jpg",croped_region)

    cropping_end = time.time()
    print ('cropping inference time: {}'.format(cropping_end-cropping_start))
    # r_image.show()
    os.makedirs("./yolo_detection", exist_ok=True)
    r_image.save("./yolo_detection/det_img_"+str(img_name)+".jpg")

    # plt.imshow(r_image)
    # plt.show()
    # os.makedirs("./yolo_detection", exist_ok=True)
    # plt.savefig("./yolo_detection/det_img_"+str(img_name)+".jpg")