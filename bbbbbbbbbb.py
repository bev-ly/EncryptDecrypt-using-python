Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
Letters = Letters.lower()

def decrypt(message, key):
    decrypted = ''
    for chars in message:
        if chars in Letters:
            num = Letters.find(chars)
            num -= key
            decrypted +=  Letters[num]

    return decrypted
message = str(input('Enter your message: '))
key = int(input('Enter your key [1 - 26]: '))
print("The Decrypted Value: ",decrypt(message, key))