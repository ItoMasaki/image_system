import cv2

from cv_bridge import CvBridge

from detect_human.entity import params

from detect_sex.classifier import detect_human_sex

import numpy as np
from numpy import array, float32

import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data

from std_msgs.msg import Bool
from sensor_msgs.msg import Image


class DetectSex(Node):
    def __init__(self):
        super(DetectSex, self).__init__("DetectSex")

        self.create_subscription(Bool, "/image_system/detect_sex", self.detect_sex, qos_profile_sensor_data)
        self.create_subscription(Image, "/camera/color/image_raw", self.get_image, qos_profile_sensor_data)

        self.bridge = CvBridge()

        self.cascade = cv2.CascadeClassifier("image_system/model/haarcascade_frontalface_alt.xml")

        self.image_data = None
        self.one_time = False

        self.get_logger().info("READY")


    def detect_sex(self, msg):
        self.one_time = msg.data
        if self.one_time == True:
            self.one_time = False

            gray_img = cv2.cvtColor(self.image_data, cv2.COLOR_BGR2GRAY)
            facerects = self.cascade.detectMultiScale(gray_img, scaleFactor=1.2, minNeighbors=3, minSize=(1, 1))

            if len(facerects) > 0:
                for facerect in facerects:
                    cropped_face, face_left_top = self.crop_face(self.image_data, facerect)
                    cropped_face = array(cv2.resize(cropped_face, (96, 96)), dtype=float32)
                    sex = detect_human_sex(cropped_face)
                    print(sex)


    def get_image(self, msg):
        self.image_data = self.bridge.imgmsg_to_cv2(msg) 


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
        padded_face = np.zeros((max_edge_len, max_edge_len, cropped_face.shape[-1]), dtype=np.uint8)
        padded_face[0:cropped_face.shape[0], 0:cropped_face.shape[1]] = cropped_face
        return padded_face, (crop_left, crop_top)


def main():
    rclpy.init()

    node = DetectSex()

    rclpy.spin(node)
