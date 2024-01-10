# Hamming Code Maps
- JSON and CSV mappings for Hamming Codes (in `maps_8_4`)
- Not specific to a programming language (the code in `src` was used to generate and validate the mappings)
- Suggested use: download the mappings or access directly through github raw (see **Usage** below)

## What it is
Hamming codes are a family of linear error-correcting codes that were introduced by Richard Hamming in 1950. They are used to detect and correct errors within data that can occur during transmission or storage. Hamming codes are particularly effective for applications where the error rate is relatively low, but reliability is crucial, such as in digital communication and data storage systems.

This repository focuses on the Hamming Code (8,4) variant. It allows the transmission of 4-bit messages through an 8-bit channel, providing single-bit error correction and double-bit error detection capabilities. This makes it an ideal choice for scenarios like serial port messaging, where robust error correction is necessary.

We provide mapping files for both encoding and decoding using the Hamming (8,4) code. These maps are available in both CSV and JSON formats for ease of use in various programming environments. For instance, the *`encoding.csv`* file demonstrates how a 4-bit message like `'1110'` is encoded into an 8-bit Hamming code `'00101100'`.

Example from *`encoding.csv`*:

```csv
message,encoded_message
0000,00000000
0111,00011110
1110,00101100
```

The python code that was used to generate the encodings is also provided, but it is not necessary for usage.
## Usage
You can use the files in whatever language you want. Here I show an example with python:
```python
encoding_map = pd.read_csv("https://raw.githubusercontent.com/EstevaoUyra/Hamming-Code-8-4/main/maps_8_4/encoding.csv", dtype=str)
decoding_map = pd.read_csv("https://raw.githubusercontent.com/EstevaoUyra/Hamming-Code-8-4/main/maps_8_4/decoding.csv", dtype=str)
encode = lambda s: encoding_map[encoding_map.message==s].encoded_message.values[0]
decode = lambda s: decoding_map[decoding_map.encoded_message==s].message.values[0]
```


```python
>>> encode('0001')
```
Output: `'11010010'`

```python
>>> decode('11010010')
```
Output: `'0001'`

## What if there is more than one flip
- With 1 flip, the message is recovered with 100% accuracy.
- With 3 flips, the message is irrecoverable and undetectable
- With 2 flips, we can either detect with 100% accuracy or recover with 25%.

We provide two decoding mappings, depending on how you want to deal with uncorrectable errors (i.e. when 2 bits are flipped). 
1. `decoding` detects 100% of 2-flip errors, returning an error message.
2. `decoding_guess` tries to correct the 2-flip errors to the most probable message, getting it right 25% of the time. 

We ran validation in `src/test_performance.py`. You can see that the encodings provided are 100% robust to single flips.

flips|correct|guess_correct
---|---|---
0|100%|100%
1|100%|100%
2|0%|25%

