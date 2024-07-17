# 11 Bits Matrix Generator
11 Bits matrix generator initially developed for the [Black Tag](https://x.com/BlackTagBR) seed plate

![image](https://github.com/user-attachments/assets/01c953e6-9201-400b-9910-15d030d64f68)

## BlackTag Seed Plate:

![image](https://github.com/user-attachments/assets/0a01f174-0ed5-4e25-bbab-1c8bb7ab22d2)

[Tutorial on YouTube](https://www.youtube.com/watch?v=Cyp3cZ74tPk&t=199s&ab_channel=Morata%E2%9A%A1%EF%B8%8F)

# About
The script generates a matrix representation and a QR code based on the BIP39 words you input.
The QR code will be saved as 'bip39_qr_code.png' in the current directory.

### Credits: All my thanks to our partner [@jvx](https://github.com/jvxis) who came up with this script

# This script requires the following Python packages:
 * qrcode
 * pillow (PIL)
 
### You can install these packages using pip:
```
pip install qrcode[pil] pillow
```
Additionally, you need to have a BIP39 wordlist file named 'bip39_wordlist.txt' in the same directory as this script. Save this file as 'bip39_wordlist.txt'.

### Running Script
```
cd 11bits-matrix-generator
```

```
python3 11bits-mxgen.py
```

* Then enter your complete seed, whether it is 12 words or 24 words, with the words separated by spaces (do not put them with their respective numbers) and hit enter button. The script will give you a list of words numbered in order and with their respective numbers from the beep 39 list.

* You don't need to input 12 or 24 words, the script accepts any number.

* At the same time, the script will deliver a matrix indicating where to mark the seed plate with the punch. Check emojis indicate the positions to be marked and "X" emojis indicate spaces that will be left blank.

* A QRCode of the input seed will also be generated in a .png file
