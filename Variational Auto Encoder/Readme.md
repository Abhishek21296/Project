# Variational Autoencoder

Variational Autoencoders are a type of generative model that's especially appropriate for task of image editing via concept vectors.

A classical image autoencoder  takes an image, maps it to a latent vector space via encoder module, and then decodes it back to an output with the same dimensions as the original image, via decoder module. It's then trained by using as target data the same images as the inputs images, meaning the autoencoder learns to reconstruct the original inputs.

## VAE architecture

We're using mnist handwritten digit dataset, a 10 class 60000 image dataset of 28x28x1 images.

Encoder network:
1. Input image of shape [28,28,1].
2. Convolution layer with 32 filters and 3x3 kernel.
3. Convolution layer with 64 filters and 3x3 kernel.
4. Convolution layer with 64 filters and 3x3 kernel.
5. Convolution layer with 64 filters and 3x3 kernel.
6. Dense layer after flatten() with 32 units.
7. Output layer (dense with units = latent dimension).

Decoder Network:
1. Input layer with input vector (latent dimension).
2. Dense layer to convert vector to the shape from encoder before flattening.
3. Convolution Transpose layer with 32 filters and 3x3 kernel and a stride of 2.
4. Convolution layer with 1 filter and 3x3 kernel.