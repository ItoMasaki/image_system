# Install
in your root,
```
colcon build --package-select image_system
source install/local_setup.bash
```
then,
```
cd ~/your_workspace/install/image_system/lib/image_system
mkdir model
cp ~/your_workspace/image_system/model/cifier_adam.npz cifier_adam.npz
cp ~/your_workspace/image_system/model/coco_posenet.npz coco_posenet.npz
cp ~/your_workspace/image_system/model/haarcascade_frontalface_alt.xml haarcascade_frontalface_alt.xml

```
