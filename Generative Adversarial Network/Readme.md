# Generative Adversarial Network

GAN, introduced in 2014 by Ian Goodfellow is an alternative to VAEs for learning latent space of images. They enable generation of fairly realistic synthetic images by forcing the generated images to be statistically almost indistinguishable from real ones.

A GAN is made of two parts:
1. Generator Network - takes input a random vector, and decodes its into synthetic image.
2. Discriminator Network - takes input an image and predicts whether the image came from training set or was created by generator network.

The generator network is trained to  be able to fool the discriminator network, and thus evolves toward generating realistic images as training goes on: artificial images that look indistinguishable from real ones, to the extent that it's impossible for the discriminator network to tell the two apart. Meanwhile, the discriminator is constantly adapting to the gradually increasing capabilities of the generator, setting a high bar of realism for the generated images.

this is what a GAN is: a forger network and an expert network, each being trained to best each other.

## GAN architecture

We're using cifar10, a 10 class 50000 image dataset of 32x32x3 images.

Generator network:
1. Input vector of shape [32,].
2. Dense layer which converts input vector to shape of 16x16x128.
3. Convolution Layer with 256 filters and 5x5 kernel.
4. Convolution transpose layer with 256 filters and 4x4 kernel.
5. Convolution layer with 256 filters and 5x5 kernel.
6. Convolution layer with 256 filters and 5x5 kernel.
7. Output convolution layer with 3 filters with 7x7 kernel to generate final image.

Discriminator Network:
1. Input layer with input dimension (32,32,3).
2. Convolution layer with 128 filters and 3x3 kernel.
3. Convolution layer with 128 filters and 4x4 kernel and a stride of 2.
4. Convolution layer with 128 filters and 4x4 kernel and a stride of 2.
5. Convolution layer with 128 filters and 4x4 kernel and a stride of 2.
6. Output layer (Dense with one unit and 40% dropout after flatten()).