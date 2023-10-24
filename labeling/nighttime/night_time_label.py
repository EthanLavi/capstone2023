from yolo import yolo_conversion as yolo
import cv2 as cv
import os

label_path = input("Path to label file:\n")
folder_with_imgs = input("Path to imgs folder:\n")
folder_for_labels = input("Path for output labels (must exist):\n")

# Read in labels
f = open(label_path, "r")
data = f.read()
f.close()

# Get data per image
data_it = data.split("\n")
for img_num, img_label in enumerate(data_it):
    label_name = f"img_{img_num}.txt"
    img_name = f"img_{img_num}.jpg"

    tokens = img_label.split()
    assert(int(tokens[0]) == img_num)
    lines = ""
    if not os.path.isfile(os.path.join(folder_with_imgs, img_name)):
        continue
    img_content = cv.imread(os.path.join(folder_with_imgs, img_name))
    h, w, c = img_content.shape
    for img_i in range(int(tokens[1])):
        i = 2 + (img_i * 4)
        x1, y1, width, height = (float(tokens[i]), float(tokens[i + 1]), float(tokens[i + 2]), float(tokens[i + 3]))
        coords = yolo.BoxCoordinates(['Car', x1, y1, x1 + width, y1 + height], raw=True)
        lines += coords.to_line(w, h)

    # write the label
    f = open(os.path.join(folder_for_labels, label_name), "w")
    f.write(lines)
    f.close()
print("Done!")
