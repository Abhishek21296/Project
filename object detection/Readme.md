# Object Detection through OpenCV

OpenCV has a module named deep neural network (dnn) which allows loading pre-trained models from most populars deep learning frameworks, including Tensorflow, Caffe, Darknet, Torch.

Here we are using MobileNet SSD, a single shot detection method. Single Shot object detection or SSD takes one single shot to detect multiple objects within the image.
It composes of two parts

1. Extract feature maps
2. Apply convolution filter to detect objects

The MobileNet SSD method was first trained on the COCO dataset and was then fine-tuned on PASCAL VOC reaching 72.7% mAP (mean average precision).

## Program Flow
 
1. Open video file or capture device.
2. Load the Caffe model.
3. Resize image to 300x300 as the MobileNet required to have input of this shape.
4. Apply Mena subtraction to normalize image and then pass it to dnn.
5. Get the class and location of the detected objects and draw them.

## Links

MobileNet SSD Caffe model : [Model](https://drive.google.com/file/d/0B3gersZ2cHIxRm5PMWRoTkdHdHc/view)

MobileNet SSD Weights : [Weights](https://github.com/chuanqi305/MobileNet-SSD/blob/master/deploy.prototxt)