<p align="center">
<img src="https://github.com/karkaroff/hedwig/blob/bellatrix/docs/hedwig.png" width="360">
</p>

这个repo包含the Data Systems Group at the University of Waterloo 用于文档分类的PyTorch深度学习模型。

## Models

+ [DocBERT](models/bert/) : DocBERT: BERT模型文档分类 [(Adhikari et al., 2019)](https://arxiv.org/abs/1904.08398v1)
+ [Reg-LSTM](models/reg_lstm/): Regularized LSTM 文档分类  [(Adhikari et al., NAACL 2019)](https://cs.uwaterloo.ca/~jimmylin/publications/Adhikari_etal_NAACL2019.pdf)
+ [XML-CNN](models/xml_cnn/): CNNs for extreme multi-label text classification [(Liu et al., SIGIR 2017)](http://nyc.lti.cs.cmu.edu/yiming/Publications/jliu-sigir17.pdf)
+ [HAN](models/han/): Hierarchical Attention Networks [(Zichao et al., NAACL 2016)](https://www.cs.cmu.edu/~hovy/papers/16HLT-hierarchical-attention-networks.pdf)
+ [Char-CNN](models/char_cnn/): Character-level Convolutional Network [(Zhang et al., NIPS 2015)](http://papers.nips.cc/paper/5782-character-level-convolutional-networks-for-text-classification.pdf)
+ [Kim CNN](models/kim_cnn/): CNNs for sentence classification [(Kim, EMNLP 2014)](http://www.aclweb.org/anthology/D14-1181)

每个模型目录都有一个“ README.md”，其中包含更多详细信息。

## Setting up PyTorch

Hedwig is designed for Python 3.6 and [PyTorch](https://pytorch.org/) 0.4.
PyTorch recommends [Anaconda](https://www.anaconda.com/distribution/) for managing your environment.
我们建议创建一个自定义环境，如下所示：

```
$ conda create --name castor python=3.6
$ source activate castor
```

And installing PyTorch as follows:

```
$ conda install pytorch=0.4.1 cuda92 -c pytorch
```

Other Python packages we use can be installed via pip:

```
$ pip install -r requirements.txt
```

代码取决于NLTK中的数据（例如停用词），因此您必须下载它们。
运行Python解释器并输入以下命令：

```python
>>> import nltk
>>> nltk.download()
```

## Datasets

有两种下载Reuters，AAPD和IMDB数据集以及word2vec嵌入的方法：

Option 1. Our [Wasabi](https://wasabi.com/)-hosted mirror:

```bash
$ wget http://nlp.rocks/hedwig -O hedwig-data.zip
$ unzip hedwig-data.zip
```

Option 2. Our school-hosted repository, [`hedwig-data`](https://git.uwaterloo.ca/jimmylin/hedwig-data):

```bash
$ git clone https://github.com/castorini/hedwig.git
$ git clone https://git.uwaterloo.ca/jimmylin/hedwig-data.git
```

接下来，按以下方式组织目录结构：

```
.
├── hedwig
└── hedwig-data
```
克隆hedwig-data存储库后，您需要解压缩嵌入内容并运行预处理脚本：

```bash
cd hedwig-data/embeddings/word2vec 
gzip -d GoogleNews-vectors-negative300.bin.gz
```

**If you are an internal Hedwig contributor using the machines in the lab, follow the instructions [here](docs/internal-instructions.md).**
