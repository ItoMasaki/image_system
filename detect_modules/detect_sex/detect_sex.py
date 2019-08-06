"""detect sex"""
import cv2

from cv_bridge import CvBridge


from detect_modules.detect_sex.classifier import detect_human_sex

import numpy as np
from numpy import array, float32


cascade = cv2.CascadeClassifier(
    'image_system/model/haarcascade_frontalface_alt.xml')


def detect_sex(self, msg):
    gray_img = cv2.cvtColor(self.image_data, cv2.COLOR_BGR2GRAY)
    facerects = cascade.detectMultiScale(
        gray_img,
        scaleFactor=1.2,
        minNeighbors=3,
        minSize=(1, 1))

    if len(facerects) > 0:
        woman = 0
        man = 0
        for facerect in facerects:
            cropped_face, face_left_top = self.crop_face(
                self.image_data,
                facerect)
            cropped_face = array(cv2.resize(
                cropped_face,
                (96, 96)),
                dtype=float32)
            sex = detect_human_sex(cropped_face)
            print(sex)
            if sex == 0:
                woman += 1
            elif sex == 1:
                man += 1
            else:
                pass
    return woman, man


def crop_face(self, img, rect):
    orig_img_h, orig_img_w, _ = img.shape
    crop_center_x = rect[0] + rect[2] / 2
    crop_center_y = rect[1] + rect[3] / 2
    crop_width = rect[2] * params['face_crop_scale']
    crop_height = rect[3] * params['face_crop_scale']
    crop_left = max(0, int(crop_center_x - crop_width / 2))
    crop_top = max(0, int(crop_center_y - crop_height / 2))
    crop_right = min(orig_img_w, int(crop_center_x + crop_width / 2))
    crop_bottom = min(orig_img_h, int(crop_center_y + crop_height / 2))
    cropped_face = img[crop_top:crop_bottom, crop_left:crop_right]
    max_edge_len = np.max(cropped_face.shape[:-1])
    padded_face = np.zeros(
        (
            max_edge_len,
            max_edge_len,
            cropped_face.shape[-1]
        ),
        dtype=np.uint8)
    padded_face[0:cropped_face.shape[0],
                0:cropped_face.shape[1]] = cropped_face
    return padded_face, (crop_left, crop_top)
