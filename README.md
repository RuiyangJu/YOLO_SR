# YOLOv4 and Enhanced SRGAN

### Example of Input Image
<p align="center">
  <img src="Yolo_SR/input/example.jpg" width="640" title="input">
</p>

### Example of Detection Image
<p align="center">
  <img src="Yolo_SR/yolo_detection/det_img_example.jpg" width="640" title="detection">
</p>

### Example of cropped Image
<p align="center">
  <img src="Yolo_SR/yolo_output/croped_img_example_0.jpg" width="120" title="cropped">
  <img src="Yolo_SR/yolo_output/croped_img_example_1.jpg" width="120" title="cropped">
  <img src="Yolo_SR/yolo_output/croped_img_example_2.jpg" width="120" title="cropped">
  <img src="Yolo_SR/yolo_output/croped_img_example_3.jpg" width="120" title="cropped">
  <img src="Yolo_SR/yolo_output/croped_img_example_4.jpg" width="120" title="cropped">
</p>

### Example of final Image
<p align="center">
  <img src="Yolo_SR/final_output/croped_img_example_0_rlt.png" width="120" title="final">
  <img src="Yolo_SR/final_output/croped_img_example_1_rlt.png" width="120" title="final">
  <img src="Yolo_SR/final_output/croped_img_example_2_rlt.png" width="120" title="final">
  <img src="Yolo_SR/final_output/croped_img_example_3_rlt.png" width="120" title="final">
  <img src="Yolo_SR/final_output/croped_img_example_4_rlt.png" width="120" title="final">
</p>

## Trained Models
Use gdown to download the trained model from our GitHub:
```
gdown https://github.com/RuiyangJu/YOLO_SR/releases/download/Trained_Model/Trained_Model.zip
```

## Usage
* YOLOv4 pretrained models in [Yolo_SR/model_data]
* ESRGAN pretrained models in [Yolo_SR/models]
* Object Detection
```
    python3 yolo_test.py
```
* Super-resolution
```
    python3 SR_test.py
```

## References
* [Cropped Detection YOLOv4](https://github.com/GaoZiqiang/crop_objects_based_yolov4_pytorch)
* [Super-Resolution ESRGAN](https://github.com/xinntao/ESRGAN)
