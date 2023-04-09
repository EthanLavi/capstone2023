cd yolov5
if [ "$1" == "" ] || [ $# -gt 1 ]; then
        echo "Pass in the image file (000008.png for example) as the first argument. Don't include extenstion"
        exit
fi
if [ -d "runs/detect/exp" ]; then
  echo "Wiping runs/detect/exp"
  rm -r runs/detect/exp*
fi

python detect.py --data kitti.yaml --save-txt --source kitti/images/$1.png --weights "../best.pt" &> /dev/null
echo "Model inference results saved to output.png, bbx.txt, and label.txt"
mv runs/detect/exp*/$1.png ../output.png
mv runs/detect/exp*/labels/$1.txt ../bbx.txt
cp kitti/labels/$1.txt ../label.txt