# Hamming-Code-8-4
Here we provide files with hamming (8, 4) encoding and decoding as a map.
Encoding and decoding are provided in both CSV and JSON format.

The python code that was used to generate the encodings is also provided, but it is not necessary for usage.

## Usage
You can use the files in whatever language you want. Here I show an example with python:
```python
encoding_map = pd.read_csv("https://raw.githubusercontent.com/EstevaoUyra/Hamming-Code-8-4/main/encoding.csv", dtype=str)
decoding_map = pd.read_csv("https://raw.githubusercontent.com/EstevaoUyra/Hamming-Code-8-4/main/decoding.csv", dtype=str)
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
