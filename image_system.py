"""image system main code"""
from detect_modules.detect_human import detect_human

from detect_modules.detect_sex import detect_sex

import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data

from std_msgs.msg import String


class ImageSystem(Node):
    def __init__(self):
        super(ImageSystem, self).__init__('ImageSystem')

        self.create_subscription(
            String,
            '/image_system/command',
            self.command_callback,
            qos_profile_sensor_data)
        self.message = None
        self.command = None

    def command_callback(self, msg):
        if self.one_time_execute(msg.data, self.command):

            # contain command data
            self.command = msg.data

            # Command:speak , Content:hello!
            command = msg.data.split(',')

            if 'human' == command[0].replace('Command:', ''):
                self.message = self.detect_human()
                self.cerebrum_publisher('Return:1,Content:'+self.message)
            if 'sex' == command[0].replace('Command:', ''):
                self.message = self.detect_sex()
                self.cerebrum_publisher('Return:1,Content:'+self.message)
            if 'object' == command[0].replace('Command:', ''):
                self.detect_object()

    def detect_human(self):
        # [TODO] input image array (numpy)
        number = detect_human(image)
        return str(number)

    def detect_sex(self):
        # [TODO] input image array (numpy)
        woman, man = detect_sex(image)
        return str(woman)+'|'+str(man)

    def detect_object(self):
        # [TODO] sonouti yaru!
        print('[*] detect object')

    def cerebrum_publisher(self, message):
        self.senses_publisher = self.create_publisher(
            String,
            'Cerebrum/Command',
            qos_profile_sensor_data)

        _trans_message = String()
        _trans_message.data = message

        self.senses_publisher.publish(_trans_message)
        self.destroy_publisher(self.senses_publisher)

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


if __name__ == "__main__":
    main()
