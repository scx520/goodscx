python detect.py  ^
 --cfg cfg/yolov4-tiny.cfg ^
 --weights weights/yolov4-tiny.pt ^
 --names datasets/face.names ^
 --source imgs/  ^
 --img-size 640 ^
 --iou-thres 0.1 ^
 --conf-thres 0.1 ^
 --device 0