cd yolov5
if [ "$1" == "" ] || [ $# == 0 ]; then
        echo "Pass in the weights (without the extension) to use for evaluation (in models/)"
        exit
fi
if [ -d "runs/detect/exp" ]; then
  echo "Wiping runs/detect/exp"
  rm -r runs/detect/exp*
fi

python detect.py --data kitti.yaml --save-txt --source ../test_videos/1.mov --weights "../models/$1.pt" # &> /dev/null
python detect.py --data kitti.yaml --save-txt --source ../test_videos/2.mov --weights "../models/$1.pt" # &> /dev/null
python detect.py --data kitti.yaml --save-txt --source ../test_videos/3.mov --weights "../models/$1.pt" # &> /dev/null
python detect.py --data kitti.yaml --save-txt --source ../test_videos/4.mov --weights "../models/$1.pt" # &> /dev/null
python detect.py --data kitti.yaml --save-txt --source ../test_videos/5.mov --weights "../models/$1.pt" # &> /dev/null
python detect.py --data kitti.yaml --save-txt --source ../test_videos/6.mov --weights "../models/$1.pt" # &> /dev/null

mv runs/detect/exp/1.mp4 ../result_videos/$11.mp4
mv runs/detect/exp2/2.mp4 ../result_videos/$12.mp4
mv runs/detect/exp3/3.mp4 ../result_videos/$13.mp4
mv runs/detect/exp4/4.mp4 ../result_videos/$14.mp4
mv runs/detect/exp5/5.mp4 ../result_videos/$15.mp4
mv runs/detect/exp6/6.mp4 ../result_videos/$16.mp4
