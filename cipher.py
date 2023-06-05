# This program encrypts or decrypts messages into a very simple cryptographic hash or plain text.
# This choice depends on the users input. 

def hash():
    key = 'abcdefghijklmnopqrstuvwxyz !'
    value = key[-1] + key[0:-1]
# Encrypt and decrypt methods.
    encrypt = dict(zip(key, value))
    decrypt = dict(zip(value, key))
# Take user input.
    message = input("Please enter text here: ")
    type = input("Do you want to encrypt(E) or decrypt(D)?: ")
# Encrypt method.
    if type.upper() == 'E':
        output = ''.join([encrypt[letter]for letter in message.lower()])
# Decrypt method.
    elif type.upper() == 'D':
        output = ''.join([decrypt[letter] for letter in message.lower()])
# False input method.
    else:
        print('False input. Please enter E or D')
        
    return output
# Print the final message.
print(hash())