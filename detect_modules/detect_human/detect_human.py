import os

import chainer

from .pose_detector import PoseDetector, draw_person_pose


chainer.using_config('enable_backprop', False)

file_path = os.path.abspath(__file__)
npz = file_path.replace(
    'detect_modules/detect_human/detect_human.py', 'model/coco_posenet.npz')
device_number = -1
pose_detector = PoseDetector(
    'posenet',
    npz,
    device=device_number)


# input image array
def detect_human(image):
    person_pose_array, _ = pose_detector(image)
    return len(person_pose_array)
