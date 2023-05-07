import os
import random

img_dir = "kitti/images"
lab_dir = "kitti/labels"
test_img_dir = "kitti/test_images"
test_lab_dir = "kitti/test_labels"

bypass_filter = not input("Filter for only nighttime images? (y/n) ").lower() == "n"

img_moving = []
for image in os.listdir("kitti/images"):
    prefix = image.split(".")[0]
    label_file = os.path.join(lab_dir, prefix + ".txt")
    img_file = os.path.join(img_dir, image)
    if "img_" not in img_file and bypass_filter: # filter for augmented images
        continue
    if not os.path.exists(label_file) and not os.path.exists(img_file):
        continue
    img_moving.append((label_file, img_file))
random.shuffle(img_moving)
move_n = int(len(img_moving) * 0.2)

for label, img in img_moving[:move_n]:
    os.system(f"mv {label} {test_lab_dir}")
    os.system(f"mv {img} {test_img_dir}")
