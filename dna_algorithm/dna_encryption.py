import imp
import random

from dna_algorithm import lookuptables as l

charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
lookupno = random.randint(1,5)

def xor(a, b, n):
        ans = ""
        for i in range(n):
            if(a[i] == b[i]):
                ans+="0"
            else:
                ans+="1"
        return ans


def dna_encryption(input_text):
    case_flag = ''
    for i in input_text:
        if i.isupper():
            case_flag += '1'
        elif i.islower():
            case_flag +='0'
        elif not i.isalnum() or i.isalnum:
            case_flag += '0'

    lookupt = l.lookup[lookupno]

    dna_base = ''.join(format(lookupt[i.upper()]) for i in input_text)

    otp = "".join(random.sample(charset, len(input_text*3)))

    ascii_inp_txt = 0
    ascii_inp_txt = ''.join(format(ord(i), '08b') for i in dna_base)


    ascii_otp = 0
    ascii_otp = ''.join(format(ord(i), '08b') for i in otp)

    if(len(ascii_inp_txt) % 2 != 0):
        ascii_inp_txt = ascii_inp_txt.zfill(len(ascii_inp_txt)+1)
    if(len(ascii_inp_txt) % 2 != 0):
        ascii_otp = ascii_otp.zfill(len(ascii_otp)+1)


    #Encryption
    encrypted_message = xor(ascii_inp_txt, ascii_otp, len(ascii_inp_txt))

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

    return enciphered_text, ascii_otp, lookupno, case_flag


def dna_decryption(enciphered_text, ascii_otp, lookupno, case_flag):

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



    decrypted_message = xor(deciphered_text, ascii_otp, len(deciphered_text))

    def bintodec(binary):
        string = int(binary, 2)
        return string

    str_data = ''
    for i in range(0, len(decrypted_message), 8):
        temp_data = decrypted_message[i:i+8]
        decimal_data = bintodec(temp_data)
        str_data = str_data + chr(decimal_data)



    def get_key(val):
        for key, value in l.lookup[lookupno].items():
            if val == value:
                return key

    output_data = ''
    for i in range(0, len(str_data), 3):
        temp_data = str_data[i:i+3]
        output_data = output_data + get_key(temp_data)


    final_output = ''
    for i in range(0,len(output_data)):
        if case_flag[i]=='0':
            final_output += output_data[i].lower()
        elif case_flag[i] == '1':
            final_output += output_data[i]
        
    return final_output