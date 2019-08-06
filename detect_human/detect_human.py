import chainer
from detect_human.pose_detector import PoseDetector, draw_person_pose


chainer.using_config('enable_backprop', False)


device_number = -1
pose_detector = PoseDetector("posenet", "image_system/model/coco_posenet.npz", device=self.device_number)


# input image array
def detect_human(self, image):
    person_pose_array, _ = self.pose_detector(image)
    return len(person_pose_array)
