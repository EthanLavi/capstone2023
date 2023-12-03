# Skillion Capstone 2023

## Directory Structure (Important Folders Only)
```
bulk_detection.sh ==> Will use a model from the models folder on the entirety of the test dataset. Creating and moving the files into the proper location.
├── eval ==> Contains script for comparing test_labels_eval and test_labels to graph IOU for the model.
├── models ==> Where each trained model was saved to
├── result_videos ==> The Bethlehem evaluation videos with bounding boxes drawn on
├── test_videos ==> The Bethlehem evaluation videos
└── yolov5
    segment.py ==> A script for splitting data from the images folder into the test_images folder (also will move labels)
    augment.py ==> A script for taking a group of images/labels and augmenting them. Results will be placed in the next 2 folders.
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
python train.py --data kitti.yaml --epochs N --batch-size 5 --weights yolov5s.pt --img 416
# Save model weights
cp runs/exp{latest-exp-number}/best.pt ../models/new_model.pt
```

### Evaluating the model

```
# First argument is the model weights
sh bulk_detection.sh models/noaug_nonight.pt
# Will create predicted labels in test_labels_eval
# Then run the comparison script
python eval/intersection_over_union.py yolov5/kitti/test_labels yolov5/kitti/test_labels_eval
```

### Testing the model

#### Single Image

```
# First argument is the image ID, second is the model weights (no extension), third is the extension for the image (optional, defaults to png)
sh detection.sh 000033 final png
# Will output the annotated image in output.png, the bounding boxes used in bbx.txt, and the ground-truth bounding boxes in label.txt
```

#### Bethlehem Videos

```
# First argument is the model weights (no extension)
sh video_running.sh final
# Outputs annotated videos in result_videos directory with same name as model weights. Videos are at 6 different light levels 
# (bright 1 <-> 6 dark)
```

### Augmenting Images

```
cd yolov5
# First argument is the image directory
# Second argument is the label directory
# Third argument is the number of images to augment (use -1 for all in directory) 
# Fourth argument is if the use night images (y|n). These images are distinguished by the img_ tag in the filename. This last argument is helpful if you want to filter images from a directory (can just run twice, once with y, once with n, to get all the images). 
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
