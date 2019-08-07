curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=1bn-zEOL1hsUwI1Hd4aS1LjUQsFYo4yp0" > /dev/null
CODE="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"
curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${CODE}&id=1bn-zEOL1hsUwI1Hd4aS1LjUQsFYo4yp0" -O /model/coco_posenet.npz

curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=1osfe6mWT4dlnmcUaIINZYKvIkqwVi759" > /dev/null
CODE="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"
curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${CODE}&id=1osfe6mWT4dlnmcUaIINZYKvIkqwVi759" -O /model/cifier_adam.npz
