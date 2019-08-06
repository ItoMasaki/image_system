import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from rclpy.qos import qos_profile_sensor_data

from machine_learning.classifier import detect_human_sex
from detect_human.detect_human import detect_human
from detect_sex.detect_sex import detect_sex

class ImageSystem(Node):
    def __init__(self):
        super(ImageSystem, self).__init__("ImageSystem")

        self.create_subscription(String, "/image_system/command", self.command_callback, qos_profile_sensor_data)


    def command_callback(self, msg):
        if self.one_time_execute(msg.data, self.command):

            # contain command data
            self.command = msg.data

            # Command:speak , Content:hello!
            command = msg.data.split(" , ")

            if "human" == command[0].replace("Command:", ""):
                self.detect_human()

            if "sex" == command[0].replace("Command:", ""):
                self.detect_sex()

            if "object" == command[0].replace("Command:", ""):
                self.detect_object()


    def detect_human(self):
        # [TODO] input image array (numpy)
        number = detect_human(image)
        

    def detect_sex(self):
        # [TODO] input image array (numpy)
        flag = detect_sex(image)


    def detect_object(self):
        # [TODO] sonouti yaru!
        print("[*] detect object")


    # only one time execute
    def one_time_execute(self, now, previous):
        flag = False

        if now != previous:
            flag = True

        return flag


def main():
    rclpy.init()
    node = ImageSystem()
    rclpy.spin(node)
