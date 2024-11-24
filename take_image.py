# take 1 image per 30 frames for video with path ./iot_fire_detect.mp4 and save it in ./images/

import cv2
import os
import sys

def take_image(video_path, image_path):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if count % 30 == 0:
            image_index = str(int(count / 30))
            image_name = '0' * (4 - len(image_index)) + image_index + '.jpg'
            cv2.imwrite(image_path + image_name, frame)
        count += 1
    cap.release()

if __name__ == '__main__':
    video_path = 'iot_fire_detect.mp4'
    image_folder = 'fire_images/'
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)
    take_image(video_path, image_folder)
    print('Finish taking images from ' + video_path)