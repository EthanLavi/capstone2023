# import the necessary packages
import cv2
import sys
import matplotlib.pyplot as plt

def process_file(file):
    # Get the labels from a file
    labels = []
    f = open(file, "r")
    for line in f:
        tokens = line.split()
        if (len(tokens) == 0):
            continue
        if (tokens[0] in ["7", "8"]):
            continue
        x, y, w, h = [float(tokens[i]) for i in range(1,5)]
        w,h = w/2, h/2
        box = [x-w, y-h, x+w, y+h]
        labels.append(box)
    f.close()
    return labels

def bb_intersection_over_union(boxA, boxB):
	# determine the (x, y)-coordinates of the intersection rectangle
	xA = max(boxA[0], boxB[0])
	yA = max(boxA[1], boxB[1])
	xB = min(boxA[2], boxB[2])
	yB = min(boxA[3], boxB[3])
    
	# compute the area of intersection rectangle
	interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
    
	# compute the area of both the prediction and ground-truth
	# rectangles
	boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
	boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)
    
	# compute the intersection over union by taking the intersection
	# area and dividing it by the sum of prediction + ground-truth
	# areas - the interesection area
	iou = interArea / float(boxAArea + boxBArea - interArea)

	# return the intersection over union value
	return iou

if len(sys.argv) < 3:
    print("Must provide two arguments to represent the directories/files to process")
    exit(1)
labels = process_file(sys.argv[1])
predictions = process_file(sys.argv[2])
    
# loop over the detections
buckets = [0] * 10
count = 0
avg = 0
for box in labels:
    maxxer = 0
    mindex = None
    for pred in predictions:
        iou = bb_intersection_over_union(box, pred)
        if maxxer < iou:
            maxxer = iou
            mindex = pred
    if mindex is None:
        break
    count += 1
    avg += maxxer
    i = int(maxxer * 10)
    buckets[i] += 1
    predictions.remove(mindex)

print(buckets)
print("Average IOU:", avg / count)
print("Missed", len(labels) - count, "out of", len(labels))