# DocBERT

Finetuning the pre-trained [BERT](https://arxiv.org/abs/1810.04805) models for Document Classification tasks.

## Quick start

要在Reuters数据集上微调预训练的基于BERT的模型，只需在项目工作目录中运行以下命令即可。

```
python -m models.bert --dataset Reuters --model bert-base-uncased --max-seq-length 256 --batch-size 16 --lr 2e-5 --epochs 30
```

The best model weights will be saved in

```
models/bert/saves/Reuters/best_model.pt
```

要测试模型，可以使用以下命令。

```
python -m models.bert --dataset Reuters --model bert-base-uncased --max-seq-length 256 --batch-size 16 --lr 2e-5 --epochs 30 --trained-model models/bert/saves/Reuters/best_model.pt
```

## Model Types 

We follow the same types of models as in [huggingface's implementation](https://github.com/huggingface/pytorch-pretrained-BERT.git)
- bert-base-uncased
- bert-large-uncased
- bert-base-cased
- bert-large-cased

## Dataset

我们在以下数据集上对该模型进行实验：

- Reuters (ModApte)
- AAPD
- IMDB
- Yelp 2014

## Settings

Finetuning procedure can be found in :
- [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805)
- [DocBERT: BERT for Document Classification](https://arxiv.org/abs/1904.08398v1)

## Acknowledgement
- Our implementation is inspired from [huggingface's implementation](https://github.com/huggingface/pytorch-pretrained-BERT.git)
