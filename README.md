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

## Abstract
The efficient segmentation of foreground text information from the background in degraded color document images is a topic of concern. Due to the imperfect preservation of ancient documents over a long period of time, various types of degradation, including staining, yellowing, and ink seepage, have seriously affected the results of image binarization. In this paper, a three-stage method is proposed for image enhancement and binarization of degraded color document images by using discrete wavelet transform (DWT) and generative adversarial network (GAN). In Stage-1, we use DWT and retain the LL subband images to achieve the image enhancement. In Stage-2, the original input image is split into four (Red, Green, Blue and Gray) single-channel images, each of which trains the independent adversarial networks. The trained adversarial network models are used to extract the color foreground information from the images. In Stage-3, in order to combine global and local features, the output image from Stage-2 and the original input image are used to train the independent adversarial networks for document binarization. The experimental results demonstrate that our proposed method outperforms many classical and state-of-the-art (SOTA) methods on the Document Image Binarization Contest (DIBCO) dataset.

## Dataset
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
[DocumentBinarization](https://github.com/opensuh/DocumentBinarization)
