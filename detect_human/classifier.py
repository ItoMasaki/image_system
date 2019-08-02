import chainer
from chainer import serializers
from chainer import links as L
from chainer import optimizers
import chainer.computational_graph as c

from machine_learning.model import VGG_16

from glob import glob
from PIL import Image
from matplotlib import pyplot as plt

from numpy import array, float32, argmax


print("[INFO] [DetectHuman]: LOADING MODEL")
model = L.Classifier(VGG_16())
optimizer = optimizers.Adam()
optimizer.setup(model)
print("[INFO] [DetectHuman]: DONE")

serializers.load_npz("image_system/model/cifier_adam.npz", model)

def detect_human_sex(image):
    # image must be numpy array
    image.dtype = "float32"
    image = transpose(2, 0, 1).reshape(1, 3, 96, 96)
    predicted = model.predictor(image)
    sex = argmax(array(predicted.data))

    return sex
