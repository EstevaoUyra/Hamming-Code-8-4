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

