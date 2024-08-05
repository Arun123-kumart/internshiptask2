# Taking the path of the encrypted image to decrypt
path = r"C:\Users\Bhoomika T\OneDrive\Pictures\tcs.png"

# Taking the decryption key as input (same as the encryption key)
key = int(input('Enter the key for decryption of the image: '))

# Print the path of image file and the key used for decryption
print('The path of the file:', path)
print('Key for decryption:', key)

# Open the encrypted file for reading in binary mode
with open(path, 'rb') as fin:
    encrypted_image = fin.read()

# Convert the encrypted image into a bytearray to perform decryption easily on numeric data
encrypted_image = bytearray(encrypted_image)

# Performing the XOR operation on each value of the bytearray to decrypt
for index, values in enumerate(encrypted_image):
    encrypted_image[index] = values ^ key

# Open the file for writing in binary mode and write the decrypted data back to the image
with open(path, 'wb') as fout:
    fout.write(encrypted_image)

print('Decryption done...')

