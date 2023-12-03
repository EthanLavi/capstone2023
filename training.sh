cd yolov5
python train.py --data kitti.yaml --epochs 15 --batch-size 5 --weights yolov5s.pt --imgsz 672 384 --rect
