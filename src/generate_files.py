from itertools import product
import numpy as np
import pandas as pd
from algorithm import encode_hamming_8_4, decode_hamming_8_4, decode_hamming_8_4_with_guess, possible_4bit, possible_8bit

encodings = {}
for message in possible_4bit:
    encoded = encode_hamming_8_4(message)
    encodings[message] = encoded
enc = pd.Series(encodings).rename('encoded_message').sort_values()
enc.index = enc.index.rename('message')
enc.to_csv('./maps_8_4/encoding.csv')
enc.to_json('./maps_8_4/encoding.json', indent=2)


decodings = {}
for message in possible_8bit:
    decoded = decode_hamming_8_4(message)
    decodings[message] = decoded
dec = pd.Series(decodings).rename('message').sort_values()
dec.index = dec.index.rename('encoded_message')
dec.to_csv('./maps_8_4/decoding.csv')
dec.to_json('./maps_8_4/decoding.json', indent=2)


gdecodings = {}
for message in possible_8bit:
    decoded = decode_hamming_8_4_with_guess(message)
    gdecodings[message] = decoded
gdec = pd.Series(gdecodings).rename('message').sort_values()
gdec.index = gdec.index.rename('encoded_message')
gdec.to_csv('./maps_8_4/decoding_guess.csv')
gdec.to_json('./maps_8_4/decoding_guess.json', indent=2)






