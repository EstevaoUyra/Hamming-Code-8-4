from itertools import product
import numpy as np
import pandas as pd
from .algorithm import encode_hamming_8_4, decode_hamming_8_4

possible_8bit = [''.join(l) for l in list(product(*[['0','1'] for i in range(8)]))]
possible_4bit = [''.join(l) for l in list(product(*[['0','1'] for i in range(4)]))]

encodings = {}
for message in possible_4bit:
    encoded = encode_hamming_8_4(message)
    encodings[message] = encoded
enc = pd.Series(encodings).rename('encoded_message').sort_values()
enc.index = enc.index.rename('message')

decodings = {}
for message in possible_8bit:
    decoded = decode_hamming_8_4(message)
    decodings[message] = decoded
dec = pd.Series(decodings).rename('message').sort_values()
dec.index = dec.index.rename('encoded_message')

enc.to_csv('encoding.csv')
enc.to_json('encoding.json', indent=2)
dec.to_csv('decoding.csv')
dec.to_json('decoding.json', indent=2)
