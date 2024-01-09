# Hamming-Code-8-4
## What it is
Hamming code (8,4) enables us to send 4-bit messages through a 8-bit channel with noise correction.
The code is robust against any 1-bit flip. Useful for serial port messaging, among other things.

Here we provide files with hamming (8, 4) encoding and decoding as simple maps.
Take a look at `encoding.csv`, and see how the message `1110`, for example, should be encoded into `00101100`.
``` 
message,encoded_message
0000,00000000
0111,00011110
1110,00101100
```
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
