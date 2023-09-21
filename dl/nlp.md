# Language Models

## TF-IDF

- DF: document frequency, the number of documents that a word appears
- TF: term frequency, the number of times a word appears in the target document

## BERT

- Bidirectional transformer
- Pre-trained on masked language modeling and next structure prediction
- Mask is generated during data preprocessing

## RoBERTa

- Trained on 10x larger dataset than BERT
- Masked language modeling only, but dynamic mask

## T5

- T5 is an encoder-decoder model pre-trained on a multi-task mixture of unsupervised and supervised tasks and for which each task is converted into a text-to-text format. T5 works well on a variety of tasks out-of-the-box by prepending a different prefix to the input corresponding to each task