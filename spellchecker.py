import time
from multiprocessing import Pool
from transformers import pipeline

class SpellChecker():
    def __init__(self):
        pass
        # MODEL_NAME = 'SajjadAyoubi/distil-bigbird-fa-zwnj'
        # self.fill = pipeline('fill-mask', model=MODEL_NAME, tokenizer=MODEL_NAME)
    
    def do_spellcheck(self, token_index):
        masked_str = [
            self.tokens[i] if i!=token_index else "[MASK]"
            for i in range(len(self.tokens))
        ]
        # print()
        print(masked_str)

    def do_spellcheking_parallelly(self, query):
        self.tokens = query.split(" ")
        tokens_indexes = [i for i in range(len(self.tokens))]
        pool = Pool(processes=3)
        pool.map(self.do_spellcheck, (tokens_indexes))

if __name__ == "__main__":
    spellchecker = SpellChecker()
    spellchecker.do_spellcheking_parallelly("قسم که پس بگیرمت")
