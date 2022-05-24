import re
import string
from collections import Counter, OrderedDict
from typing import List, Tuple

import torch
from torch.nn.utils.rnn import pad_sequence
from torchtext.vocab import Vocab, vocab

Tensor = torch.Tensor


def split_and_flat(corpus: List[str]) -> List[str]:
    corpus_ = [x.split() for x in corpus]
    corpus = [x for y in corpus_ for x in y]
    return corpus


def build_vocab(corpus: List[str], oov: str = "<OOV>", pad: str = "<PAD>") -> Vocab:
    data = split_and_flat(corpus)
    counter = Counter(data)
    ordered_dict = OrderedDict(counter)
    v1 = vocab(ordered_dict, specials=[pad, oov])
    v1.set_default_index(v1[oov])
    return v1


def tokenize(corpus: List[str], v: Vocab) -> Tensor:
    batch = []
    for sent in corpus:
        batch.append(torch.tensor([v[word] for word in sent.split()]))
    return pad_sequence(batch, batch_first=True)


class Preprocessor:
    def __init__(self, max: int, vocab: Vocab) -> None:
        self.max = max
        self.vocab = vocab

    def clean(self, text: str) -> str:
        punctuation = f"[{string.punctuation}]"
        # remove CaPiTaLs
        lowercase = text.lower()
        # change don't and isn't into dont and isnt
        neg = re.sub("\\'", "", lowercase)
        # swap html tags for spaces
        html = re.sub("<br />", " ", neg)
        # swap punctuation for spaces
        stripped = re.sub(punctuation, " ", html)
        # remove extra spaces
        spaces = re.sub("  +", " ", stripped)
        return spaces

    def cast_label(self, label: str) -> int:
        if label == "neg":
            return 0
        else:
            return 1

    def __call__(self, batch: List) -> Tuple[Tensor, Tensor]:
        labels, text = [], []
        for x, y in batch:
            x = self.clean(x).split()[: self.max]
            tokens = torch.tensor([self.vocab[word] for word in x])
            text.append(tokens)
            labels.append(self.cast_label(y))

        text_ = pad_sequence(text, batch_first=True, padding_value=0)
        return text_, torch.tensor(labels)