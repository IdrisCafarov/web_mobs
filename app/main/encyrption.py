# Constants and Tables
initial_permutation = [
    58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7
]

final_permutation = [
    40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25
]

expansion_table = [
    32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11,
    12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21,
    22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1
]

s_boxes = [
    [
        # S-box 1
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    [
        # S-box 2
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    [
        # S-box 3
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    [
        # S-box 4
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    [
        # S-box 5
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    [
        # S-box 6
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    [
        # S-box 7
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    [
        # S-box 8
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]


permutation = [
    16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25
]

initial_permutation_inv = [
    40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25
]

key_permutation_1 = [
    57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2,
    59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39,
    31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37,
    29, 21, 13, 5, 28, 20, 12, 4
]

key_permutation_2 = [
    14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4,
    26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32
]

shift_schedule = [
    1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1
]





# Helper Functions
def string_to_binary(text):
    binary_list = [bin(ord(char))[2:].zfill(8) for char in text]
    binary_string = ''.join(binary_list)
    
    # Check if the binary string is shorter than 64 bits
    if len(binary_string) < 64:
        # Pad with zeros on the right to make it 64 bits
        binary_string = binary_string.ljust(64, '0')
    
    return binary_string




def binary_to_string(binary_data):
    # Split the binary data into 8-bit chunks
    binary_chunks = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]

    # Convert each 8-bit chunk to an integer and then to a character
    characters = [chr(int(chunk, 2)) for chunk in binary_chunks]

    # Join the characters into a string
    text = ''.join(characters)

    return text


def permute(data, table):
    """Permute the bits of data according to the provided table."""
    return ''.join(data[i - 1] for i in table)

def left_shift(data, shift_count):
    """Perform a circular left shift on the data."""
    return data[shift_count:] + data[:shift_count]

def xor(a, b):
    """Perform a bitwise XOR operation between two strings of bits."""
    return ''.join('0' if x == y else '1' for x, y in zip(a, b))

# Key Generation
def generate_subkeys(key):
    # Perform PC-1 permutation on the key
    key = permute(key, key_permutation_1)
    subkeys = []
    left, right = key[:28], key[28:]
    for round_num in range(16):
        # Perform circular left shifts on left and right halves
        left = left_shift(left, shift_schedule[round_num])
        right = left_shift(right, shift_schedule[round_num])
        # Perform PC-2 permutation on the concatenated left and right halves
        subkey = permute(left + right, key_permutation_2)
        subkeys.append(subkey)
    return subkeys

# Initial and Final Permutations
def perform_initial_permutation(data):
    print(data)
    return permute(data, initial_permutation)

def perform_final_permutation(data):
    return permute(data, final_permutation)

# Expansion and S-boxes
def expand_data(data):
    return permute(data, expansion_table)

def substitute_data(data):
    blocks = [data[i:i+6] for i in range(0, len(data), 6)]
    result = ''
    for i, block in enumerate(blocks):
        row = int(block[0] + block[5], 2)
        col = int(block[1:5], 2)
        s_box_value = s_boxes[i][row][col]
        result += format(s_box_value, '04b')
    return result

# Rounds
def perform_round(data, subkey):
    left, right = data[:32], data[32:]
    expanded_right = expand_data(right)
    xored = xor(expanded_right, subkey)
    substituted = substitute_data(xored)
    permuted = permute(substituted, permutation)
    new_right = xor(left, permuted)
    return right + new_right

# Encryption
def des_encrypt(plaintext, key):
    # Initial Permutation
    data = perform_initial_permutation(plaintext)

    # Key Generation
    subkeys = generate_subkeys(key)

    # 16 Rounds
    for subkey in subkeys:
        data = perform_round(data, subkey)

    # Swap left and right halves
    data = data[32:] + data[:32]

    # Final Permutation
    ciphertext = perform_final_permutation(data)

    return ciphertext

# Decryption
def des_decrypt(ciphertext, key):
    # Initial Permutation
    data = perform_initial_permutation(ciphertext)

    # Key Generation
    subkeys = generate_subkeys(key)

    # Reverse the subkeys
    subkeys = subkeys[::-1]

    # 16 Rounds
    for subkey in subkeys:
        data = perform_round(data, subkey)

    # Swap left and right halves
    data = data[32:] + data[:32]

    # Final Permutation
    plaintext = perform_final_permutation(data)

    return plaintext

