import cv2
import argparse
import chainer
from detect_human.pose_detector import PoseDetector, draw_person_pose

import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from std_msgs.msg import Bool, Float32
from sensor_msgs.msg import Image

from cv_bridge import CvBridge

from numpy import array

from matplotlib import pyplot as plt

chainer.using_config('enable_backprop', False)


class DetectHuman(Node):
    def __init__(self):
        super(DetectHuman, self).__init__("DetectHuman")

        self.create_subscription(Bool, "/image_system/detect_human", self.detect_human, qos_profile_sensor_data)
        self.create_subscription(Image, "/camera/color/image_raw", self.get_image, qos_profile_sensor_data)

        self.number_human_publisher = self.create_publisher(Float32, "/image_system/data_return", qos_profile_sensor_data)

        self.device_number = -1
        self.number = Float32()

        self.pose_detector = PoseDetector("posenet", "image_system/model/coco_posenet.npz", device=self.device_number)
        self.bridge = CvBridge()

        self.image_data = None
        self.one_time = False

        self.get_logger().info("READY")

    def detect_human(self, msg):
        if self.one_time == False:
            self.one_time = True
            image = self.image_data
            person_pose_array, _ = self.pose_detector(image)
            self.number.data = len(person_pose_array)
            self.number_human_publisher.publish(self.number)


    def get_image(self, msg):
        self.image_data = self.bridge.imgmsg_to_cv2(msg)


def main():
    rclpy.init()

    node = DetectHuman()
    
    rclpy.spin(node)

#if __name__ == '__main__':
#
#    cap = cv2.VideoCapture(0)
#    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
#
#    while True:
#        # get video frame
#        ret, img = cap.read()
#
#        if not ret:
#            print("Failed to capture image")
#            break
#
#        person_pose_array, _ = pose_detector(img)
#        res_img = cv2.addWeighted(img, 0.6, draw_person_pose(img, person_pose_array), 0.4, 0)
#        cv2.imshow("result", res_img)
#        cv2.waitKey(1)
