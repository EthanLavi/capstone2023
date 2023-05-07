# Skillion Capstone 2023

## Directory Structure
```
├── eval
├── labeling
│   ├── kitti
│   │   └── __pycache__
│   └── nighttime
│       ├── __pycache__
│       └── vehicles-nighttime
│           ├── data
│           └── labels
├── models
├── result_videos
├── test_videos
└── yolov5
    ├── augmented_images
    ├── augmented_labels
    ├── classify
    ├── data
    │   ├── hyps
    │   ├── images
    │   └── scripts
    ├── kitti
    │   ├── images
    │   ├── labels
    │   ├── test_images
    │   ├── test_labels
    │   └── test_labels_eval
    ├── models
    ├── runs
    │   ├── detect
    │       ├── expX
    │   └── train
    │       ├── expX
    ├── segment
    ├── utils
    └── yolov5
        └── runs
            └── train
                └── exp5
                    └── weights
```

## Example Commands

### Training a model

```
# Start training process
cd yolov5
python train.py --data kitti.yaml --epochs 5 --batch-size 5 --weights yolov5s.pt --cache disk
# Save model weights
cp yolov5/runs/exp{latest-exp-number}/best.pt ../models/new_model.pt
```

### Evaluating the model

```
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
