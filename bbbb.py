def ccipher(raw_text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted_alphabet = alphabet[26-key:]+alphabet[0:(26-key)]
    cipher_text = ""
    for i in range(len(raw_text)):
        char = raw_text[i]
        idx = alphabet.find(char.upper())
        if idx == -1:
            cipher_text = cipher_text + char
        elif char.islower():
            cipher_text = cipher_text + shifted_alphabet[idx].lower()
        else:
            cipher_text = cipher_text + shifted_alphabet[idx] 
    return(cipher_text)
strmsg = str(input('Enter Value to Encrypt: '))
key = int(input('Enter the shif key between 1 to 26: '))
print ("Decrypted Value: ",ccipher(strmsg, key))