import pandas as pd
from algorithm import hamming_distance, possible_8bit, possible_4bit

encoding_map = pd.read_csv("../maps_8_4/encoding.csv", dtype=str)
decoding_map = pd.read_csv("../maps_8_4/decoding.csv", dtype=str)
decoding_guess_map = pd.read_csv("../maps_8_4/decoding_guess.csv", dtype=str)
encode = lambda s: encoding_map[encoding_map.message==s].encoded_message.values[0]
decode = lambda s: decoding_map[decoding_map.encoded_message==s].message.values[0]
gecode = lambda s: decoding_guess_map[decoding_guess_map.encoded_message==s].message.values[0]

def test_encoding(encoding_row):
    """Evaluates the decoding performance for all 1-bit and 2-bit errors"""
    message = encoding_row.message
    encoded_message = encoding_row.encoded_message
    
    comparisons = pd.DataFrame({'noisy': possible_8bit, 'message': message})
    comparisons['flips'] = comparisons.noisy.apply(lambda s: hamming_distance(s, encoded_message))
    comparisons['decoded'] = comparisons.noisy.apply(lambda s: decode(s))
    comparisons['guess_decoded'] = comparisons.noisy.apply(lambda s: gecode(s))
    comparisons['correct'] = comparisons.message == comparisons.decoded
    comparisons['guess_correct'] = comparisons.message == comparisons.guess_decoded
    return comparisons.groupby('flips')[['correct', 'guess_correct']].mean().query('flips <= 2').stack()

res = encoding_map.apply(test_encoding, axis=1).assign(message=encoding_map.message).set_index('message').min().unstack()
(
    ((res*100).astype(int).astype(str)+'%').to_csv('../decoding_performance.csv', sep='|')
)
