# This script requires the following Python packages:
# - qrcode
# - pillow (PIL)
# 
# You can install these packages using pip:
# pip install qrcode[pil] pillow
#
# Additionally, you need to have a BIP39 wordlist file named 'bip39_wordlist.txt'
# in the same directory as this script.
#
# The script generates a matrix representation and a QR code based on the BIP39 words you input.
# The QR code will be saved as 'bip39_qr_code.png' in the current directory.


import qrcode
from PIL import Image

def load_bip39_wordlist():
    with open("bip39_wordlist.txt", "r") as file:
        wordlist = file.read().splitlines()
    return wordlist

def find_bip39_numbers(words):
    wordlist = load_bip39_wordlist()
    word_number_pairs = []
    for word in words:
        if word in wordlist:
            number = wordlist.index(word) + 1
            word_number_pairs.append((word, number))
        else:
            word_number_pairs.append((word, "Word not found in BIP39 list"))
    return word_number_pairs

def calculate_binary_representation(number):
    if number == 2048:
        return [0] * 11
    binary_rep = bin(number)[2:].zfill(11)
    return [int(bit) for bit in binary_rep]

def generate_matrix(words):
    matrix = []
    word_number_pairs = find_bip39_numbers(words)
    for _, number in word_number_pairs:
        if isinstance(number, int):
            binary_rep = calculate_binary_representation(number)
            matrix.append(binary_rep)
        else:
            matrix.append([0] * 11)
    return matrix

def convert_to_emoji(value):
    if value == 1:
        return "✅"  # OK emoji
    else:
        return "❌"  # Empty space

def generate_qr_code(words):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(" ".join(words))
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("bip39_qr_code.png")

def main():
    user_input = input("Enter your BIP39 24 or 12 words (separated by spaces): ")
    words = user_input.strip().split()
    position = 0
    word_number_pairs = find_bip39_numbers(words)
    for word, number in word_number_pairs:
        position = position + 1
        print(f"{str(position).zfill(2)} - {word} - {number}")

    matrix = generate_matrix(words)

    print("Matrix Representation:")
    line = 0
    for row in matrix:
        line = line + 1
        emoji_row = [convert_to_emoji(bit) for bit in row]
        print(f"{str(line).zfill(2)} - {''.join(emoji_row)}")

    generate_qr_code(words)
    print("QR code saved as 'bip39_qr_code.png'")

if __name__ == "__main__":
    main()