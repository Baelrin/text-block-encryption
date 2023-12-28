import pyAesCrypt

password = input('Enter password: ')

# encrypt
pyAesCrypt.encryptFile('data.txt', 'data.txt.aes', password)

# decrypt
pyAesCrypt.decryptFile('data.txt.aes', 'dataout.txt', password)