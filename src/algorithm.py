from itertools import product
possible_8bit = [''.join(l) for l in list(product(*[['0','1'] for i in range(8)]))]
possible_4bit = [''.join(l) for l in list(product(*[['0','1'] for i in range(4)]))]

def hamming_distance(str1, str2):
    """
    Calculate the Hamming distance between two strings.
    """
    return sum(c1 != c2 for c1, c2 in zip(str1, str2))

def encode_hamming_8_4(data):
    """
    Encode a 4-bit data into an 8-bit (8, 4) Hamming code.

    Parameters:
    data (str): A string of 4 bits (e.g., '1011').

    Returns:
    str: 8-bit Hamming code.
    """
    if len(data) != 4 or any(bit not in ['0', '1'] for bit in data):
        return "Invalid data. Please provide 4 bits."

    # Place data bits
    code = ['P1', 'P2', data[0], 'P4', data[1], data[2], data[3], 'P8']

    # Parity bit positions
    parity_positions = [1, 2, 4, 8]

    # Calculate parity bits
    for p in parity_positions:
        parity = 0
        for i in range(1, 9):
            if (i & p) or i == p:
                parity ^= int(code[i-1] if code[i-1] not in ['P1', 'P2', 'P4', 'P8'] else 0)
        code[p-1] = str(parity)

    return ''.join(code)

def decode_hamming_8_4(received_code):
    """
    Decode an 8-bit (8, 4) Hamming code.

    Parameters:
    received_code (str): An 8-bit Hamming code.

    Returns:
    str: The corrected 4-bit data, or an error message if invalid input.
    """
    if len(received_code) != 8 or any(bit not in ['0', '1'] for bit in received_code):
        return "Invalid code. Please provide 8 bits."

    # Parity bit positions
    parity_positions = [1, 2, 4, 8]

    # Calculate syndrome
    syndrome = ''
    for p in parity_positions:
        parity = 0
        for i in range(1, 9):
            if (i & p) or i == p:
                parity ^= int(received_code[i-1])
        syndrome = str(parity) + syndrome

    # Detect and correct error
    error_position = int(syndrome, 2)
    if error_position != 0:
        if error_position > 8:
            return "Uncorrectable error detected"
        
        corrected_code = list(received_code)
        corrected_code[error_position - 1] = '1' if received_code[error_position - 1] == '0' else '0'
        received_code = ''.join(corrected_code)

    # Extract original data
    data_positions = [3, 5, 6, 7]
    original_data = ''.join(received_code[i-1] for i in data_positions)

    return original_data

def decode_hamming_8_4_with_guess(received_code):
    """
    Decode an 8-bit (8, 4) Hamming code, guessing the most probable message in case of uncorrectable errors.

    Parameters:
    received_code (str): An 8-bit Hamming code.

    Returns:
    str: The corrected 4-bit data, or the most probable data in case of uncorrectable error.
    """
    if len(received_code) != 8 or any(bit not in ['0', '1'] for bit in received_code):
        return "Invalid code. Please provide 8 bits."

    # Standard decoding first
    decoded = decode_hamming_8_4(received_code)
    if decoded != "Uncorrectable error detected":
        return decoded

    # In case of uncorrectable error, find the most probable message
    min_distance = len(received_code) + 1
    most_probable_message = None

    for i in range(8):
        # Generate single-bit error correction
        corrected_code = list(received_code)
        corrected_code[i] = '1' if corrected_code[i] == '0' else '0'
        corrected_code = ''.join(corrected_code)

        # Decode the corrected code
        decoded = decode_hamming_8_4(corrected_code)
        if decoded != "Uncorrectable error detected":
            # Calculate Hamming distance
            distance = hamming_distance(received_code, corrected_code)
            if distance < min_distance:
                min_distance = distance
                most_probable_message = decoded

    return most_probable_message if most_probable_message is not None else "No probable message found"


