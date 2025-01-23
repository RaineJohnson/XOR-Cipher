# Define the test plain texts and keys
plain_texts = [
    "1100010101100110",
    "0010100111000010",
    "0101110011100010",
    "1110011111000011",
    "0011111011110010"
]

test_keys = [
    "1110100100111110",
    "1000110110000011"
]

# Function to encrypt a plain text with a key using XOR
def encrypt(plain_text, key):
    # Ensure both plain_text and key are the same length
    if len(plain_text) != len(key):
        raise ValueError("Plain text and key must be of the same length.")

    # Perform XOR operation
    encrypted_text = "".join(
        str(int(plain_text[i]) ^ int(key[i])) for i in range(len(plain_text))
    )
    return encrypted_text

# Function to calculate the number of differing bits between two binary strings
def count_differing_bits(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Strings must be of the same length.")
    return sum(1 for a, b in zip(str1, str2) if a != b)

# Function to calculate the avalanche effect
def calculate_avalanche_effect():
    total_bits_changed = 0
    total_rounds = len(plain_texts) * len(test_keys) * len(test_keys[0])

    for key in test_keys:
        for plain_text in plain_texts:
            # Original ciphertext
            original_ciphertext = encrypt(plain_text, key)

            # Iterate through each bit in the key
            for i in range(len(key)):
                # Flip one bit in the key
                modified_key = (
                    key[:i] + ('1' if key[i] == '0' else '0') + key[i+1:]
                )

                # Encrypt with the modified key
                modified_ciphertext = encrypt(plain_text, modified_key)

                # Count differing bits between original and modified ciphertexts
                bits_changed = count_differing_bits(original_ciphertext, modified_ciphertext)
                total_bits_changed += bits_changed

    # Calculate average avalanche effect
    average_avalanche_effect = total_bits_changed / (total_rounds * len(key))
    return average_avalanche_effect

# Perform encryption for each plain text with each key
for key in test_keys:
    print(f"Encrypting with key: {key}")
    for plain_text in plain_texts:
        encrypted = encrypt(plain_text, key)
        print(f"Plain text:  {plain_text} -> Encrypted text: {encrypted}")
    print()

# Calculate and print the avalanche effect
average_effect = calculate_avalanche_effect()
print(f"Average Avalanche Effect: {average_effect:.6f}")
