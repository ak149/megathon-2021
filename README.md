# Face Mask Detector

# Description
Output CSV Files are in the output folder 

# Input Videos
- [Input Videos](https://www.youtube.com/playlist?list=PLEOgpsXy3CIqjKcKj9OWFBabJbAzCTrDu)

# Output Videos
- [Output Videos](https://www.youtube.com/playlist?list=PLEOgpsXy3CIoBXnbYW73jrJ859tBp0ujd)

# Instructions to Run
1. Clone the repository: ```git clone https://github.com/AmoghTiwari/megathon_2021 ```
2. Run ```pip install -e .``` in the parent directory
3. Download yolov4-face_mask.weights file from https://drive.google.com/drive/folders/1D5juJ9QHlnGq4Ph4DPhzlTY4hYwUdXTs?usp=sharing 	and place it inside yolov4-mask-detector folder
4. Run the python command ```python3 main.py -y yolov4-mask-detector -i input/airport.mp4 -o output/airport.mp4 -u 1```
	* In case you get an segmentation fault, try running the above command with ```-d``` flag set to ```0``` i.e., run this: ```python3 main.py -y yolov4-mask-detector -i input/airport.mp4 -o output/airport.mp4 -u 1 -d 0```
5. For Further inputs download the input videos from youtube link and place them in a folder named input

# Training Instructions
- Download the dataset folder from here: https://drive.google.com/drive/folders/1D5juJ9QHlnGq4Ph4DPhzlTY4hYwUdXTs?usp=sharing
- Place the dataset folder in the parent directory
- Clone the darknet github repository [Darknet github Repo](https://github.com/AlexeyAB/darknet)
- Preparation:
	- We'll need a ```obj.names``` and a ```obj.data``` file which contain details about the data. They are already present in the repository
	- We'll need a ```.cfg``` config file. This too is already provided in this repo
	- ```train.txt``` and ```test.txt file```: Files with absolute paths to the images. These too are already given in the repository
- Final Training
``` !./darknet detector train data/face_mask.data cfg/face_mask.cfg backup/face_mask_last.weights -dont_show -i 0 -map ```
**Note:** The above instructions are for linux. For windows, we'll need to use ```darknet.exe``` in place of ```./darknet``` in the above command

# References
- [YOLOv3 Article](https://towardsdatascience.com/face-mask-detection-using-darknets-yolov3-84cde488e5a1)
- [YOLOv4 Paper](https://arxiv.org/abs/2004.10934)
- [YOLO Inference with GPU Article](https://www.pyimagesearch.com/2020/02/10/opencv-dnn-with-nvidia-gpus-1549-faster-yolo-ssd-and-mask-r-cnn/)
- [Darknet github Repo](https://github.com/AlexeyAB/darknet)