import cv2 as cv
from datetime import datetime as dt
from yolo.yolo_conversion import BoxCoordinates, labels, label_colors
import os

os.makedirs("outdir2", exist_ok=True)
LABELER = "ethan"
for val in labels:
    print(labels[val], " --> ", val)
print("CONTROLS:")
print("[0-9] - changes the label of the last bounding box (labels above)")
print("[q] - quits the program")
print("[space] - saves the frame")
print("[z] - undo the last bounding box")
print("[d] - will discard the frame")

click_context = (0, 0)
drawing = False
boxes = []


def draw_frame():
    frame = empty_frame.copy()
    for box in boxes:
        label = box[2]
        color_rgb = label_colors[label][1]
        cv.rectangle(frame, box[0], box[1], color_rgb, 2)
        text_coord = (min(box[0][0], box[1][0]) + 4, min(box[0][1], box[1][1]) + 30)
        cv.putText(frame, label, text_coord, cv.FONT_HERSHEY_SIMPLEX, 1, color_rgb, 4)
    cv.imshow("Frame", frame)


def drawer(event, x, y, flags, param):
    global click_context, drawing, boxes
    frame = empty_frame.copy()
    if frame is None:
        return
    if event == cv.EVENT_LBUTTONDOWN and not drawing:
        click_context = (x, y)
        drawing = True
    elif event == cv.EVENT_LBUTTONDOWN and drawing:
        # draw a rectangle around the region of interest
        boxes.append([click_context, (x, y), 'Car'])
        drawing = False
        draw_frame()
    elif drawing:
        frame_temp = frame.copy()
        cv.rectangle(frame_temp, click_context, (x, y), (0, 255, 0), 2)
        cv.imshow("Frame", frame_temp)


cap = cv.VideoCapture("vid.mp4")
cv.namedWindow("Frame")
cv.setMouseCallback("Frame", drawer)
restart = True
empty_frame = None
# Read until video is completed
while cap.isOpened():
    # Capture frame-by-frame
    ret = True
    if restart:
        for i in range(100):
            ret, frame_uncrop = cap.read()
        boxes = []
        h, w, c = frame_uncrop.shape
        empty_frame = frame_uncrop[int(h * 0.1):int(h * 0.9), int(w * 0.1):int(w * 0.9)].copy()
    restart = True
    if ret:
        draw_frame()
        key = cv.waitKey(0) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('z'):
            restart = False
            if len(boxes) == 0:
                continue
            boxes.pop()
        elif key == ord(' '):
            filename_prefix = "outdir2/" + LABELER + dt.now().strftime("%m_%d_%H_%M_%S")
            # continue normally and save
            f = open(filename_prefix + ".txt", "w")
            fdata = ""
            h, w, c = empty_frame.shape
            for box in boxes:
                # classification, x1, y1, x2, y2
                fdata += BoxCoordinates([box[2], box[0][0], box[0][1], box[1][0], box[1][1]], raw=True).to_line(w, h)
            f.write(fdata)
            f.close()
            cv.imwrite(filename_prefix + ".png", empty_frame)
            continue
        elif key in [ord(str(i)) for i in range(10)]:
            restart = False
            if key == ord('9'):
                continue
            label = list(labels.keys())[list(labels.values()).index(int(chr(key)))]
            color, color_rgb = label_colors[label]
            if len(boxes) != 0:
                i = len(boxes) - 1
                boxes[i][2] = label
                box = boxes[i]
        elif key == ord('d'):
            # discard the frame
            continue
        else:
            restart = False
    else:
        break

cap.release()
cv.destroyAllWindows()
