## YOLOv4 and Enhanced SRGAN
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

## Pretained Models
* YOLOv4:
  [(Download Link)](https://www.dropbox.com/s/8l4va3n1cu6ul8o/yolo4.zip?dl=0)
  
* ESRGAN: 
  [(Download Link)](https://www.dropbox.com/s/va58gkcfo8d0c9d/prdb.zip?dl=0)

## Usage
* Patch per datasets

    Example: 512×512
<p align="center">
<img src="img_512X512/PHIBD_2012_4_h0.png" width="120" title="512_1">
<img src="img_512X512/PHIBD_2012_4_r0.png" width="120" title="512_2">
<img src="img_512X512/PHIBD_2012_4_r1.png" width="120" title="512_3">
<img src="img_512X512/PHIBD_2012_4_r2.png" width="120" title="512_4">
<img src="img_512X512/PHIBD_2012_4_r3.png" width="120" title="512_5">
<img src="img_512X512/PHIBD_2012_4_v0.png" width="120" title="512_6">
</p>

```
    python3 image_to_256.py
    python3 image_to_512.py
```

* Discrete Wavelet Transform

    Example: Blue, Green, Red
<p align="center">
<img src="img_dwt/blue.bmp" width="240" title="blue">
<img src="img_dwt/green.bmp" width="240" title="green">
<img src="img_dwt/red.bmp" width="240" title="red">
</p>

```
    python3 image_dwt_original.py
    python3 image_dwt_256.py
```
* Train the model
```
    python3 train_stage2.py
    python3 predict_for_stage3.py
    python3 train_stage3.py
    python3 train_stage3_resize.py
```

* Evaluation the model
```
    python3 eval_stage3_all.py
```

## References
[Cropped Detection](https://github.com/GaoZiqiang/crop_objects_based_yolov4_pytorch)
[ESRGAN](https://github.com/xinntao/ESRGAN)
