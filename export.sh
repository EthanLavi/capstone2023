cd yolov5
if [ "$1" == "" ] || [ $# == 0 ]; then
        echo "Pass in the weights to use for evaluation (fullpath, models/) with extension"
        exit
fi
python export.py --weights ../$1 --include torchscript onnx 