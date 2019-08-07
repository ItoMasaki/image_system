FILE_ID=1bn-zEOL1hsUwI1Hd4aS1LjUQsFYo4yp0
FILE_NAME=./model/coco_posenet.npz

wget --save-cookie /tmp/cookie "https://drive.google.com/uc?export=download&id=${FILE_ID}" > /dev/null
CODE="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"
aria2c -x10 --load-cookies /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${CODE}&id=${FILE_ID}" -o ./model/coco_posenet.npz
rm -rf 'uc?export*'

#curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=1osfe6mWT4dlnmcUaIINZYKvIkqwVi759" > /dev/null
#CODE="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"
#curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${CODE}&id=1osfe6mWT4dlnmcUaIINZYKvIkqwVi759" -O ./model/cifier_adam.npz
