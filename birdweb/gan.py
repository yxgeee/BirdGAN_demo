import torch
import os,sys

dir_path = (os.path.abspath(os.path.join(os.path.realpath(__file__), '../../AttnGAN/code')))
sys.path.append(dir_path)
from generate import init_models,gen_example

__all__ = ["gan"]

_g = None

class _Attngan(object):
	def __init__(self, cfg_file):
		wordtoix, algo=init_models(cfg_file)
		self.wordtoix = wordtoix
		self.algo = algo
		
	def gan(self, sent):
		return gen_example(self.wordtoix, self.algo, sent)

if _g is None:
    _g = _Attngan('AttnGAN/code/cfg/eval_bird.yml')

def gan(sent):
    return _g.gan(sent)