cd yolov5
if [ "$1" == "" ] || [ $# == 0 ]; then
        echo "Pass in the weights to use for evaluation (in models/)"
        exit
fi
if [ -d "runs/detect/exp" ]; then
  echo "Wiping runs/detect/exp"
  rm -r runs/detect/exp*
fi

python detect.py --data kitti.yaml --save-txt --source kitti/test_images --weights "../$1" # &> /dev/null
echo "Model inference results saved to kitti/test_labels_eval"
rm kitti/test_labels_eval/*.txt
mkdir -p kitti/test_labels_eval
mv runs/detect/exp/labels/*.txt kitti/test_labels_eval
echo "Proceed to run eval/intersection_over_union.py"