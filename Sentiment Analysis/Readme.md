# IMDB Sentiment Classifiction

The following model is designed to classify the imdb movie reviews as positive or negative. Its a bi-class classification on text input using LSTM. The model has achieved testing accuracy of 88.4 percent in 10 epochs only and can be increased by fine tuning the model itself.

## Model Architecture
 
1. Embedding Layer with wiehts from pre-trained (100D GloVe) word embedding.
2. LSTM layer with 100 units.
3. Output with one unit.

## Links

GloVe : [Link](https://nlp.stanford.edu/projects/glove/)