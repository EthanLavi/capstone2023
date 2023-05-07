rm output.png &> /dev/null
rm output.jpg &> /dev/null
cd yolov5
if [ "$1" == "" ] || [ $# -gt 2 ]; then
        echo "Pass in the image file (000008.png for example) as the first argument. Include extenstion as second arg (default png)"
        exit
fi
if [ -d "runs/detect/exp" ]; then
  echo "Wiping runs/detect/exp"
  rm -r runs/detect/exp*
fi
EXT="png"
if [ "$2" != "" ] && [ $# -lt 3 ]; then
        EXT=$2
fi

python detect.py --data kitti.yaml --save-txt --source kitti/images/$1.$EXT --weights "../models/old.pt" # &> /dev/null
echo "Model inference results saved to output.$EXT, bbx.txt, and label.txt"
mv runs/detect/exp*/$1.$EXT ../output.$EXT
mv runs/detect/exp*/labels/$1.txt ../bbx.txt
cp kitti/labels/$1.txt ../label.txt