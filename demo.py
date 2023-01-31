from parrot import Parrot
parrot = Parrot()
import torch
import warnings
warnings.filterwarnings("ignore")

def random_state(seed):
  torch.manual_seed(seed)
  if torch.cuda.is_available():
    torch.cuda.manual_seed_all(seed)

random_state(1234)

parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5")

phrases = [
     ('Many of you may be familiar with Python as a programming language,'
     ' but don\'t know much about it')
]
for phrase in phrases:
  print('-'*110)
  print('Input Phrase:', phrase)
  print('-'*110)
  paraphrases = parrot.augment(input_phrase=phrase)
  if paraphrases:
    for paraphrase in paraphrases:
      print(paraphrase)