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
# First argument is the image ID, second is the model weights (no extension), third is the extension (optional, defaults to png)
sh detection.sh 000033 noaug_nonight png
# Will output the annotated image in output.png, the bounding boxes used in bbx.txt, and the ground-truth bounding boxes in label.txt
```

### Testing the model

```

```

### Augmenting Images

```
```

### Separating into Training/Testing Datasets

```
```
