# Skillion Capstone 2023

## Directory Structure (Important Folders Only)
```
├── eval ==> Contains script for comparing test_labels_eval and test_labels to graph IOU for the model.
├── labeling
│   ├── kitti ==> Contains script for converting downloaded kitti dataset into YOLO format
│   └── nighttime ==> Contains scripts for converting downloaded night-time data into YOLO format and also visualization for night-time data.
│       └── vehicles-nighttime ==> Where the night-time data repo was downloaded to
│           ├── data ==> Empty folder where images used to be
│           └── labels ==> Empty folder where labels were generated to (generated from vehicles-nighttime/labels.txt)
├── models ==> Where each trained model was saved to
├── result_videos ==> The Bethlehem evaluation videos with bounding boxes drawn on
├── test_videos ==> The Bethlehem evaluation videos
└── yolov5
    ├── augmented_images ==> Empty folder where generated augmented images were placed
    ├── augmented_labels ==> Empty folder where generated augmented labels were placed
    ├── kitti.yaml ==> Contains class mapping (0 is car, 1 is ...)
    ├── kitti ==> Where the dataset was stored to
    │   ├── images ==> Training images
    │   ├── labels ==> Training labels
    │   ├── test_images ==> Testing images
    │   ├── test_labels ==> Testing labels
    │   └── test_labels_eval ==> Predicted labels on testing images
    ├── runs
    │   ├── detect ==> Output directory for detection related tasks.
    │       ├── expX
    │   └── train ==> Output directory for training related tasks
    │       ├── expX
    ├── utils ==> Bulk of YOLO training scripts. Modified to suit our tasks.
```

## Example Commands

### Training a model

```
# Start training process
cd yolov5
python train.py --data kitti.yaml --epochs 5 --batch-size 5 --weights yolov5s.pt --cache disk
# Save model weights
cp runs/exp{latest-exp-number}/best.pt ../models/new_model.pt
```

### Evaluating the model

```
# First argument is the model weights (no extension)
sh bulk_detection.sh noaug_nonight
# Will create predicted labels in test_labels_eval
# Then run the comparison script
python eval/intersection_over_union.py yolov5/kitti/test_labels yolov5/kitti/test_labels_eval
```

### Testing the model

#### Single Image

```
# First argument is the image ID, second is the model weights (no extension), third is the extension (optional, defaults to png)
sh detection.sh 000033 noaug_nonight png
# Will output the annotated image in output.png, the bounding boxes used in bbx.txt, and the ground-truth bounding boxes in label.txt
```

#### Bethlehem Videos

```
# First argument is the model weights (no extension)
sh video_running.sh noaug_nonight
# Outputs annotated videos in result_videos directory with same name as model weights. Videos are at 6 different light levels 
# (bright 1 <-> 6 dark)
```

### Augmenting Images

```
cd yolov5
# First argument is the image directory
# Second argument is the label directory
# Third argument is the number of images to augment (use -1 for all in directory) 
# Fourth argument is if the use night images (y|n). These images are distinguished by the img_ tag in the filename.
python augment.py tmp_images/ tmp_labels/ -1 y
# Then run the following to move the augmented images into the training directories.
mv augmented_images/*.png kitti/images && mv augmented_labels/*.txt kitti/labels
```

### Separating into Training/Testing Datasets

```
cd yolov5
# moves 20% of the images in kitti/images into kitti/test_images along with their corresponding labels from labels/ into test_labels
python segment.py 
# RECOMMENDED NOT TO RUN TWICE! 
# Reset the test directories before rerunning by moving the images from test_images and test_labels back to the original directories
```
