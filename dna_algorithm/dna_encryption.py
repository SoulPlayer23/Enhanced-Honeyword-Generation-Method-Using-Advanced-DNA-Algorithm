import random
import binascii
import string
from unicodedata import decimal

charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

input_text = input("Enter message to be encrypted:")

otp = "".join(random.sample(charset, len(input_text)))
print(otp)

ascii_inp_txt = 0
ascii_inp_txt = ''.join(format(ord(i), '08b') for i in input_text)


ascii_otp = 0
ascii_otp = ''.join(format(ord(i), '08b') for i in otp)

if(len(ascii_inp_txt) % 2 != 0):
    ascii_inp_txt = ascii_inp_txt.zfill(len(ascii_inp_txt)+1)
if(len(ascii_inp_txt) % 2 != 0):
    ascii_otp = ascii_otp.zfill(len(ascii_otp)+1)

print(ascii_inp_txt)
#print(ascii_otp)

def xor(a, b, n):
    ans = ""
    for i in range(n):
        if(a[i] == b[i]):
            ans+="0"
        else:
            ans+="1"
    return ans

#Encryption

encrypted_message = xor(ascii_inp_txt, ascii_otp, len(ascii_inp_txt))
print(encrypted_message)

enciphered_text = ""

for i in range(0, len(encrypted_message), 2):
    if(encrypted_message[i] + encrypted_message[i+1] == '00'):
        enciphered_text += 'A'
    elif(encrypted_message[i] + encrypted_message[i+1] == '01'):
        enciphered_text += 'T'
    elif(encrypted_message[i] + encrypted_message[i+1] == '10'):
        enciphered_text += 'C'
    elif(encrypted_message[i] + encrypted_message[i+1] == '11'):
        enciphered_text += 'G'

print(enciphered_text)

#Decryption

deciphered_text = ""

for i in range(0, len(enciphered_text)):
    if(enciphered_text[i] == 'A'):
        deciphered_text += '00'
    elif(enciphered_text[i] == 'T'):
        deciphered_text += '01'
    elif(enciphered_text[i] == 'C'):
        deciphered_text += '10'
    elif(enciphered_text[i] == 'G'):
        deciphered_text += '11'

print(deciphered_text)

decrypted_message = xor(deciphered_text, ascii_otp, len(deciphered_text))
print(decrypted_message)

def bintodec(binary):
    string = int(binary, 2)
    return string

str_data = ' '
for i in range(0, len(decrypted_message), 8):
    temp_data = decrypted_message[i:i+8]
    decimal_data = bintodec(temp_data)
    str_data = str_data + chr(decimal_data)

print(str_data)