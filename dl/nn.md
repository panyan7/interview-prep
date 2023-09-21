# Neural Networks

## CNN

## RNN/LSTM

- LSTM: deal with vanishing gradient problem. Forget gate assigns 0/1 weight to decide if we will forget, and input gate assigns 0/1 weight to decide if we should store information in the current state. 

## Dropout

- Prevents over-fitting by randomly drop out rows of the row vectors from the weight matrix.

## BatchNorm

- Normalize using the mean and variance of all the data in the batch for each dimension separately.
- Make training faster.

## LayerNorm

- Normalize using mean and variance of all the hidden units in a layer.
- Improve training and generalization.

## Model Compression

- Knowledge Distillation: Use the output of a complex model (teacher network) to train a simple model (student network).
- Low Rank Approximation
- Pruning: Add sparsity regularization to remove redundant weights.
- Quantitzation: Store tensors at lower bit-width to reduce model size.
