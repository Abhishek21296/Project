# MNIST Hand written digit recognition

Keras model designed to achieve  Validation score of 99%+ (which in our case is 99.3%) while having only around ~8K(8048) parameters.

The model is trained on 57000 images and validated on 3000 images.

## Model architecture

1. Convolution layer with 4 filters
2. Convolution layer with 4 filters
3. Convolution layer with 5 filters
4. Average pooling layer with 3x3 kernel and 2x2 stride
5. Dense layer with 15 units and 10% dropout
6. Output Layer (10 units)

## Callbacks

1. 'ReduceLROnPlateau' to reduce the learning rate when a local mimima is achieved.
2. 'EarlyStopping' to stop if validation accuracy stops increasing.