import os

import models.args


def get_args():
    parser = models.args.get_args()
    parser.add_argument('--model', default=None, type=str, required=True, help='使用的模型，例如bert-base-uncased')
    parser.add_argument('--dataset', type=str, default='SST-2', choices=['SST-2', 'AGNews', 'Reuters', 'AAPD', 'IMDB', 'Yelp2014'],help='可使用的数据集，事先下载好数据集')
    parser.add_argument('--save-path', type=str, default=os.path.join('model_checkpoints', 'bert'),help='保存模型路径')
    parser.add_argument('--cache-dir', default='cache', type=str,help='cache路径')
    parser.add_argument('--trained-model', default=None, type=str,help='使用训练好的模型继续训练')
    parser.add_argument('--fp16', action='store_true', help='use 16-bit floating point precision')

    parser.add_argument('--max-seq-length',
                        default=128,
                        type=int,
                        help='经过WordPiece tokenization之后的输入序列的最大长度 \n'
                             '大于此长度会被truncated,小于此长度会被padded')

    parser.add_argument('--warmup-proportion',
                        default=0.1,
                        type=float,
                        help='执行线性学习率的warmup的比例')

    parser.add_argument('--gradient-accumulation-steps',
                        type=int,
                        default=1,
                        help='在执行backward/update前梯度累计的步数')

    parser.add_argument('--loss-scale',
                        type=float,
                        default=0,
                        help='Loss scaling to improve fp16 numeric stability. Only used when fp16 set to True.\n'
                             '0 (default value): dynamic loss scaling.\n'
                             'Positive power of 2: static loss scaling value.\n')

    args = parser.parse_args()
    return args
