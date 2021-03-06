from unittest import TestCase
from os.path import dirname, join
from data import CONLLFactory

search_value = "DET-ADJ"

bk_treebank_file = join(dirname(dirname(__file__)), "tmp", "UD_Vietnamese-BKT2", "vi_bkt2-ud-train.conllu")
corpus = CONLLFactory.load_corpus_from_file(bk_treebank_file)


class TestSearch(TestCase):
    def test_search(self):
        output = corpus.search()
        output = [{"id": item.id, "content": item.content} for item in output]
        print(output)

    def test_search_pos(self):
        pos = ""
        output = corpus.search(pos)
        # output = corpus.search_pos(pos)
        output = [{"id": item.id, "content": item.content} for item in output]
        print(output)
