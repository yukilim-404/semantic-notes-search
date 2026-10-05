"""Fill in the stage interfaces in your own workspace."""

import re
import unicodedata


def _clean(s):
    return unicodedata.normalize("NFC", s).casefold()


def normalize(text, aliases=None):
    if text is None:
        raise ValueError("text must not be None")
    words = re.findall(r"\w+", _clean(text))
    table = {_clean(k): _clean(v) for k, v in (aliases or {}).items()}
    return [table.get(w, w) for w in words]


def build_index(documents, aliases=None):
    raise NotImplementedError("build_index")


def search(index, query, k=3):
    raise NotImplementedError("search")


def evaluate(index, cases, k=3):
    raise NotImplementedError("evaluate")
