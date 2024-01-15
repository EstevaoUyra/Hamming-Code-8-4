from itertools import product
import numpy as np
import pandas as pd
from algorithm import encode_hamming_8_4, decode_hamming_8_4, decode_hamming_8_4_with_guess, possible_4bit, possible_8bit

encodings = {}
for message in possible_4bit:
    encoded = encode_hamming_8_4(message)
    encodings[message] = encoded
enc = pd.Series(encodings).rename('encoded_message').sort_index()
enc.index = enc.index.rename('message')
enc.to_csv('./maps_8_4/encoding.csv')
enc.to_json('./maps_8_4/encoding.json', indent=2)
enc_int = enc.reset_index().applymap(lambda x: int(x, 2)).set_index('message')
enc_int.to_csv('./maps_8_4/int_encoding.csv')
enc_int.to_json('./maps_8_4/int_encoding.json', indent=2)

decodings = {}
for message in possible_8bit:
    decoded = decode_hamming_8_4(message)
    decodings[message] = decoded
dec = pd.Series(decodings).rename('message').sort_values()
dec.index = dec.index.rename('encoded_message')
dec.to_csv('./maps_8_4/decoding.csv')
dec.to_json('./maps_8_4/decoding.json', indent=2)
dec_int = dec.reset_index().applymap(lambda x: int(x, 2) if 'error' not in x else x).set_index('encoded_message')
dec_int.to_csv('./maps_8_4/int_decoding.csv')
dec_int.to_json('./maps_8_4/int_decoding.json', indent=2)

gdecodings = {}
for message in possible_8bit:
    decoded = decode_hamming_8_4_with_guess(message)
    gdecodings[message] = decoded
gdec = pd.Series(gdecodings).rename('message').sort_values()
gdec.index = gdec.index.rename('encoded_message')
gdec.to_csv('./maps_8_4/decoding_guess.csv')
gdec.to_json('./maps_8_4/decoding_guess.json', indent=2)
gdec_int = gdec.reset_index().applymap(lambda x: int(x, 2) if 'error' not in x else x).set_index('encoded_message')
gdec_int.to_csv('./maps_8_4/int_decoding_guess.csv')
gdec_int.to_json('./maps_8_4/int_decoding_guess.json', indent=2)





