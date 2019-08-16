# Install
in your root,
```
colcon build --package-select image_system
source install/local_setup.bash
```
then,
```
cd ~/your/workspace/install/image_system/lib/image_system
mkdir model && cd model
cp ~/your/workspace/image_system/model/cifier_adam.npz cifier_adam.npz
cp ~/your/workspace/image_system/model/coco_posenet.npz coco_posenet.npz
cp ~/your/workspace/image_system/model/haarcascade_frontalface_alt.xml haarcascade_frontalface_alt.xml

```
# Usage
ros2 run image_system image_system

it is success example in execution.
```
[INFO] [DetectHuman]: LOADING POSE MODEL
[INFO] [DetectHuman]: LOADING MODEL
[INFO] [DetectHuman]: DONE

```

# Data flow
![image_system](https://github.com/rionehome/image_system/tree/dev/UML/SequenceDiagram.png "image_system_data_flow")
