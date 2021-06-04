Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
Letters = Letters.lower()

def encrypt(message, key):
    encrypted = ''
    for chars in message:
        if chars in Letters:
            num = Letters.find(chars)
            num += key
            encrypted +=  Letters[num]

    return encrypted
#run again to get the decrypt then put the result of the encrypt into the Enter your message in the Decrypt
def decrypt(message, key):
    decrypted = ''
    for chars in message:
        if chars in Letters:
            num = Letters.find(chars)
            num -= key
            decrypted +=  Letters[num]

    return decrypted

def main():
    message = str(input('Enter your message: '))
    choice = input('Encrypt or Decrypt? [e/d]: ')
    key = int(input('Enter the shift key [1 - 26]: '))

    if choice.lower().startswith('e'):
        print("The Decrypted Value: ",decrypt(message, key))
    else:
        print("The Encrypted Value: ",encrypt(message, key))

if __name__ == '__main__':
    main()