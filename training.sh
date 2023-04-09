cd yolov5
touch ../training_output.txt
python train.py --data kitti.yaml --epochs 5 --batch-size 5 --weights yolov5s.pt &> ../training_output.txt