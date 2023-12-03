import os
import random

img_dir = "kitti/images"
lab_dir = "kitti/labels"
test_img_dir = "kitti/test_images"
test_lab_dir = "kitti/test_labels"

img_moving = []
j = 0
for image in os.listdir("kitti/images"):
    j += 1
    if j % 1000 == 0:
        print("Processed", j, "images")
    prefix = image.split(".")[0]
    label_file = os.path.join(lab_dir, prefix + ".txt")
    img_file = os.path.join(img_dir, image)
    if "aug" in img_file: # filter for augmented images
        continue
    if not os.path.exists(label_file) or not os.path.exists(img_file):
        print(label_file)
        print(img_file)
        print("UNDO EVERYTHING (with mv command), NON EXISTENT LABEL FILE FOR THESE IMAGES")
        exit(0)
    img_moving.append((label_file, img_file))
random.shuffle(img_moving)
move_n = int(len(img_moving) * 0.3)

print("Starting move of", len(img_moving) * 0.3, "images")
i = 0
for label, img in img_moving[:move_n]:
    i += 1
    if i % 100 == 0:
        print("Moved", i, "images")
    os.system(f"mv {label} {test_lab_dir}")
    os.system(f"mv {img} {test_img_dir}")
