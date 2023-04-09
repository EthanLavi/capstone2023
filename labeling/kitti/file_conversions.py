import os
from yolo_conversion import BoxCoordinates
import cv2

home_path = os.path.join(input("Path to tensorflow datasets"), 'tensorflow_datasets/downloads/data/training')
label_dir = home_path + '/label/'
img_dir = home_path + '/image/'
out_dir = home_path + '/output/'

filenames = os.listdir(label_dir)
for i, file in enumerate(filenames):
    if i % 100 == 0 and i != 0:
        print(str(i) + " files converted")
    file_prefix = file.split(".txt")[0]
    dims = cv2.imread(img_dir + file_prefix + ".png").shape
    h, w, c = dims
    modif_f = ''
    with open(label_dir + file, 'r') as f:
        label_arr = [row.split() for row in f.read().strip().split("\n")]
        for label in label_arr:
            coords = BoxCoordinates("kitti", label)
            modif_f += coords.to_line(w, h)
    with open(out_dir + file_prefix + ".txt", 'w') as g:
        g.write(modif_f.strip())
